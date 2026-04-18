"""Tests for predictive maintenance alerting and reports."""

from datetime import datetime, timedelta

import scripts.predictive_maintenance as pm_module
from scripts.ai_core import AIResponse
from scripts.predictive_maintenance import PerformanceMetrics, UsageStats


class DummyAnalytics:
    def __init__(self, usage_stats, performance_metrics):
        self._usage_stats = usage_stats
        self._performance_metrics = performance_metrics
        self.database_path = ":memory:"

    def get_usage_stats(self, _template_name, _days=30):
        return self._usage_stats

    def get_performance_metrics(self, _template_name, _days=30):
        return self._performance_metrics


class DummyAICore:
    def __init__(self, enabled=False, response_text=None):
        self.enabled = enabled
        self.response_text = response_text

    def is_enabled(self, _feature=None):
        return self.enabled

    def chat_completion(self, _messages):
        return AIResponse(
            content=self.response_text or "{}",
            confidence=0.8,
            provider="stub",
            model="m",
            metadata={},
        )


def test_analyze_template_generates_expected_alerts(monkeypatch, sample_usage_stats_data):
    usage_stats = UsageStats(
        template_name=sample_usage_stats_data["template_name"],
        total_uses=sample_usage_stats_data["total_uses"],
        success_rate=sample_usage_stats_data["success_rate"],
        avg_build_time=sample_usage_stats_data["avg_build_time"],
        last_used=datetime.now() - timedelta(days=90),
        common_parameters=sample_usage_stats_data["common_parameters"],
        error_patterns=sample_usage_stats_data["error_patterns"],
        performance_trends=sample_usage_stats_data["performance_trends"],
    )
    performance_metrics = PerformanceMetrics(
        template_name=sample_usage_stats_data["template_name"],
        avg_build_time_seconds=450.0,
        avg_image_size_mb=1500.0,
        success_rate=0.5,
        resource_efficiency=0.2,
        security_score=0.4,
        maintenance_score=0.3,
    )

    monkeypatch.setattr(
        pm_module,
        "TemplateAnalytics",
        lambda: DummyAnalytics(usage_stats, performance_metrics),
    )
    monkeypatch.setattr(pm_module, "get_ai_core", lambda: DummyAICore(enabled=False))

    maintenance = pm_module.PredictiveMaintenance()
    alerts = maintenance.analyze_template(sample_usage_stats_data["template_name"])

    categories = {alert.category for alert in alerts}
    severities = {alert.severity for alert in alerts}

    assert "performance" in categories
    assert "security" in categories
    assert "high" in severities
    assert len(alerts) >= 4


def test_generate_maintenance_report_summarizes_alerts(monkeypatch, sample_usage_stats_data):
    usage_stats = UsageStats(
        template_name=sample_usage_stats_data["template_name"],
        total_uses=sample_usage_stats_data["total_uses"],
        success_rate=sample_usage_stats_data["success_rate"],
        avg_build_time=sample_usage_stats_data["avg_build_time"],
        last_used=datetime.now() - timedelta(days=90),
        common_parameters=sample_usage_stats_data["common_parameters"],
        error_patterns=sample_usage_stats_data["error_patterns"],
        performance_trends=sample_usage_stats_data["performance_trends"],
    )
    performance_metrics = PerformanceMetrics(
        template_name=sample_usage_stats_data["template_name"],
        avg_build_time_seconds=450.0,
        avg_image_size_mb=1500.0,
        success_rate=0.5,
        resource_efficiency=0.2,
        security_score=0.4,
        maintenance_score=0.3,
    )

    monkeypatch.setattr(
        pm_module,
        "TemplateAnalytics",
        lambda: DummyAnalytics(usage_stats, performance_metrics),
    )
    monkeypatch.setattr(pm_module, "get_ai_core", lambda: DummyAICore(enabled=False))

    maintenance = pm_module.PredictiveMaintenance()
    report = maintenance.generate_maintenance_report(sample_usage_stats_data["template_name"])

    assert report["scope"] == sample_usage_stats_data["template_name"]
    assert report["templates_analyzed"] == 1
    assert report["total_alerts"] >= 1
    assert isinstance(report["high_priority_actions"], list)


def test_ai_maintenance_suggestions_are_parsed(monkeypatch, sample_usage_stats_data):
    usage_stats = UsageStats(
        template_name=sample_usage_stats_data["template_name"],
        total_uses=sample_usage_stats_data["total_uses"],
        success_rate=sample_usage_stats_data["success_rate"],
        avg_build_time=sample_usage_stats_data["avg_build_time"],
        last_used=datetime.now() - timedelta(days=10),
        common_parameters=sample_usage_stats_data["common_parameters"],
        error_patterns=sample_usage_stats_data["error_patterns"],
        performance_trends=sample_usage_stats_data["performance_trends"],
    )
    performance_metrics = PerformanceMetrics(
        template_name=sample_usage_stats_data["template_name"],
        avg_build_time_seconds=120.0,
        avg_image_size_mb=500.0,
        success_rate=0.95,
        resource_efficiency=0.9,
        security_score=0.8,
        maintenance_score=0.8,
    )

    ai_payload = (
        "Recommendation:\n"
        '{"alerts":[{"severity":"medium","category":"maintenance","title":"Refresh deps",'
        '"description":"Dependencies are aging.","recommended_action":"Update lockfiles.","confidence":0.88}]}'
    )

    monkeypatch.setattr(
        pm_module,
        "TemplateAnalytics",
        lambda: DummyAnalytics(usage_stats, performance_metrics),
    )
    monkeypatch.setattr(
        pm_module,
        "get_ai_core",
        lambda: DummyAICore(enabled=True, response_text=ai_payload),
    )

    maintenance = pm_module.PredictiveMaintenance()
    alerts = maintenance._get_ai_maintenance_suggestions(
        sample_usage_stats_data["template_name"], usage_stats, performance_metrics
    )

    assert len(alerts) == 1
    assert alerts[0].title == "Refresh deps"
    assert alerts[0].data["source"] == "ai_analysis"

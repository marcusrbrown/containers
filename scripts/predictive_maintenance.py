"""
Predictive Maintenance for Container Templates

This module provides AI-powered predictive maintenance capabilities:
- Usage pattern analysis
- Template performance monitoring
- Proactive issue detection
- Automated maintenance suggestions
- Template lifecycle management
"""

import json
import logging
import sqlite3
import statistics
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .ai_core import get_ai_core

logger = logging.getLogger(__name__)


@dataclass
class UsageStats:
    """Template usage statistics"""

    template_name: str
    total_uses: int
    success_rate: float
    avg_build_time: float
    last_used: datetime
    common_parameters: Dict[str, Any]
    error_patterns: List[str]
    performance_trends: List[float]


@dataclass
class MaintenanceAlert:
    """Maintenance alert or recommendation"""

    template_name: str
    severity: str  # low, medium, high, critical
    category: str  # performance, security, compatibility, deprecated
    title: str
    description: str
    recommended_action: str
    confidence: float
    created_at: datetime
    data: Dict[str, Any]


@dataclass
class PerformanceMetrics:
    """Performance metrics for templates"""

    template_name: str
    avg_build_time_seconds: float
    avg_image_size_mb: float
    success_rate: float
    resource_efficiency: float
    security_score: float
    maintenance_score: float


class TemplateAnalytics:
    """Analytics and data collection for templates"""

    def __init__(self, database_path: str = "template_analytics.db"):
        self.database_path = database_path
        self._init_database()
        self.ai_core = get_ai_core()

    def _init_database(self):
        """Initialize analytics database with comprehensive schema"""
        conn = sqlite3.connect(self.database_path)

        # Usage tracking table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS template_usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_name TEXT NOT NULL,
                action TEXT NOT NULL,
                success BOOLEAN NOT NULL,
                parameters TEXT,
                duration_seconds REAL,
                image_size_mb REAL,
                build_logs TEXT,
                error_message TEXT,
                user_id TEXT,
                project_type TEXT,
                ai_provider TEXT,
                timestamp INTEGER NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        # Performance metrics table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_name TEXT NOT NULL,
                metric_type TEXT NOT NULL,
                metric_value REAL NOT NULL,
                measurement_time INTEGER NOT NULL,
                metadata TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        # Issues and alerts table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS maintenance_alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_name TEXT NOT NULL,
                severity TEXT NOT NULL,
                category TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                recommended_action TEXT NOT NULL,
                confidence REAL NOT NULL,
                resolved BOOLEAN DEFAULT FALSE,
                resolution_notes TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                resolved_at DATETIME
            )
        """
        )

        # Template versions and updates table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS template_versions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_name TEXT NOT NULL,
                version TEXT NOT NULL,
                changes TEXT,
                compatibility_notes TEXT,
                migration_guide TEXT,
                deprecated BOOLEAN DEFAULT FALSE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        # User feedback table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS user_feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_name TEXT NOT NULL,
                rating INTEGER CHECK (rating BETWEEN 1 AND 5),
                feedback_text TEXT,
                category TEXT,
                user_id TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        conn.commit()
        conn.close()

    def log_template_usage(
        self,
        template_name: str,
        action: str,
        success: bool,
        duration: float = None,
        parameters: Dict[str, Any] = None,
        image_size_mb: float = None,
        error_message: str = None,
        build_logs: str = None,
        user_id: str = None,
        project_type: str = None,
        ai_provider: str = None,
    ):
        """Log template usage event"""
        try:
            conn = sqlite3.connect(self.database_path)
            conn.execute(
                """
                INSERT INTO template_usage
                (template_name, action, success, parameters, duration_seconds,
                 image_size_mb, build_logs, error_message, user_id, project_type,
                 ai_provider, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    template_name,
                    action,
                    success,
                    json.dumps(parameters) if parameters else None,
                    duration,
                    image_size_mb,
                    build_logs,
                    error_message,
                    user_id,
                    project_type,
                    ai_provider,
                    int(time.time()),
                ),
            )
            conn.commit()
            conn.close()

        except Exception as e:
            logger.error(f"Failed to log template usage: {e}")

    def log_performance_metric(
        self,
        template_name: str,
        metric_type: str,
        metric_value: float,
        metadata: Dict[str, Any] = None,
    ):
        """Log performance metric"""
        try:
            conn = sqlite3.connect(self.database_path)
            conn.execute(
                """
                INSERT INTO performance_metrics
                (template_name, metric_type, metric_value, measurement_time, metadata)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    template_name,
                    metric_type,
                    metric_value,
                    int(time.time()),
                    json.dumps(metadata) if metadata else None,
                ),
            )
            conn.commit()
            conn.close()

        except Exception as e:
            logger.error(f"Failed to log performance metric: {e}")

    def create_maintenance_alert(self, alert: MaintenanceAlert):
        """Create a maintenance alert"""
        try:
            conn = sqlite3.connect(self.database_path)
            conn.execute(
                """
                INSERT INTO maintenance_alerts
                (template_name, severity, category, title, description,
                 recommended_action, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    alert.template_name,
                    alert.severity,
                    alert.category,
                    alert.title,
                    alert.description,
                    alert.recommended_action,
                    alert.confidence,
                ),
            )
            conn.commit()
            conn.close()

        except Exception as e:
            logger.error(f"Failed to create maintenance alert: {e}")

    def get_usage_stats(self, template_name: str, days: int = 30) -> UsageStats:
        """Get usage statistics for a template"""
        cutoff_time = int(time.time()) - (days * 24 * 3600)

        conn = sqlite3.connect(self.database_path)

        # Basic usage stats
        cursor = conn.execute(
            """
            SELECT COUNT(*), AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END),
                   AVG(duration_seconds), MAX(timestamp)
            FROM template_usage
            WHERE template_name = ? AND timestamp > ?
        """,
            (template_name, cutoff_time),
        )

        row = cursor.fetchone()
        total_uses = row[0] if row[0] else 0
        success_rate = row[1] if row[1] else 0.0
        avg_build_time = row[2] if row[2] else 0.0
        last_used_timestamp = row[3] if row[3] else 0

        # Common parameters
        cursor = conn.execute(
            """
            SELECT parameters FROM template_usage
            WHERE template_name = ? AND timestamp > ? AND parameters IS NOT NULL
        """,
            (template_name, cutoff_time),
        )

        parameters_list = []
        for row in cursor.fetchall():
            try:
                params = json.loads(row[0])
                parameters_list.append(params)
            except json.JSONDecodeError:
                continue

        common_parameters = self._analyze_common_parameters(parameters_list)

        # Error patterns
        cursor = conn.execute(
            """
            SELECT error_message FROM template_usage
            WHERE template_name = ? AND timestamp > ? AND success = FALSE
            AND error_message IS NOT NULL
        """,
            (template_name, cutoff_time),
        )

        error_patterns = [row[0] for row in cursor.fetchall()]

        # Performance trends (daily averages)
        cursor = conn.execute(
            """
            SELECT DATE(created_at) as day, AVG(duration_seconds)
            FROM template_usage
            WHERE template_name = ? AND timestamp > ? AND duration_seconds IS NOT NULL
            GROUP BY DATE(created_at)
            ORDER BY day
        """,
            (template_name, cutoff_time),
        )

        performance_trends = [row[1] for row in cursor.fetchall()]

        conn.close()

        return UsageStats(
            template_name=template_name,
            total_uses=total_uses,
            success_rate=success_rate,
            avg_build_time=avg_build_time,
            last_used=(
                datetime.fromtimestamp(last_used_timestamp)
                if last_used_timestamp
                else datetime.min
            ),
            common_parameters=common_parameters,
            error_patterns=error_patterns,
            performance_trends=performance_trends,
        )

    def get_performance_metrics(
        self, template_name: str, days: int = 30
    ) -> PerformanceMetrics:
        """Get performance metrics for a template"""
        cutoff_time = int(time.time()) - (days * 24 * 3600)

        conn = sqlite3.connect(self.database_path)

        # Build time metrics
        cursor = conn.execute(
            """
            SELECT AVG(duration_seconds) FROM template_usage
            WHERE template_name = ? AND timestamp > ? AND duration_seconds IS NOT NULL
        """,
            (template_name, cutoff_time),
        )
        avg_build_time = cursor.fetchone()[0] or 0.0

        # Image size metrics
        cursor = conn.execute(
            """
            SELECT AVG(image_size_mb) FROM template_usage
            WHERE template_name = ? AND timestamp > ? AND image_size_mb IS NOT NULL
        """,
            (template_name, cutoff_time),
        )
        avg_image_size = cursor.fetchone()[0] or 0.0

        # Success rate
        cursor = conn.execute(
            """
            SELECT AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END) FROM template_usage
            WHERE template_name = ? AND timestamp > ?
        """,
            (template_name, cutoff_time),
        )
        success_rate = cursor.fetchone()[0] or 0.0

        conn.close()

        # Calculate derived metrics
        resource_efficiency = self._calculate_resource_efficiency(
            avg_build_time, avg_image_size
        )
        security_score = self._calculate_security_score(template_name)
        maintenance_score = self._calculate_maintenance_score(template_name)

        return PerformanceMetrics(
            template_name=template_name,
            avg_build_time_seconds=avg_build_time,
            avg_image_size_mb=avg_image_size,
            success_rate=success_rate,
            resource_efficiency=resource_efficiency,
            security_score=security_score,
            maintenance_score=maintenance_score,
        )

    def _analyze_common_parameters(
        self, parameters_list: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Analyze common parameter patterns"""
        if not parameters_list:
            return {}

        # Count parameter values
        value_counts = {}
        for params in parameters_list:
            for key, value in params.items():
                if key not in value_counts:
                    value_counts[key] = {}

                value_str = str(value)
                if value_str not in value_counts[key]:
                    value_counts[key][value_str] = 0
                value_counts[key][value_str] += 1

        # Find most common values
        common_parameters = {}
        for key, values in value_counts.items():
            if values:
                most_common_value = max(values.items(), key=lambda x: x[1])
                common_parameters[key] = most_common_value[0]

        return common_parameters

    def _calculate_resource_efficiency(
        self, build_time: float, image_size: float
    ) -> float:
        """Calculate resource efficiency score (0-1)"""
        if build_time <= 0 and image_size <= 0:
            return 0.5  # Neutral score for no data

        # Normalize build time (lower is better)
        build_score = max(0, 1 - (build_time / 300))  # 300 seconds as reference

        # Normalize image size (lower is better)
        size_score = max(0, 1 - (image_size / 1000))  # 1GB as reference

        # Weighted average
        return build_score * 0.4 + size_score * 0.6

    def _calculate_security_score(self, template_name: str) -> float:
        """Calculate security score based on template characteristics"""
        # This would be enhanced with actual security scanning results
        # For now, return a placeholder based on template name patterns

        security_indicators = {
            "alpine": 0.9,  # Alpine is generally more secure
            "ubuntu": 0.7,
            "debian": 0.7,
            "node": 0.6,
            "python": 0.6,
            "nginx": 0.8,
            "postgres": 0.8,
        }

        template_lower = template_name.lower()
        for indicator, score in security_indicators.items():
            if indicator in template_lower:
                return score

        return 0.5  # Default neutral score

    def _calculate_maintenance_score(self, template_name: str) -> float:
        """Calculate maintenance score based on update frequency and issues"""
        # This would be enhanced with actual maintenance data
        # For now, return a score based on recent usage and issues

        conn = sqlite3.connect(self.database_path)

        # Check for recent alerts
        cursor = conn.execute(
            """
            SELECT COUNT(*) FROM maintenance_alerts
            WHERE template_name = ? AND created_at > datetime('now', '-30 days')
            AND resolved = FALSE
        """,
            (template_name,),
        )

        unresolved_alerts = cursor.fetchone()[0]

        # Check usage consistency
        cursor = conn.execute(
            """
            SELECT COUNT(DISTINCT DATE(created_at)) FROM template_usage
            WHERE template_name = ? AND timestamp > ?
        """,
            (template_name, int(time.time()) - (30 * 24 * 3600)),
        )

        usage_days = cursor.fetchone()[0]

        conn.close()

        # Calculate score (more usage = better maintenance, fewer alerts = better)
        usage_score = min(usage_days / 30.0, 1.0)
        alert_penalty = min(unresolved_alerts * 0.2, 0.8)

        return max(0.1, usage_score - alert_penalty)


class PredictiveMaintenance:
    """AI-powered predictive maintenance system"""

    def __init__(self):
        self.analytics = TemplateAnalytics()
        self.ai_core = get_ai_core()

    def analyze_all_templates(self) -> List[MaintenanceAlert]:
        """Analyze all templates for maintenance issues"""
        alerts = []

        # Get list of all templates from usage data
        conn = sqlite3.connect(self.analytics.database_path)
        cursor = conn.execute(
            """
            SELECT DISTINCT template_name FROM template_usage
            WHERE timestamp > ?
        """,
            (int(time.time()) - (90 * 24 * 3600),),
        )  # Last 90 days

        template_names = [row[0] for row in cursor.fetchall()]
        conn.close()

        for template_name in template_names:
            template_alerts = self.analyze_template(template_name)
            alerts.extend(template_alerts)

        return alerts

    def analyze_template(self, template_name: str) -> List[MaintenanceAlert]:
        """Analyze a specific template for maintenance issues"""
        alerts = []

        # Get usage stats and performance metrics
        usage_stats = self.analytics.get_usage_stats(template_name)
        performance_metrics = self.analytics.get_performance_metrics(template_name)

        # Performance-based alerts
        alerts.extend(
            self._check_performance_issues(
                template_name, usage_stats, performance_metrics
            )
        )

        # Usage pattern alerts
        alerts.extend(self._check_usage_patterns(template_name, usage_stats))

        # Error pattern alerts
        alerts.extend(self._check_error_patterns(template_name, usage_stats))

        # Security alerts
        alerts.extend(self._check_security_issues(template_name, performance_metrics))

        # AI-powered analysis
        if self.ai_core.is_enabled("predictive_maintenance"):
            ai_alerts = self._get_ai_maintenance_suggestions(
                template_name, usage_stats, performance_metrics
            )
            alerts.extend(ai_alerts)

        return alerts

    def _check_performance_issues(
        self,
        template_name: str,
        usage_stats: UsageStats,
        performance_metrics: PerformanceMetrics,
    ) -> List[MaintenanceAlert]:
        """Check for performance-related issues"""
        alerts = []

        # Slow build times
        if performance_metrics.avg_build_time_seconds > 300:  # 5 minutes
            alerts.append(
                MaintenanceAlert(
                    template_name=template_name,
                    severity="medium",
                    category="performance",
                    title="Slow Build Times",
                    description=f"Average build time is {performance_metrics.avg_build_time_seconds:.1f} seconds, which is slower than expected.",
                    recommended_action="Review Dockerfile for optimization opportunities, consider multi-stage builds, and optimize dependency installation.",
                    confidence=0.8,
                    created_at=datetime.now(),
                    data={"avg_build_time": performance_metrics.avg_build_time_seconds},
                )
            )

        # Large image sizes
        if performance_metrics.avg_image_size_mb > 1000:  # 1GB
            alerts.append(
                MaintenanceAlert(
                    template_name=template_name,
                    severity="medium",
                    category="performance",
                    title="Large Image Size",
                    description=f"Average image size is {performance_metrics.avg_image_size_mb:.1f} MB, which may impact deployment speed.",
                    recommended_action="Use multi-stage builds, minimize installed packages, and consider Alpine-based images.",
                    confidence=0.9,
                    created_at=datetime.now(),
                    data={"avg_image_size": performance_metrics.avg_image_size_mb},
                )
            )

        # Low success rate
        if performance_metrics.success_rate < 0.8:
            alerts.append(
                MaintenanceAlert(
                    template_name=template_name,
                    severity="high",
                    category="reliability",
                    title="Low Success Rate",
                    description=f"Build success rate is {performance_metrics.success_rate:.1%}, indicating reliability issues.",
                    recommended_action="Investigate common failure patterns and improve error handling.",
                    confidence=0.95,
                    created_at=datetime.now(),
                    data={"success_rate": performance_metrics.success_rate},
                )
            )

        return alerts

    def _check_usage_patterns(
        self, template_name: str, usage_stats: UsageStats
    ) -> List[MaintenanceAlert]:
        """Check usage patterns for potential issues"""
        alerts = []

        # Declining usage
        if len(usage_stats.performance_trends) > 7:
            recent_trend = statistics.mean(usage_stats.performance_trends[-7:])
            older_trend = statistics.mean(usage_stats.performance_trends[:-7])

            if recent_trend > older_trend * 1.5:  # 50% increase in build time
                alerts.append(
                    MaintenanceAlert(
                        template_name=template_name,
                        severity="medium",
                        category="performance",
                        title="Performance Degradation",
                        description="Build times have increased significantly over the past week.",
                        recommended_action="Investigate recent changes and dependency updates that may be causing slower builds.",
                        confidence=0.7,
                        created_at=datetime.now(),
                        data={
                            "trend_increase": (recent_trend - older_trend) / older_trend
                        },
                    )
                )

        # Stale template (not used recently)
        days_since_last_use = (datetime.now() - usage_stats.last_used).days
        if days_since_last_use > 60:
            alerts.append(
                MaintenanceAlert(
                    template_name=template_name,
                    severity="low",
                    category="maintenance",
                    title="Stale Template",
                    description=f"Template has not been used for {days_since_last_use} days.",
                    recommended_action="Consider deprecating or updating template to modern standards.",
                    confidence=0.6,
                    created_at=datetime.now(),
                    data={"days_since_last_use": days_since_last_use},
                )
            )

        return alerts

    def _check_error_patterns(
        self, template_name: str, usage_stats: UsageStats
    ) -> List[MaintenanceAlert]:
        """Check error patterns for systemic issues"""
        alerts = []

        if not usage_stats.error_patterns:
            return alerts

        # Common error patterns
        error_frequency = {}
        for error in usage_stats.error_patterns:
            # Simple pattern matching - could be enhanced with NLP
            if "dependency" in error.lower() or "package" in error.lower():
                error_frequency["dependency_issues"] = (
                    error_frequency.get("dependency_issues", 0) + 1
                )
            elif "network" in error.lower() or "timeout" in error.lower():
                error_frequency["network_issues"] = (
                    error_frequency.get("network_issues", 0) + 1
                )
            elif "permission" in error.lower() or "access" in error.lower():
                error_frequency["permission_issues"] = (
                    error_frequency.get("permission_issues", 0) + 1
                )

        # Generate alerts for frequent error patterns
        total_errors = len(usage_stats.error_patterns)
        for error_type, count in error_frequency.items():
            if count / total_errors > 0.3:  # More than 30% of errors are this type
                alerts.append(
                    MaintenanceAlert(
                        template_name=template_name,
                        severity="medium",
                        category="reliability",
                        title=f'Frequent {error_type.replace("_", " ").title()}',
                        description=f'{count} out of {total_errors} recent errors are related to {error_type.replace("_", " ")}.',
                        recommended_action=self._get_error_fix_suggestion(error_type),
                        confidence=0.8,
                        created_at=datetime.now(),
                        data={
                            "error_type": error_type,
                            "frequency": count / total_errors,
                        },
                    )
                )

        return alerts

    def _check_security_issues(
        self, template_name: str, performance_metrics: PerformanceMetrics
    ) -> List[MaintenanceAlert]:
        """Check for security-related issues"""
        alerts = []

        # Low security score
        if performance_metrics.security_score < 0.6:
            alerts.append(
                MaintenanceAlert(
                    template_name=template_name,
                    severity="high",
                    category="security",
                    title="Low Security Score",
                    description=f"Security score is {performance_metrics.security_score:.1f}, indicating potential security risks.",
                    recommended_action="Review base image choices, update dependencies, and implement security best practices.",
                    confidence=0.7,
                    created_at=datetime.now(),
                    data={"security_score": performance_metrics.security_score},
                )
            )

        return alerts

    def _get_error_fix_suggestion(self, error_type: str) -> str:
        """Get fix suggestions for common error types"""
        suggestions = {
            "dependency_issues": "Update package versions, check for breaking changes, and consider using lock files.",
            "network_issues": "Add retry logic, use reliable package mirrors, and check firewall settings.",
            "permission_issues": "Review file permissions, ensure proper user configuration, and check volume mounts.",
        }
        return suggestions.get(
            error_type, "Review error logs and template configuration."
        )

    def _get_ai_maintenance_suggestions(
        self,
        template_name: str,
        usage_stats: UsageStats,
        performance_metrics: PerformanceMetrics,
    ) -> List[MaintenanceAlert]:
        """Get AI-powered maintenance suggestions"""
        if not self.ai_core.is_enabled("predictive_maintenance"):
            return []

        try:
            # Create prompt for AI analysis
            prompt = f"""
Analyze this container template for potential maintenance issues and optimization opportunities:

Template: {template_name}

Usage Statistics:
- Total uses: {usage_stats.total_uses}
- Success rate: {usage_stats.success_rate:.1%}
- Average build time: {usage_stats.avg_build_time:.1f} seconds
- Days since last use: {(datetime.now() - usage_stats.last_used).days}
- Common parameters: {json.dumps(usage_stats.common_parameters, indent=2)}

Performance Metrics:
- Average build time: {performance_metrics.avg_build_time_seconds:.1f} seconds
- Average image size: {performance_metrics.avg_image_size_mb:.1f} MB
- Success rate: {performance_metrics.success_rate:.1%}
- Resource efficiency: {performance_metrics.resource_efficiency:.2f}
- Security score: {performance_metrics.security_score:.2f}

Recent Errors:
{chr(10).join(usage_stats.error_patterns[-5:]) if usage_stats.error_patterns else 'None'}

Please identify potential issues and provide specific recommendations for:
1. Performance optimization
2. Security improvements
3. Reliability enhancements
4. Maintenance actions

Format your response as JSON with this structure:
{{
  "alerts": [
    {{
      "severity": "low|medium|high|critical",
      "category": "performance|security|reliability|maintenance",
      "title": "Brief title",
      "description": "Detailed description",
      "recommended_action": "Specific action to take",
      "confidence": 0.8
    }}
  ]
}}
"""

            messages = [
                {
                    "role": "system",
                    "content": "You are an expert DevOps engineer specializing in container optimization and maintenance.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            if response:
                # Parse AI response
                try:
                    start_idx = response.content.find("{")
                    end_idx = response.content.rfind("}") + 1

                    if start_idx >= 0 and end_idx > start_idx:
                        json_str = response.content[start_idx:end_idx]
                        data = json.loads(json_str)

                        alerts = []
                        for alert_data in data.get("alerts", []):
                            alert = MaintenanceAlert(
                                template_name=template_name,
                                severity=alert_data.get("severity", "medium"),
                                category=alert_data.get("category", "maintenance"),
                                title=alert_data.get("title", "AI Recommendation"),
                                description=alert_data.get("description", ""),
                                recommended_action=alert_data.get(
                                    "recommended_action", ""
                                ),
                                confidence=alert_data.get("confidence", 0.5),
                                created_at=datetime.now(),
                                data={"source": "ai_analysis"},
                            )
                            alerts.append(alert)

                        return alerts

                except json.JSONDecodeError as e:
                    logger.error(f"Failed to parse AI maintenance suggestions: {e}")

        except Exception as e:
            logger.error(f"AI maintenance analysis failed: {e}")

        return []

    def generate_maintenance_report(self, template_name: str = None) -> Dict[str, Any]:
        """Generate comprehensive maintenance report"""
        if template_name:
            alerts = self.analyze_template(template_name)
            templates = [template_name]
        else:
            alerts = self.analyze_all_templates()
            templates = list(set(alert.template_name for alert in alerts))

        # Categorize alerts
        alerts_by_severity = {}
        alerts_by_category = {}

        for alert in alerts:
            # By severity
            if alert.severity not in alerts_by_severity:
                alerts_by_severity[alert.severity] = []
            alerts_by_severity[alert.severity].append(alert)

            # By category
            if alert.category not in alerts_by_category:
                alerts_by_category[alert.category] = []
            alerts_by_category[alert.category].append(alert)

        # Generate summary
        report = {
            "generated_at": datetime.now().isoformat(),
            "scope": template_name if template_name else "all_templates",
            "templates_analyzed": len(templates),
            "total_alerts": len(alerts),
            "alerts_by_severity": {
                severity: len(alert_list)
                for severity, alert_list in alerts_by_severity.items()
            },
            "alerts_by_category": {
                category: len(alert_list)
                for category, alert_list in alerts_by_category.items()
            },
            "high_priority_actions": [
                {
                    "template": alert.template_name,
                    "title": alert.title,
                    "action": alert.recommended_action,
                    "confidence": alert.confidence,
                }
                for alert in alerts
                if alert.severity in ["high", "critical"]
            ],
            "detailed_alerts": [asdict(alert) for alert in alerts],
        }

        return report


def main():
    """CLI interface for predictive maintenance"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Template predictive maintenance system"
    )
    parser.add_argument(
        "command", choices=["analyze", "report", "stats"], help="Command to execute"
    )
    parser.add_argument("--template", help="Specific template to analyze")
    parser.add_argument(
        "--days", type=int, default=30, help="Number of days to analyze"
    )
    parser.add_argument("--output", help="Output file for results")
    parser.add_argument(
        "--format", choices=["json", "yaml"], default="json", help="Output format"
    )

    args = parser.parse_args()

    maintenance = PredictiveMaintenance()

    if args.command == "analyze":
        if args.template:
            alerts = maintenance.analyze_template(args.template)
        else:
            alerts = maintenance.analyze_all_templates()

        result = {"alerts": [asdict(alert) for alert in alerts]}

    elif args.command == "report":
        result = maintenance.generate_maintenance_report(args.template)

    elif args.command == "stats":
        if not args.template:
            print("Template name required for stats command")
            return

        analytics = maintenance.analytics
        usage_stats = analytics.get_usage_stats(args.template, args.days)
        performance_metrics = analytics.get_performance_metrics(
            args.template, args.days
        )

        result = {
            "usage_stats": asdict(usage_stats),
            "performance_metrics": asdict(performance_metrics),
        }

    # Output results
    if args.format == "json":
        output = json.dumps(result, indent=2, default=str)
    else:
        import yaml

        output = yaml.dump(result, default_flow_style=False)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Results saved to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()

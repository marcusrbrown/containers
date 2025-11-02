"""
Template Intelligence Engine

This module provides AI-powered template recommendations, analysis, and optimization.
Features:
- Intelligent template recommendations based on project analysis
- Smart parameter inference from existing project files
- Template similarity analysis and clustering
- Performance optimization suggestions
"""

import json
import logging
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml

from .ai_core import TemplateRecommendation, get_ai_core

logger = logging.getLogger(__name__)


@dataclass
class ProjectAnalysis:
    """Analysis results for a project directory"""

    project_type: str
    languages: List[str]
    frameworks: List[str]
    dependencies: Dict[str, List[str]]
    package_managers: List[str]
    architecture_hints: List[str]
    complexity_score: float
    recommended_templates: List[TemplateRecommendation]


@dataclass
class TemplateMetadata:
    """Enhanced template metadata for AI processing"""

    name: str
    path: str
    description: str
    category: str
    complexity: str
    tags: List[str]
    use_cases: List[str]
    tech_stack: List[str]
    performance_profile: str
    security_considerations: List[str]
    common_integrations: List[str]
    difficulty_indicators: Dict[str, int]
    usage_stats: Dict[str, Any]


class ProjectAnalyzer:
    """Analyzes project directories to extract meaningful metadata"""

    def __init__(self):
        self.ai_core = get_ai_core()
        self.file_analyzers = {
            "package.json": self._analyze_package_json,
            "requirements.txt": self._analyze_requirements_txt,
            "pyproject.toml": self._analyze_pyproject_toml,
            "go.mod": self._analyze_go_mod,
            "Cargo.toml": self._analyze_cargo_toml,
            "composer.json": self._analyze_composer_json,
            "Gemfile": self._analyze_gemfile,
            "pom.xml": self._analyze_pom_xml,
            "build.gradle": self._analyze_gradle,
            "Dockerfile": self._analyze_dockerfile,
            "docker-compose.yml": self._analyze_docker_compose,
        }

    def analyze_project(self, project_path: str) -> ProjectAnalysis:
        """Analyze a project directory and return comprehensive analysis"""
        project_path_obj = Path(project_path)

        if not project_path_obj.exists():
            raise ValueError(f"Project path does not exist: {project_path}")

        # Scan for known files
        found_files = {}
        for filename, analyzer in self.file_analyzers.items():
            file_path = project_path_obj / filename
            if file_path.exists():
                try:
                    found_files[filename] = analyzer(file_path)
                except Exception as e:
                    logger.warning(f"Failed to analyze {filename}: {e}")

        # Scan directory structure
        structure_info = self._analyze_directory_structure(project_path_obj)

        # Combine analysis results
        analysis = self._combine_analysis_results(found_files, structure_info)

        # Get AI-powered recommendations
        if self.ai_core.is_enabled("template_recommendation"):
            analysis.recommended_templates = self._get_ai_recommendations(analysis)

        return analysis

    def _analyze_package_json(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Node.js package.json file"""
        with open(file_path, "r") as f:
            data = json.load(f)

        dependencies = list(data.get("dependencies", {}).keys())
        dev_dependencies = list(data.get("devDependencies", {}).keys())

        # Detect frameworks
        frameworks = []
        if "express" in dependencies:
            frameworks.append("express")
        if "react" in dependencies:
            frameworks.append("react")
        if "vue" in dependencies:
            frameworks.append("vue")
        if "angular" in dependencies:
            frameworks.append("angular")
        if "next" in dependencies:
            frameworks.append("nextjs")
        if "nestjs" in dependencies or "@nestjs/core" in dependencies:
            frameworks.append("nestjs")

        # Detect build tools
        build_tools = []
        if "webpack" in dev_dependencies:
            build_tools.append("webpack")
        if "vite" in dev_dependencies:
            build_tools.append("vite")
        if "rollup" in dev_dependencies:
            build_tools.append("rollup")

        return {
            "language": "javascript",
            "package_manager": "npm",
            "dependencies": dependencies,
            "dev_dependencies": dev_dependencies,
            "frameworks": frameworks,
            "build_tools": build_tools,
            "scripts": list(data.get("scripts", {}).keys()),
            "node_version": data.get("engines", {}).get("node"),
        }

    def _analyze_requirements_txt(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Python requirements.txt file"""
        with open(file_path, "r") as f:
            lines = f.readlines()

        dependencies = []
        frameworks = []

        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                # Extract package name (before version specifier)
                package = (
                    line.split("==")[0]
                    .split(">=")[0]
                    .split("<=")[0]
                    .split("~=")[0]
                    .strip()
                )
                dependencies.append(package)

                # Detect frameworks
                if package.lower() in [
                    "django",
                    "flask",
                    "fastapi",
                    "tornado",
                    "pyramid",
                    "bottle",
                ]:
                    frameworks.append(package.lower())
                elif package.lower() in [
                    "tensorflow",
                    "pytorch",
                    "scikit-learn",
                    "pandas",
                    "numpy",
                ]:
                    frameworks.append("data-science")

        return {
            "language": "python",
            "package_manager": "pip",
            "dependencies": dependencies,
            "frameworks": frameworks,
        }

    def _analyze_pyproject_toml(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Python pyproject.toml file"""
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        project_data = data.get("project", {})
        dependencies = project_data.get("dependencies", [])

        # Extract package names
        package_names = []
        frameworks = []

        for dep in dependencies:
            if isinstance(dep, str):
                package = dep.split(">=")[0].split("==")[0].split("~=")[0].strip()
                package_names.append(package)

                # Detect frameworks
                if package.lower() in ["django", "flask", "fastapi", "tornado"]:
                    frameworks.append(package.lower())

        build_system = data.get("build-system", {})

        return {
            "language": "python",
            "package_manager": "poetry" if "poetry" in str(build_system) else "pip",
            "dependencies": package_names,
            "frameworks": frameworks,
            "python_version": project_data.get("requires-python"),
            "build_backend": build_system.get("build-backend"),
        }

    def _analyze_go_mod(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Go go.mod file"""
        with open(file_path, "r") as f:
            content = f.read()

        lines = content.split("\\n")
        module_name = None
        go_version = None
        dependencies = []
        frameworks = []

        for line in lines:
            line = line.strip()
            if line.startswith("module "):
                module_name = line.split("module ")[1]
            elif line.startswith("go "):
                go_version = line.split("go ")[1]
            elif (
                line
                and not line.startswith("//")
                and "/" in line
                and not line.startswith("replace")
            ):
                # Extract dependency
                parts = line.split()
                if len(parts) >= 2:
                    dep = parts[0]
                    dependencies.append(dep)

                    # Detect frameworks
                    if "gin-gonic/gin" in dep:
                        frameworks.append("gin")
                    elif "gorilla/mux" in dep:
                        frameworks.append("gorilla")
                    elif "echo" in dep:
                        frameworks.append("echo")

        return {
            "language": "go",
            "package_manager": "go",
            "module_name": module_name,
            "go_version": go_version,
            "dependencies": dependencies,
            "frameworks": frameworks,
        }

    def _analyze_cargo_toml(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Rust Cargo.toml file"""
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        package_info = data.get("package", {})
        dependencies = list(data.get("dependencies", {}).keys())
        dev_dependencies = list(data.get("dev-dependencies", {}).keys())

        frameworks = []
        # Detect Rust frameworks
        if "actix-web" in dependencies:
            frameworks.append("actix-web")
        if "rocket" in dependencies:
            frameworks.append("rocket")
        if "warp" in dependencies:
            frameworks.append("warp")
        if "axum" in dependencies:
            frameworks.append("axum")

        return {
            "language": "rust",
            "package_manager": "cargo",
            "name": package_info.get("name"),
            "version": package_info.get("version"),
            "rust_version": package_info.get("rust-version"),
            "dependencies": dependencies,
            "dev_dependencies": dev_dependencies,
            "frameworks": frameworks,
        }

    def _analyze_composer_json(self, file_path: Path) -> Dict[str, Any]:
        """Analyze PHP composer.json file"""
        with open(file_path, "r") as f:
            data = json.load(f)

        dependencies = list(data.get("require", {}).keys())
        dev_dependencies = list(data.get("require-dev", {}).keys())

        frameworks = []
        if "laravel/framework" in dependencies:
            frameworks.append("laravel")
        if "symfony/symfony" in dependencies:
            frameworks.append("symfony")
        if "slim/slim" in dependencies:
            frameworks.append("slim")

        return {
            "language": "php",
            "package_manager": "composer",
            "dependencies": dependencies,
            "dev_dependencies": dev_dependencies,
            "frameworks": frameworks,
            "php_version": data.get("require", {}).get("php"),
        }

    def _analyze_gemfile(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Ruby Gemfile"""
        with open(file_path, "r") as f:
            content = f.read()

        dependencies = []
        frameworks = []
        ruby_version = None

        for line in content.split("\\n"):
            line = line.strip()
            if line.startswith("gem "):
                # Extract gem name
                parts = line.split("'")
                if len(parts) >= 2:
                    gem_name = parts[1]
                    dependencies.append(gem_name)

                    if gem_name == "rails":
                        frameworks.append("rails")
                    elif gem_name == "sinatra":
                        frameworks.append("sinatra")
            elif line.startswith("ruby "):
                ruby_version = line.split("'")[1] if "'" in line else None

        return {
            "language": "ruby",
            "package_manager": "bundler",
            "ruby_version": ruby_version,
            "dependencies": dependencies,
            "frameworks": frameworks,
        }

    def _analyze_pom_xml(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Java pom.xml file"""
        # Basic XML parsing - in a real implementation, use xml.etree.ElementTree
        with open(file_path, "r") as f:
            content = f.read()

        frameworks = []
        if "spring-boot" in content:
            frameworks.append("spring-boot")
        if "spring-web" in content:
            frameworks.append("spring")
        if "quarkus" in content:
            frameworks.append("quarkus")

        return {
            "language": "java",
            "package_manager": "maven",
            "frameworks": frameworks,
        }

    def _analyze_gradle(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Gradle build file"""
        with open(file_path, "r") as f:
            content = f.read()

        frameworks = []
        if "spring-boot" in content:
            frameworks.append("spring-boot")
        if "kotlin" in content:
            frameworks.append("kotlin")

        return {
            "language": "java" if "kotlin" not in content else "kotlin",
            "package_manager": "gradle",
            "frameworks": frameworks,
        }

    def _analyze_dockerfile(self, file_path: Path) -> Dict[str, Any]:
        """Analyze existing Dockerfile"""
        with open(file_path, "r") as f:
            content = f.read()

        base_images = []
        languages = []

        for line in content.split("\\n"):
            line = line.strip()
            if line.startswith("FROM "):
                base_image = line.split("FROM ")[1].split()[0]
                base_images.append(base_image)

                # Infer language from base image
                if "node" in base_image:
                    languages.append("javascript")
                elif "python" in base_image:
                    languages.append("python")
                elif "golang" in base_image or "go:" in base_image:
                    languages.append("go")
                elif "openjdk" in base_image or "java" in base_image:
                    languages.append("java")

        return {
            "containerized": True,
            "base_images": base_images,
            "languages": languages,
        }

    def _analyze_docker_compose(self, file_path: Path) -> Dict[str, Any]:
        """Analyze Docker Compose file"""
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        services = list(data.get("services", {}).keys())
        databases = []

        for service_name, service_config in data.get("services", {}).items():
            image = service_config.get("image", "")
            if "postgres" in image:
                databases.append("postgresql")
            elif "mysql" in image:
                databases.append("mysql")
            elif "redis" in image:
                databases.append("redis")
            elif "mongo" in image:
                databases.append("mongodb")

        return {
            "multi_service": True,
            "services": services,
            "databases": databases,
        }

    def _analyze_directory_structure(self, project_path: Path) -> Dict[str, Any]:
        """Analyze project directory structure for additional hints"""
        structure_hints = []

        # Check for common directory patterns
        directories = [d.name for d in project_path.iterdir() if d.is_dir()]

        if "src" in directories:
            structure_hints.append("structured-project")
        if "lib" in directories:
            structure_hints.append("library")
        if "bin" in directories:
            structure_hints.append("executable")
        if "docs" in directories:
            structure_hints.append("documented")
        if "tests" in directories or "test" in directories:
            structure_hints.append("tested")
        if ".git" in directories:
            structure_hints.append("git-repository")
        if "migrations" in directories:
            structure_hints.append("database-app")
        if "static" in directories or "public" in directories:
            structure_hints.append("web-app")
        if "templates" in directories:
            structure_hints.append("templated-app")

        # Check for common file patterns
        files = [f.name for f in project_path.iterdir() if f.is_file()]

        if "README.md" in files:
            structure_hints.append("documented")
        if "LICENSE" in files or "LICENSE.txt" in files:
            structure_hints.append("open-source")
        if ".env" in files or ".env.example" in files:
            structure_hints.append("configurable")

        return {
            "structure_hints": structure_hints,
            "directories": directories,
            "files": files,
        }

    def _combine_analysis_results(
        self, found_files: Dict[str, Any], structure_info: Dict[str, Any]
    ) -> ProjectAnalysis:
        """Combine all analysis results into a comprehensive project analysis"""

        # Determine primary language and frameworks
        languages = set()
        frameworks = set()
        dependencies = {}
        package_managers = set()

        for filename, analysis in found_files.items():
            if "language" in analysis:
                languages.add(analysis["language"])
            if "frameworks" in analysis:
                frameworks.update(analysis["frameworks"])
            if "dependencies" in analysis:
                dependencies[filename] = analysis["dependencies"]
            if "package_manager" in analysis:
                package_managers.add(analysis["package_manager"])

        # Determine project type
        project_type = self._determine_project_type(
            list(languages), list(frameworks), structure_info
        )

        # Calculate complexity score
        complexity_score = self._calculate_complexity_score(found_files, structure_info)

        # Architecture hints
        architecture_hints = structure_info.get("structure_hints", [])
        if len(languages) > 1:
            architecture_hints.append("polyglot")
        if any("database" in str(deps) for deps in dependencies.values()):
            architecture_hints.append("database-dependent")

        return ProjectAnalysis(
            project_type=project_type,
            languages=list(languages),
            frameworks=list(frameworks),
            dependencies=dependencies,
            package_managers=list(package_managers),
            architecture_hints=architecture_hints,
            complexity_score=complexity_score,
            recommended_templates=[],  # Will be filled by AI recommendations
        )

    def _determine_project_type(
        self,
        languages: List[str],
        frameworks: List[str],
        structure_info: Dict[str, Any],
    ) -> str:
        """Determine the primary project type"""

        # Web application frameworks
        web_frameworks = [
            "express",
            "react",
            "vue",
            "angular",
            "nextjs",
            "django",
            "flask",
            "fastapi",
            "rails",
            "spring-boot",
        ]
        if any(fw in frameworks for fw in web_frameworks):
            return "web-application"

        # API frameworks
        api_frameworks = ["express", "fastapi", "gin", "actix-web", "spring-boot"]
        if any(fw in frameworks for fw in api_frameworks):
            return "api-service"

        # Data science
        data_frameworks = ["data-science", "tensorflow", "pytorch"]
        if any(fw in frameworks for fw in data_frameworks):
            return "data-science"

        # Microservice indicators
        if "docker-compose.yml" in structure_info.get("files", []):
            return "microservice"

        # CLI application
        if "bin" in structure_info.get("directories", []):
            return "cli-application"

        # Library
        if "lib" in structure_info.get("directories", []):
            return "library"

        # Default based on primary language
        if "javascript" in languages:
            return "nodejs-application"
        elif "python" in languages:
            return "python-application"
        elif "go" in languages:
            return "go-application"
        elif "rust" in languages:
            return "rust-application"
        elif "java" in languages:
            return "java-application"

        return "generic-application"

    def _calculate_complexity_score(
        self, found_files: Dict[str, Any], structure_info: Dict[str, Any]
    ) -> float:
        """Calculate project complexity score (0.0 to 1.0)"""
        score = 0.0

        # Base complexity from number of languages
        languages = set()
        for analysis in found_files.values():
            if "language" in analysis:
                languages.add(analysis["language"])

        score += len(languages) * 0.1

        # Complexity from dependencies
        total_deps = 0
        for analysis in found_files.values():
            if "dependencies" in analysis:
                total_deps += len(analysis["dependencies"])

        score += min(total_deps / 100, 0.3)  # Cap at 0.3

        # Complexity from frameworks
        frameworks = set()
        for analysis in found_files.values():
            if "frameworks" in analysis:
                frameworks.update(analysis["frameworks"])

        score += len(frameworks) * 0.05

        # Complexity from structure
        structure_hints = structure_info.get("structure_hints", [])
        if "multi-service" in structure_hints:
            score += 0.2
        if "database-dependent" in structure_hints:
            score += 0.1
        if "tested" in structure_hints:
            score += 0.1  # More complex but well-structured

        return min(score, 1.0)

    def _get_ai_recommendations(
        self, analysis: ProjectAnalysis
    ) -> List[TemplateRecommendation]:
        """Get AI-powered template recommendations"""
        if not self.ai_core.is_enabled("template_recommendation"):
            return []

        try:
            # Load available templates
            templates = self._load_available_templates()

            # Create prompt for AI
            prompt = self._create_recommendation_prompt(analysis, templates)

            messages = [
                {
                    "role": "system",
                    "content": "You are an expert DevOps engineer specializing in container templates and project architecture.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            if response:
                return self._parse_ai_recommendations(response.content)

        except Exception as e:
            logger.error(f"Failed to get AI recommendations: {e}")

        return []

    def _load_available_templates(self) -> List[TemplateMetadata]:
        """Load available template metadata"""
        templates = []
        templates_dir = Path(__file__).parent.parent / "templates"

        if not templates_dir.exists():
            return templates

        # Recursively find template.yaml files
        for template_file in templates_dir.rglob("template.yaml"):
            try:
                with open(template_file, "r") as f:
                    data = yaml.safe_load(f)

                template = TemplateMetadata(
                    name=data.get("name", template_file.parent.name),
                    path=str(template_file.parent),
                    description=data.get("description", ""),
                    category=data.get("category", "general"),
                    complexity=data.get("complexity", "medium"),
                    tags=data.get("ai_metadata", {}).get("tags", []),
                    use_cases=data.get("ai_metadata", {}).get("use_cases", []),
                    tech_stack=data.get("ai_metadata", {}).get("tech_stack", []),
                    performance_profile=data.get("ai_metadata", {}).get(
                        "performance_profile", "medium"
                    ),
                    security_considerations=data.get("ai_metadata", {}).get(
                        "security_considerations", []
                    ),
                    common_integrations=data.get("ai_metadata", {}).get(
                        "common_integrations", []
                    ),
                    difficulty_indicators=data.get("ai_metadata", {}).get(
                        "difficulty_indicators", {}
                    ),
                    usage_stats={},  # Would be loaded from analytics database
                )
                templates.append(template)

            except Exception as e:
                logger.warning(
                    f"Failed to load template metadata from {template_file}: {e}"
                )

        return templates

    def _create_recommendation_prompt(
        self, analysis: ProjectAnalysis, templates: List[TemplateMetadata]
    ) -> str:
        """Create AI prompt for template recommendations"""

        template_descriptions = []
        for template in templates:
            template_descriptions.append(
                f"""
Template: {template.name}
Category: {template.category}
Description: {template.description}
Tech Stack: {', '.join(template.tech_stack)}
Use Cases: {', '.join(template.use_cases)}
Complexity: {template.complexity}
Tags: {', '.join(template.tags)}
"""
            )

        prompt = f"""
Analyze this project and recommend the best container templates:

Project Analysis:
- Type: {analysis.project_type}
- Languages: {', '.join(analysis.languages)}
- Frameworks: {', '.join(analysis.frameworks)}
- Package Managers: {', '.join(analysis.package_managers)}
- Architecture Hints: {', '.join(analysis.architecture_hints)}
- Complexity Score: {analysis.complexity_score:.2f}

Available Templates:
{''.join(template_descriptions)}

Please recommend the top 3-5 most suitable templates with:
1. Template name
2. Confidence score (0.0-1.0)
3. Reasoning for recommendation
4. Suggested parameter values
5. Alternative templates to consider

Format your response as JSON:
{{
  "recommendations": [
    {{
      "template_name": "template-name",
      "confidence": 0.95,
      "reasoning": "This template is perfect because...",
      "parameters": {{"param1": "value1", "param2": "value2"}},
      "alternatives": ["alt-template-1", "alt-template-2"]
    }}
  ]
}}
"""
        return prompt

    def _parse_ai_recommendations(
        self, ai_response: str
    ) -> List[TemplateRecommendation]:
        """Parse AI response into TemplateRecommendation objects"""
        try:
            # Try to extract JSON from the response
            start_idx = ai_response.find("{")
            end_idx = ai_response.rfind("}") + 1

            if start_idx >= 0 and end_idx > start_idx:
                json_str = ai_response[start_idx:end_idx]
                data = json.loads(json_str)

                recommendations = []
                for rec in data.get("recommendations", []):
                    recommendation = TemplateRecommendation(
                        template_name=rec.get("template_name", ""),
                        confidence=rec.get("confidence", 0.0),
                        reasoning=rec.get("reasoning", ""),
                        parameters=rec.get("parameters", {}),
                        alternatives=rec.get("alternatives", []),
                    )
                    recommendations.append(recommendation)

                return recommendations

        except Exception as e:
            logger.error(f"Failed to parse AI recommendations: {e}")

        return []


class TemplateIntelligence:
    """Main interface for template intelligence features"""

    def __init__(self):
        self.project_analyzer = ProjectAnalyzer()
        self.ai_core = get_ai_core()

    def analyze_project(self, project_path: str) -> ProjectAnalysis:
        """Analyze a project and return comprehensive analysis"""
        return self.project_analyzer.analyze_project(project_path)

    def recommend_templates(self, project_path: str) -> List[TemplateRecommendation]:
        """Get template recommendations for a project"""
        analysis = self.analyze_project(project_path)
        return analysis.recommended_templates

    def infer_parameters(self, project_path: str, template_name: str) -> Dict[str, Any]:
        """Infer template parameters from project analysis"""
        analysis = self.analyze_project(project_path)

        # Basic parameter inference
        parameters = {}

        # Common parameters
        if analysis.languages:
            parameters["primary_language"] = analysis.languages[0]

        if analysis.package_managers:
            parameters["package_manager"] = analysis.package_managers[0]

        # Framework-specific parameters
        if "express" in analysis.frameworks:
            parameters["framework"] = "express"
            parameters["app_port"] = 3000
        elif "fastapi" in analysis.frameworks:
            parameters["framework"] = "fastapi"
            parameters["app_port"] = 8000
        elif "flask" in analysis.frameworks:
            parameters["framework"] = "flask"
            parameters["app_port"] = 5000

        # Complexity-based parameters
        if analysis.complexity_score > 0.7:
            parameters["optimization_level"] = "production"
            parameters["enable_monitoring"] = True
        else:
            parameters["optimization_level"] = "development"
            parameters["enable_monitoring"] = False

        # Architecture-based parameters
        if "database-dependent" in analysis.architecture_hints:
            parameters["include_database"] = True

        if "multi-service" in analysis.architecture_hints:
            parameters["architecture"] = "microservice"
        else:
            parameters["architecture"] = "monolith"

        # Use AI for more sophisticated parameter inference
        if self.ai_core.is_enabled("parameter_inference"):
            ai_parameters = self._get_ai_parameter_suggestions(
                analysis, template_name, parameters
            )
            parameters.update(ai_parameters)

        return parameters

    def _get_ai_parameter_suggestions(
        self,
        analysis: ProjectAnalysis,
        template_name: str,
        basic_parameters: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Use AI to suggest additional parameters"""
        try:
            prompt = f"""
Based on this project analysis, suggest optimal parameters for the '{template_name}' template:

Project Analysis:
- Type: {analysis.project_type}
- Languages: {', '.join(analysis.languages)}
- Frameworks: {', '.join(analysis.frameworks)}
- Complexity: {analysis.complexity_score:.2f}
- Architecture: {', '.join(analysis.architecture_hints)}

Current Parameters: {json.dumps(basic_parameters, indent=2)}

Please suggest additional parameters that would optimize this template for this specific project.
Focus on:
- Performance optimization settings
- Security configurations
- Development vs production settings
- Resource allocation
- Monitoring and logging

Return only a JSON object with parameter suggestions:
{{
  "suggested_parameters": {{
    "parameter_name": "value",
    "explanation": "why this value is recommended"
  }}
}}
"""

            messages = [
                {
                    "role": "system",
                    "content": "You are an expert in container optimization and template configuration.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            if response:
                # Parse AI suggestions
                start_idx = response.content.find("{")
                end_idx = response.content.rfind("}") + 1

                if start_idx >= 0 and end_idx > start_idx:
                    json_str = response.content[start_idx:end_idx]
                    data = json.loads(json_str)
                    return data.get("suggested_parameters", {})

        except Exception as e:
            logger.error(f"Failed to get AI parameter suggestions: {e}")

        return {}


# CLI interface functions
def analyze_project():
    """CLI function for project analysis"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Analyze project for template recommendations"
    )
    parser.add_argument("project_path", help="Path to project directory")
    parser.add_argument("--output", "-o", help="Output file for analysis results")
    parser.add_argument(
        "--format", choices=["json", "yaml"], default="json", help="Output format"
    )

    args = parser.parse_args()

    intelligence = TemplateIntelligence()
    analysis = intelligence.analyze_project(args.project_path)

    # Convert to dict for serialization
    result = asdict(analysis)

    if args.format == "json":
        output = json.dumps(result, indent=2, default=str)
    else:
        output = yaml.dump(result, default_flow_style=False)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Analysis saved to {args.output}")
    else:
        print(output)


def recommend_templates():
    """CLI function for template recommendations"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Get template recommendations for project"
    )
    parser.add_argument("project_path", help="Path to project directory")
    parser.add_argument("--output", "-o", help="Output file for recommendations")
    parser.add_argument(
        "--top", "-n", type=int, default=5, help="Number of recommendations"
    )

    args = parser.parse_args()

    intelligence = TemplateIntelligence()
    recommendations = intelligence.recommend_templates(args.project_path)

    # Limit to top N recommendations
    recommendations = recommendations[: args.top]

    # Convert to dict for serialization
    result = {
        "project_path": args.project_path,
        "recommendations": [asdict(rec) for rec in recommendations],
    }

    output = json.dumps(result, indent=2, default=str)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Recommendations saved to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "analyze":
        sys.argv.pop(1)  # Remove 'analyze' from args
        analyze_project()
    elif len(sys.argv) > 1 and sys.argv[1] == "recommend":
        sys.argv.pop(1)  # Remove 'recommend' from args
        recommend_templates()
    else:
        print("Usage: python template_intelligence.py {analyze|recommend} [options]")

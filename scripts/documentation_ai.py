"""
AI-Powered Documentation Generator

This module automatically generates comprehensive documentation for templates:
- README files with usage examples
- API documentation
- Troubleshooting guides
- Best practices documentation
- Architecture diagrams (text-based)
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from .ai_core import get_ai_core
from .template_intelligence import TemplateIntelligence

logger = logging.getLogger(__name__)


class DocumentationGenerator:
    """AI-powered documentation generation"""

    def __init__(self):
        self.ai_core = get_ai_core()
        self.template_intelligence = TemplateIntelligence()

    def generate_readme(
        self, template_path: str, template_config: Dict[str, Any]
    ) -> str:
        """Generate comprehensive README for template"""

        if not self.ai_core.is_enabled("documentation_generation"):
            return self._generate_basic_readme(template_config)

        try:
            prompt = self._create_readme_prompt(template_config)

            messages = [
                {
                    "role": "system",
                    "content": "You are a technical documentation expert specializing in container templates and DevOps.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            if response:
                return response.content
            else:
                return self._generate_basic_readme(template_config)

        except Exception as e:
            logger.error(f"AI documentation generation failed: {e}")
            return self._generate_basic_readme(template_config)

    def generate_api_docs(self, template_config: Dict[str, Any]) -> str:
        """Generate API documentation for web service templates"""

        if not self._is_api_template(template_config):
            return ""

        prompt = f"""
Generate comprehensive API documentation for this container template:

Template: {template_config.get('name', 'Unknown')}
Description: {template_config.get('description', '')}
Tech Stack: {', '.join(template_config.get('ai_metadata', {}).get('tech_stack', []))}

Please include:
1. API Overview
2. Authentication (if applicable)
3. Endpoints with examples
4. Request/Response formats
5. Error codes and handling
6. Rate limiting information
7. SDKs and client libraries

Format as Markdown with proper headers and code examples.
"""

        try:
            messages = [
                {
                    "role": "system",
                    "content": "You are an API documentation specialist. Create clear, comprehensive API docs.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            return response.content if response else ""

        except Exception as e:
            logger.error(f"API documentation generation failed: {e}")
            return ""

    def generate_troubleshooting_guide(
        self,
        template_config: Dict[str, Any],
        common_issues: Optional[List[str]] = None,
    ) -> str:
        """Generate troubleshooting guide"""

        prompt = f"""
Create a comprehensive troubleshooting guide for this container template:

Template: {template_config.get('name', 'Unknown')}
Description: {template_config.get('description', '')}
Tech Stack: {', '.join(template_config.get('ai_metadata', {}).get('tech_stack', []))}
Security Considerations: {', '.join(template_config.get('ai_metadata', {}).get('security_considerations', []))}

Common Issues (if known): {json.dumps(common_issues) if common_issues else 'None provided'}

Please include:
1. Common build issues and solutions
2. Runtime problems and debugging steps
3. Performance troubleshooting
4. Security-related issues
5. Network and connectivity problems
6. Resource constraints and solutions
7. Logging and monitoring setup
8. Emergency procedures

Format as Markdown with clear sections and actionable solutions.
"""

        try:
            messages = [
                {
                    "role": "system",
                    "content": "You are a DevOps troubleshooting expert. Provide practical, actionable solutions.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            return (
                response.content
                if response
                else self._generate_basic_troubleshooting(template_config)
            )

        except Exception as e:
            logger.error(f"Troubleshooting guide generation failed: {e}")
            return self._generate_basic_troubleshooting(template_config)

    def generate_examples(self, template_config: Dict[str, Any]) -> str:
        """Generate usage examples and code samples"""

        prompt = f"""
Generate practical usage examples for this container template:

Template: {template_config.get('name', 'Unknown')}
Description: {template_config.get('description', '')}
Tech Stack: {', '.join(template_config.get('ai_metadata', {}).get('tech_stack', []))}
Use Cases: {', '.join(template_config.get('ai_metadata', {}).get('use_cases', []))}

Please include:
1. Basic usage example
2. Production deployment example
3. Development setup
4. Integration with CI/CD
5. Environment configuration examples
6. Docker Compose examples
7. Kubernetes deployment examples
8. Monitoring and logging setup

Provide complete, working examples with explanations.
Format as Markdown with proper code blocks.
"""

        try:
            messages = [
                {
                    "role": "system",
                    "content": "You are a DevOps engineer creating practical examples and tutorials.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            return response.content if response else ""

        except Exception as e:
            logger.error(f"Examples generation failed: {e}")
            return ""

    def _create_readme_prompt(self, template_config: Dict[str, Any]) -> str:
        """Create prompt for README generation"""

        ai_metadata = template_config.get("ai_metadata", {})

        return f"""
Generate a comprehensive README.md file for this container template:

Template Information:
- Name: {template_config.get('name', 'Unknown')}
- Description: {template_config.get('description', '')}
- Category: {template_config.get('category', '')}
- Version: {template_config.get('version', '1.0.0')}

AI Metadata:
- Tech Stack: {', '.join(ai_metadata.get('tech_stack', []))}
- Use Cases: {', '.join(ai_metadata.get('use_cases', []))}
- Performance Profile: {ai_metadata.get('performance_profile', 'N/A')}
- Security Considerations: {', '.join(ai_metadata.get('security_considerations', []))}
- Best Practices: {chr(10).join(f'- {practice}' for practice in ai_metadata.get('best_practices', []))}
- Resource Requirements: Memory: {ai_metadata.get('resource_requirements', {}).get('memory_mb', 'N/A')}MB, CPU: {ai_metadata.get('resource_requirements', {}).get('cpu_cores', 'N/A')} cores

Parameters: {json.dumps(template_config.get('parameters', {}), indent=2)}

Please create a professional README.md that includes:
1. Project title and description
2. Table of contents
3. Quick start guide
4. Requirements and prerequisites
5. Installation and setup instructions
6. Configuration options (parameters)
7. Usage examples
8. Best practices and recommendations
9. Security considerations
10. Performance optimization tips
11. Troubleshooting section
12. Contributing guidelines
13. License information

Use proper Markdown formatting with badges, code blocks, and clear sections.
Make it beginner-friendly but comprehensive for advanced users.
"""

    def _generate_basic_readme(self, template_config: Dict[str, Any]) -> str:
        """Generate basic README when AI is not available"""

        name = template_config.get("name", "Container Template")
        description = template_config.get(
            "description", "A container template for deployment"
        )

        return f"""# {name}

{description}

## Quick Start

```bash
# Build the container
docker build -t {name.lower()} .

# Run the container
docker run -p 8080:8080 {name.lower()}
```

## Configuration

This template supports the following parameters:

{self._format_parameters_table(template_config.get('parameters', {}))}

## Usage

1. Clone this template
2. Customize the parameters as needed
3. Build and run the container

## Support

For issues and questions, please refer to the documentation or create an issue.

## License

MIT License - see LICENSE file for details.
"""

    def _generate_basic_troubleshooting(self, template_config: Dict[str, Any]) -> str:
        """Generate basic troubleshooting guide"""

        return f"""# Troubleshooting Guide

## Common Issues

### Build Failures
- Check Docker daemon is running
- Verify all dependencies are available
- Review build logs for specific errors

### Runtime Problems
- Check container logs: `docker logs <container-name>`
- Verify port mappings
- Check environment variables

### Performance Issues
- Monitor resource usage: `docker stats`
- Review application logs
- Check for memory leaks

### Network Connectivity
- Verify port bindings
- Check firewall settings
- Test network connectivity

## Getting Help

1. Check the logs first
2. Review the documentation
3. Search for similar issues
4. Create a detailed issue report

## Emergency Procedures

1. Stop the container: `docker stop <container-name>`
2. Check system resources
3. Review recent changes
4. Restart with verbose logging
"""

    def _format_parameters_table(self, parameters: Dict[str, Any]) -> str:
        """Format parameters as a markdown table"""
        if not parameters:
            return "No configurable parameters."

        table = "| Parameter | Type | Default | Description |\\n"
        table += "|-----------|------|---------|-------------|\\n"

        for param_name, param_config in parameters.items():
            param_type = param_config.get("type", "string")
            default = param_config.get("default", "N/A")
            description = param_config.get("description", "No description")
            table += f"| {param_name} | {param_type} | {default} | {description} |\\n"

        return table

    def _is_api_template(self, template_config: Dict[str, Any]) -> bool:
        """Check if template is for an API service"""
        ai_metadata = template_config.get("ai_metadata", {})
        use_cases = ai_metadata.get("use_cases", [])
        tech_stack = ai_metadata.get("tech_stack", [])

        api_indicators = ["api", "rest", "graphql", "microservice", "web-service"]

        return any(
            indicator in " ".join(use_cases + tech_stack).lower()
            for indicator in api_indicators
        )


class TestGenerator:
    """AI-powered test case generation"""

    def __init__(self):
        self.ai_core = get_ai_core()

    def generate_container_tests(self, template_config: Dict[str, Any]) -> str:
        """Generate container-specific tests"""

        prompt = f"""
Generate comprehensive test cases for this container template:

Template: {template_config.get('name', 'Unknown')}
Description: {template_config.get('description', '')}
Tech Stack: {', '.join(template_config.get('ai_metadata', {}).get('tech_stack', []))}

Please generate tests for:
1. Container build tests
2. Container startup tests
3. Health check tests
4. Port accessibility tests
5. Environment variable tests
6. Volume mount tests
7. Security tests
8. Performance tests

Use appropriate testing frameworks and provide complete, runnable test code.
Include both positive and negative test cases.
Format as a complete test file with proper imports and setup.
"""

        try:
            messages = [
                {
                    "role": "system",
                    "content": "You are a test automation expert specializing in container testing.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            return (
                response.content
                if response
                else self._generate_basic_tests(template_config)
            )

        except Exception as e:
            logger.error(f"Test generation failed: {e}")
            return self._generate_basic_tests(template_config)

    def generate_application_tests(self, template_config: Dict[str, Any]) -> str:
        """Generate application-specific tests"""

        ai_metadata = template_config.get("ai_metadata", {})
        tech_stack = ai_metadata.get("tech_stack", [])

        # Determine testing framework based on tech stack
        framework = self._determine_test_framework(tech_stack)

        prompt = f"""
Generate comprehensive application tests for this template using {framework}:

Template: {template_config.get('name', 'Unknown')}
Tech Stack: {', '.join(tech_stack)}
Use Cases: {', '.join(ai_metadata.get('use_cases', []))}

Generate tests for:
1. Unit tests for core functionality
2. Integration tests
3. API endpoint tests (if applicable)
4. Database integration tests (if applicable)
5. Authentication tests (if applicable)
6. Error handling tests
7. Performance tests
8. Load tests

Provide complete, production-ready test code with:
- Proper test structure and organization
- Setup and teardown procedures
- Mock objects where appropriate
- Comprehensive assertions
- Error case coverage

Format as complete test files with proper imports and configuration.
"""

        try:
            messages = [
                {
                    "role": "system",
                    "content": f"You are a software testing expert specializing in {framework} and test automation.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            return response.content if response else ""

        except Exception as e:
            logger.error(f"Application test generation failed: {e}")
            return ""

    def generate_ci_tests(self, template_config: Dict[str, Any]) -> str:
        """Generate CI/CD pipeline tests"""

        prompt = f"""
Generate CI/CD pipeline configuration with comprehensive testing for this template:

Template: {template_config.get('name', 'Unknown')}
Tech Stack: {', '.join(template_config.get('ai_metadata', {}).get('tech_stack', []))}

Include:
1. Build pipeline with testing
2. Docker image building and testing
3. Security scanning
4. Performance testing
5. Integration testing
6. Deployment testing
7. Rollback procedures

Provide configurations for popular CI/CD platforms:
- GitHub Actions
- GitLab CI
- Jenkins

Include proper error handling, notifications, and artifact management.
"""

        try:
            messages = [
                {
                    "role": "system",
                    "content": "You are a DevOps engineer specializing in CI/CD pipeline design and testing.",
                },
                {"role": "user", "content": prompt},
            ]

            response = self.ai_core.chat_completion(messages)
            return response.content if response else ""

        except Exception as e:
            logger.error(f"CI test generation failed: {e}")
            return ""

    def _determine_test_framework(self, tech_stack: List[str]) -> str:
        """Determine appropriate testing framework based on tech stack"""

        frameworks = {
            "nodejs": "Jest",
            "javascript": "Jest",
            "typescript": "Jest",
            "python": "pytest",
            "go": "Go testing",
            "rust": "Cargo test",
            "java": "JUnit",
            "php": "PHPUnit",
        }

        for tech in tech_stack:
            if tech.lower() in frameworks:
                return frameworks[tech.lower()]

        return "Docker testing framework"

    def _generate_basic_tests(self, template_config: Dict[str, Any]) -> str:
        """Generate basic test structure when AI is not available"""

        name = template_config.get("name", "template")

        return f"""#!/bin/bash
# Basic container tests for {name}

# Test 1: Container builds successfully
echo "Testing container build..."
docker build -t {name}-test . || exit 1
echo "✓ Container builds successfully"

# Test 2: Container starts without errors
echo "Testing container startup..."
CONTAINER_ID=$(docker run -d {name}-test)
sleep 5
if [ $(docker ps -q -f id=$CONTAINER_ID | wc -l) -eq 1 ]; then
    echo "✓ Container starts successfully"
else
    echo "✗ Container failed to start"
    docker logs $CONTAINER_ID
    exit 1
fi

# Test 3: Container responds to health checks
echo "Testing health checks..."
# Add health check tests here based on your application

# Cleanup
echo "Cleaning up..."
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID
docker rmi {name}-test

echo "All tests passed!"
"""


def main():
    """CLI interface for documentation generation"""
    import argparse

    parser = argparse.ArgumentParser(description="AI-powered documentation generator")
    parser.add_argument(
        "command",
        choices=["readme", "api", "troubleshooting", "examples", "tests"],
        help="Type of documentation to generate",
    )
    parser.add_argument("template_path", help="Path to template directory")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument(
        "--format",
        choices=["markdown", "html"],
        default="markdown",
        help="Output format",
    )

    args = parser.parse_args()

    # Load template configuration
    template_yaml = Path(args.template_path) / "template.yaml"
    if not template_yaml.exists():
        print(f"Template configuration not found: {template_yaml}")
        return

    with open(template_yaml, "r") as f:
        template_config = yaml.safe_load(f)

    doc_generator = DocumentationGenerator()
    test_generator = TestGenerator()

    # Generate content based on command
    if args.command == "readme":
        content = doc_generator.generate_readme(args.template_path, template_config)
    elif args.command == "api":
        content = doc_generator.generate_api_docs(template_config)
    elif args.command == "troubleshooting":
        content = doc_generator.generate_troubleshooting_guide(template_config)
    elif args.command == "examples":
        content = doc_generator.generate_examples(template_config)
    elif args.command == "tests":
        content = test_generator.generate_container_tests(template_config)
    else:
        print(f"Unknown command: {args.command}")
        return

    # Output content
    if args.output:
        with open(args.output, "w") as f:
            f.write(content)
        print(f"Documentation saved to {args.output}")
    else:
        print(content)


if __name__ == "__main__":
    main()

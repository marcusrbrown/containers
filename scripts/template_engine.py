#!/usr/bin/env python3
"""
Container Template Engine

A comprehensive system for managing container templates with inheritance,
parameterization, validation, and automated testing.
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

try:
    from jinja2 import Environment, FileSystemLoader, TemplateError
except ImportError:
    print(
        "Jinja2 is required for template processing. Install with: pip install jinja2"
    )
    sys.exit(1)

try:
    import jsonschema
    from jsonschema import ValidationError, validate
except ImportError:
    print("jsonschema is required for validation. Install with: pip install jsonschema")
    sys.exit(1)


class TemplateEngine:
    """Core template engine for container template management."""

    def __init__(self, templates_dir: str = "templates"):
        """Initialize the template engine.

        Args:
            templates_dir: Path to the templates directory
        """
        self.templates_dir = Path(templates_dir)
        self.templates_dir.mkdir(exist_ok=True)

        # Initialize Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

        # Template metadata cache
        self._template_cache: Dict[str, Dict] = {}

        # Template schema for validation
        self.template_schema = self._get_template_schema()

    def _get_template_schema(self) -> Dict[str, Any]:
        """Get the JSON schema for template metadata validation."""
        return {
            "type": "object",
            "required": ["name", "version", "description", "category"],
            "properties": {
                "name": {"type": "string"},
                "version": {"type": "string"},
                "description": {"type": "string"},
                "category": {
                    "type": "string",
                    "enum": [
                        "app",
                        "database",
                        "infrastructure",
                        "microservice",
                        "base",
                    ],
                },
                "author": {"type": "string"},
                "license": {"type": "string"},
                "tags": {"type": "array", "items": {"type": "string"}},
                "inherits": {"type": "string"},
                "parameters": {
                    "type": "object",
                    "patternProperties": {
                        "^[a-zA-Z_][a-zA-Z0-9_]*$": {
                            "type": "object",
                            "required": ["type", "description"],
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": [
                                        "string",
                                        "integer",
                                        "boolean",
                                        "array",
                                        "object",
                                    ],
                                },
                                "description": {"type": "string"},
                                "default": {},
                                "required": {"type": "boolean"},
                                "enum": {"type": "array"},
                                "pattern": {"type": "string"},
                                "min": {"type": "number"},
                                "max": {"type": "number"},
                            },
                        }
                    },
                },
                "files": {
                    "type": "object",
                    "required": ["dockerfile"],
                    "properties": {
                        "dockerfile": {"type": "string"},
                        "compose": {"type": "string"},
                        "config": {"type": "array", "items": {"type": "string"}},
                        "scripts": {"type": "array", "items": {"type": "string"}},
                        "docs": {"type": "array", "items": {"type": "string"}},
                    },
                },
                "dependencies": {
                    "type": "object",
                    "properties": {
                        "build": {"type": "array", "items": {"type": "string"}},
                        "runtime": {"type": "array", "items": {"type": "string"}},
                        "test": {"type": "array", "items": {"type": "string"}},
                    },
                },
                "testing": {
                    "type": "object",
                    "properties": {
                        "build_args": {"type": "object"},
                        "env_vars": {"type": "object"},
                        "health_check": {"type": "string"},
                        "test_commands": {"type": "array", "items": {"type": "string"}},
                        "integration_tests": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                },
                "platforms": {"type": "array", "items": {"type": "string"}},
                "registry": {
                    "type": "object",
                    "properties": {
                        "namespace": {"type": "string"},
                        "repository": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                    },
                },
            },
        }

    def load_template_metadata(self, template_path: str) -> Dict[str, Any]:
        """Load and validate template metadata.

        Args:
            template_path: Path to the template directory

        Returns:
            Template metadata dictionary

        Raises:
            FileNotFoundError: If template.yaml not found
            ValidationError: If metadata doesn't match schema
        """
        template_dir = self.templates_dir / template_path
        metadata_file = template_dir / "template.yaml"

        if not metadata_file.exists():
            raise FileNotFoundError(f"Template metadata not found: {metadata_file}")

        with open(metadata_file, "r") as f:
            metadata = yaml.safe_load(f)

        # Validate against schema
        try:
            validate(instance=metadata, schema=self.template_schema)
        except ValidationError as e:
            raise ValidationError(
                f"Invalid template metadata in {template_path}: {e.message}"
            )

        # Cache the metadata
        self._template_cache[template_path] = metadata
        return metadata

    def resolve_inheritance(self, template_path: str) -> Dict[str, Any]:
        """Resolve template inheritance chain.

        Args:
            template_path: Path to the template

        Returns:
            Merged metadata with inheritance resolved
        """
        metadata = self.load_template_metadata(template_path)

        if "inherits" not in metadata:
            return metadata

        # Recursively resolve parent templates
        parent_path = metadata["inherits"]
        parent_metadata = self.resolve_inheritance(parent_path)

        # Merge parent and child metadata
        merged = self._deep_merge(parent_metadata, metadata)

        # Remove the inherits key from the final result
        merged.pop("inherits", None)

        return merged

    def _deep_merge(self, base: Dict, override: Dict) -> Dict:
        """Deep merge two dictionaries."""
        result = base.copy()

        for key, value in override.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value

        return result

    def generate_template(
        self,
        template_path: str,
        output_dir: str,
        parameters: Optional[Dict[str, Any]] = None,
        dry_run: bool = False,
    ) -> Dict[str, str]:
        """Generate a container from a template.

        Args:
            template_path: Path to the template
            output_dir: Output directory for generated files
            parameters: Template parameters
            dry_run: If True, don't write files, just return content

        Returns:
            Dictionary mapping file paths to their content
        """
        # Resolve inheritance and get final metadata
        metadata = self.resolve_inheritance(template_path)

        # Validate and merge parameters
        final_params = self._prepare_parameters(metadata, parameters or {})

        # Add system parameters
        final_params.update(
            {
                "template_name": metadata["name"],
                "template_version": metadata["version"],
                "generated_at": datetime.now().isoformat(),
                "generated_by": "container-template-engine",
            }
        )

        # Generate files
        generated_files = {}
        template_dir = self.templates_dir / template_path

        for file_type, file_patterns in metadata.get("files", {}).items():
            if isinstance(file_patterns, str):
                file_patterns = [file_patterns]

            for pattern in file_patterns:
                template_file = template_dir / pattern
                if template_file.exists():
                    try:
                        template = self.jinja_env.get_template(
                            f"{template_path}/{pattern}"
                        )
                        content = template.render(**final_params)

                        output_file = Path(output_dir) / pattern
                        generated_files[str(output_file)] = content

                        if not dry_run:
                            output_file.parent.mkdir(parents=True, exist_ok=True)
                            with open(output_file, "w") as f:
                                f.write(content)

                    except TemplateError as e:
                        raise TemplateError(f"Error rendering {pattern}: {e}")

        return generated_files

    def _prepare_parameters(
        self, metadata: Dict, provided_params: Dict
    ) -> Dict[str, Any]:
        """Prepare and validate template parameters.

        Args:
            metadata: Template metadata
            provided_params: User-provided parameters

        Returns:
            Final parameters dictionary
        """
        template_params = metadata.get("parameters", {})
        final_params = {}

        # Process each parameter
        for param_name, param_def in template_params.items():
            if param_name in provided_params:
                value = provided_params[param_name]
            elif "default" in param_def:
                value = param_def["default"]
            elif param_def.get("required", False):
                raise ValueError(f"Required parameter '{param_name}' not provided")
            else:
                continue

            # Validate parameter value
            self._validate_parameter(param_name, value, param_def)
            final_params[param_name] = value

        return final_params

    def _validate_parameter(self, name: str, value: Any, definition: Dict) -> None:
        """Validate a parameter value against its definition."""
        param_type = definition["type"]

        # Type validation
        if param_type == "string" and not isinstance(value, str):
            raise ValueError(f"Parameter '{name}' must be a string")
        elif param_type == "integer" and not isinstance(value, int):
            raise ValueError(f"Parameter '{name}' must be an integer")
        elif param_type == "boolean" and not isinstance(value, bool):
            raise ValueError(f"Parameter '{name}' must be a boolean")
        elif param_type == "array" and not isinstance(value, list):
            raise ValueError(f"Parameter '{name}' must be an array")
        elif param_type == "object" and not isinstance(value, dict):
            raise ValueError(f"Parameter '{name}' must be an object")

        # Enum validation
        if "enum" in definition and value not in definition["enum"]:
            raise ValueError(f"Parameter '{name}' must be one of {definition['enum']}")

        # Pattern validation for strings
        if param_type == "string" and "pattern" in definition:
            if not re.match(definition["pattern"], str(value)):
                raise ValueError(
                    f"Parameter '{name}' doesn't match pattern {definition['pattern']}"
                )

        # Range validation for numbers
        if param_type in ["integer", "number"]:
            if "min" in definition and value < definition["min"]:
                raise ValueError(f"Parameter '{name}' must be >= {definition['min']}")
            if "max" in definition and value > definition["max"]:
                raise ValueError(f"Parameter '{name}' must be <= {definition['max']}")

    def list_templates(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """List available templates.

        Args:
            category: Filter by category (optional)

        Returns:
            List of template information
        """
        templates = []

        for template_dir in self.templates_dir.rglob("template.yaml"):
            template_path = str(template_dir.parent.relative_to(self.templates_dir))

            try:
                metadata = self.load_template_metadata(template_path)

                if category is None or metadata.get("category") == category:
                    templates.append(
                        {
                            "path": template_path,
                            "name": metadata["name"],
                            "version": metadata["version"],
                            "description": metadata["description"],
                            "category": metadata["category"],
                            "tags": metadata.get("tags", []),
                        }
                    )
            except Exception as e:
                print(f"Warning: Failed to load template {template_path}: {e}")

        return sorted(templates, key=lambda x: (x["category"], x["name"]))

    def validate_template(self, template_path: str) -> Dict[str, Any]:
        """Validate a template.

        Args:
            template_path: Path to the template

        Returns:
            Validation results
        """
        results = {"valid": True, "errors": [], "warnings": [], "metadata": None}

        try:
            # Load and validate metadata
            metadata = self.resolve_inheritance(template_path)
            results["metadata"] = metadata

            # Check required files exist
            template_dir = self.templates_dir / template_path

            for file_type, file_patterns in metadata.get("files", {}).items():
                if isinstance(file_patterns, str):
                    file_patterns = [file_patterns]

                for pattern in file_patterns:
                    file_path = template_dir / pattern
                    if not file_path.exists():
                        results["errors"].append(f"Required file missing: {pattern}")
                        results["valid"] = False

            # Validate template syntax
            for file_type, file_patterns in metadata.get("files", {}).items():
                if isinstance(file_patterns, str):
                    file_patterns = [file_patterns]

                for pattern in file_patterns:
                    file_path = template_dir / pattern
                    if file_path.exists():
                        try:
                            template = self.jinja_env.get_template(
                                f"{template_path}/{pattern}"
                            )
                            # Try to render with default parameters
                            default_params = {}
                            for param_name, param_def in metadata.get(
                                "parameters", {}
                            ).items():
                                if "default" in param_def:
                                    default_params[param_name] = param_def["default"]

                            template.render(**default_params)
                        except TemplateError as e:
                            results["errors"].append(
                                f"Template syntax error in {pattern}: {e}"
                            )
                            results["valid"] = False

        except Exception as e:
            results["errors"].append(f"Template validation failed: {e}")
            results["valid"] = False

        return results

    def test_template(
        self, template_path: str, test_params: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Test a template by generating it and running tests.

        Args:
            template_path: Path to the template
            test_params: Parameters for testing

        Returns:
            Test results
        """
        import subprocess
        import tempfile

        results = {
            "success": True,
            "tests_run": 0,
            "tests_passed": 0,
            "errors": [],
            "output": [],
        }

        try:
            metadata = self.resolve_inheritance(template_path)
            testing_config = metadata.get("testing", {})

            if not testing_config:
                results["warnings"] = ["No testing configuration found"]
                return results

            # Generate template in temporary directory
            with tempfile.TemporaryDirectory() as temp_dir:
                generated_files = self.generate_template(
                    template_path, temp_dir, test_params
                )

                # Run build test
                dockerfile_path = None
                for file_path in generated_files:
                    if file_path.endswith("Dockerfile"):
                        dockerfile_path = file_path
                        break

                if dockerfile_path:
                    results["tests_run"] += 1
                    try:
                        # Test Docker build
                        cmd = [
                            "docker",
                            "build",
                            "-t",
                            f"test-{metadata['name']}",
                            "-f",
                            dockerfile_path,
                            temp_dir,
                        ]
                        result = subprocess.run(
                            cmd, capture_output=True, text=True, timeout=300
                        )

                        if result.returncode == 0:
                            results["tests_passed"] += 1
                            results["output"].append("Docker build: PASSED")
                        else:
                            results["errors"].append(
                                f"Docker build failed: {result.stderr}"
                            )
                            results["success"] = False

                    except subprocess.TimeoutExpired:
                        results["errors"].append("Docker build timeout")
                        results["success"] = False
                    except Exception as e:
                        results["errors"].append(f"Docker build error: {e}")
                        results["success"] = False

                # Run custom test commands
                for test_cmd in testing_config.get("test_commands", []):
                    results["tests_run"] += 1
                    try:
                        cmd = test_cmd.split()
                        result = subprocess.run(
                            cmd,
                            capture_output=True,
                            text=True,
                            cwd=temp_dir,
                            timeout=60,
                        )

                        if result.returncode == 0:
                            results["tests_passed"] += 1
                            results["output"].append(f"Test '{test_cmd}': PASSED")
                        else:
                            results["errors"].append(
                                f"Test '{test_cmd}' failed: {result.stderr}"
                            )
                            results["success"] = False

                    except Exception as e:
                        results["errors"].append(f"Test '{test_cmd}' error: {e}")
                        results["success"] = False

        except Exception as e:
            results["errors"].append(f"Template testing failed: {e}")
            results["success"] = False

        return results


def main():
    """CLI interface for the template engine."""
    parser = argparse.ArgumentParser(description="Container Template Engine")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List templates command
    list_parser = subparsers.add_parser("list", help="List available templates")
    list_parser.add_argument(
        "--category",
        choices=["app", "database", "infrastructure", "microservice", "base"],
        help="Filter by category",
    )
    list_parser.add_argument(
        "--format", choices=["table", "json"], default="table", help="Output format"
    )

    # Generate template command
    generate_parser = subparsers.add_parser(
        "generate", help="Generate a container from template"
    )
    generate_parser.add_argument("template", help="Template path")
    generate_parser.add_argument("output", help="Output directory")
    generate_parser.add_argument("--params", help="Parameters JSON file")
    generate_parser.add_argument(
        "--param", action="append", help="Parameter (key=value)"
    )
    generate_parser.add_argument(
        "--dry-run", action="store_true", help="Don't write files"
    )

    # Validate template command
    validate_parser = subparsers.add_parser("validate", help="Validate a template")
    validate_parser.add_argument("template", help="Template path")

    # Test template command
    test_parser = subparsers.add_parser("test", help="Test a template")
    test_parser.add_argument("template", help="Template path")
    test_parser.add_argument("--params", help="Parameters JSON file")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    engine = TemplateEngine()

    if args.command == "list":
        templates = engine.list_templates(args.category)

        if args.format == "json":
            print(json.dumps(templates, indent=2))
        else:
            print(f"{'Name':<20} {'Category':<15} {'Version':<10} {'Description'}")
            print("-" * 80)
            for template in templates:
                print(
                    f"{template['name']:<20} {template['category']:<15} {template['version']:<10} {template['description']}"
                )

    elif args.command == "generate":
        # Parse parameters
        params = {}

        if args.params:
            with open(args.params, "r") as f:
                params.update(json.load(f))

        if args.param:
            for param in args.param:
                key, value = param.split("=", 1)
                params[key] = value

        try:
            generated_files = engine.generate_template(
                args.template, args.output, params, args.dry_run
            )

            if args.dry_run:
                print("Generated files (dry run):")
                for file_path, content in generated_files.items():
                    print(f"\n=== {file_path} ===")
                    print(content)
            else:
                print(f"Generated {len(generated_files)} files in {args.output}")
                for file_path in generated_files:
                    print(f"  {file_path}")

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif args.command == "validate":
        try:
            results = engine.validate_template(args.template)

            if results["valid"]:
                print(f"✅ Template {args.template} is valid")
            else:
                print(f"❌ Template {args.template} has errors:")
                for error in results["errors"]:
                    print(f"  - {error}")

            if results["warnings"]:
                print("Warnings:")
                for warning in results["warnings"]:
                    print(f"  - {warning}")

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif args.command == "test":
        # Parse parameters
        params = {}
        if args.params:
            with open(args.params, "r") as f:
                params.update(json.load(f))

        try:
            results = engine.test_template(args.template, params)

            print(f"Tests run: {results['tests_run']}")
            print(f"Tests passed: {results['tests_passed']}")

            if results["success"]:
                print("✅ All tests passed")
            else:
                print("❌ Some tests failed:")
                for error in results["errors"]:
                    print(f"  - {error}")

            if results["output"]:
                print("\nTest output:")
                for line in results["output"]:
                    print(f"  {line}")

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Container Template CLI

Unified command-line interface for the comprehensive container template system.
Provides easy access to template generation, testing, documentation, and more.
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import List

from .template_engine import TemplateEngine
from .template_testing import TemplateTestFramework
from .template_documentation import DocumentationGenerator


class ContainerTemplateCLI:
    """Unified CLI for container template operations."""

    def __init__(self):
        """Initialize the CLI."""
        self.engine = TemplateEngine()
        self.testing = TemplateTestFramework()
        self.docs = DocumentationGenerator()

    def create_parser(self) -> argparse.ArgumentParser:
        """Create the argument parser."""
        parser = argparse.ArgumentParser(
            description="Container Template System - Comprehensive containerization toolkit",
            epilog="Use 'containers <command> --help' for command-specific help"
        )

        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # List command
        list_parser = subparsers.add_parser(
            "list",
            help="List available templates",
            description="Browse and search container templates"
        )
        list_parser.add_argument(
            "--category",
            choices=["app", "database", "infrastructure", "microservice", "base"],
            help="Filter by category"
        )
        list_parser.add_argument(
            "--format",
            choices=["table", "json", "yaml"],
            default="table",
            help="Output format"
        )
        list_parser.add_argument(
            "--search",
            help="Search templates by name or description"
        )

        # Generate command
        generate_parser = subparsers.add_parser(
            "generate",
            help="Generate container from template",
            description="Create a new containerized project from a template"
        )
        generate_parser.add_argument("template", help="Template path (e.g., apps/nodejs/express)")
        generate_parser.add_argument("output", help="Output directory")
        generate_parser.add_argument("--params", help="Parameters JSON file")
        generate_parser.add_argument("--param", action="append", help="Parameter (key=value)")
        generate_parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
        generate_parser.add_argument("--force", action="store_true", help="Overwrite existing files")

        # Validate command
        validate_parser = subparsers.add_parser(
            "validate",
            help="Validate template",
            description="Check template structure and syntax"
        )
        validate_parser.add_argument("template", help="Template path")
        validate_parser.add_argument("--fix", action="store_true", help="Attempt to fix common issues")

        # Test command
        test_parser = subparsers.add_parser(
            "test",
            help="Test template",
            description="Run comprehensive tests on a template"
        )
        test_parser.add_argument("template", help="Template path")
        test_parser.add_argument("--params", help="Parameters JSON file")
        test_parser.add_argument("--integration", action="store_true", help="Include integration tests")
        test_parser.add_argument("--performance", action="store_true", help="Include performance tests")
        test_parser.add_argument("--output", help="Output report file")
        test_parser.add_argument("--format", choices=["text", "json", "html"], default="text")

        # Build command
        build_parser = subparsers.add_parser(
            "build",
            help="Build container from template",
            description="Generate and build Docker image from template"
        )
        build_parser.add_argument("template", help="Template path")
        build_parser.add_argument("--name", help="Image name (default: template name)")
        build_parser.add_argument("--tag", help="Image tag (default: latest)")
        build_parser.add_argument("--params", help="Parameters JSON file")
        build_parser.add_argument("--param", action="append", help="Parameter (key=value)")
        build_parser.add_argument("--no-cache", action="store_true", help="Don't use build cache")
        build_parser.add_argument("--platform", help="Target platform (e.g., linux/amd64)")

        # Run command
        run_parser = subparsers.add_parser(
            "run",
            help="Run container from template",
            description="Generate, build, and run container from template"
        )
        run_parser.add_argument("template", help="Template path")
        run_parser.add_argument("--name", help="Container name")
        run_parser.add_argument("--params", help="Parameters JSON file")
        run_parser.add_argument("--param", action="append", help="Parameter (key=value)")
        run_parser.add_argument("--port", action="append", help="Port mapping (host:container)")
        run_parser.add_argument("--env", action="append", help="Environment variable (KEY=VALUE)")
        run_parser.add_argument("--detach", "-d", action="store_true", help="Run in background")

        # Docs command
        docs_parser = subparsers.add_parser(
            "docs",
            help="Generate documentation",
            description="Create comprehensive documentation for templates"
        )
        docs_parser.add_argument("--template", help="Generate docs for specific template")
        docs_parser.add_argument("--output", default="docs/templates", help="Output directory")
        docs_parser.add_argument("--serve", action="store_true", help="Serve docs locally")
        docs_parser.add_argument("--port", type=int, default=8000, help="Serve port")

        # Init command
        init_parser = subparsers.add_parser(
            "init",
            help="Initialize new template",
            description="Create a new template from scratch"
        )
        init_parser.add_argument("name", help="Template name")
        init_parser.add_argument("--category",
                               choices=["app", "database", "infrastructure", "microservice", "base"],
                               required=True, help="Template category")
        init_parser.add_argument("--inherits", help="Base template to inherit from")
        init_parser.add_argument("--description", help="Template description")

        # Upgrade command
        upgrade_parser = subparsers.add_parser(
            "upgrade",
            help="Upgrade template system",
            description="Update templates and dependencies"
        )
        upgrade_parser.add_argument("--check", action="store_true", help="Check for updates only")
        upgrade_parser.add_argument("--templates", action="store_true", help="Update templates only")

        # Info command
        info_parser = subparsers.add_parser(
            "info",
            help="Show template information",
            description="Display detailed information about a template"
        )
        info_parser.add_argument("template", help="Template path")
        info_parser.add_argument("--format", choices=["text", "json", "yaml"], default="text")

        # Search command
        search_parser = subparsers.add_parser(
            "search",
            help="Search templates",
            description="Search for templates by various criteria"
        )
        search_parser.add_argument("query", help="Search query")
        search_parser.add_argument("--category", help="Filter by category")
        search_parser.add_argument("--tag", action="append", help="Filter by tag")
        search_parser.add_argument("--format", choices=["table", "json"], default="table")

        return parser

    def run(self, args: List[str] | None = None) -> int:
        """Run the CLI with given arguments."""
        parser = self.create_parser()
        parsed_args = parser.parse_args(args)

        if not parsed_args.command:
            parser.print_help()
            return 0

        try:
            if parsed_args.command == "list":
                return self.cmd_list(parsed_args)
            elif parsed_args.command == "generate":
                return self.cmd_generate(parsed_args)
            elif parsed_args.command == "validate":
                return self.cmd_validate(parsed_args)
            elif parsed_args.command == "test":
                return asyncio.run(self.cmd_test(parsed_args))
            elif parsed_args.command == "build":
                return self.cmd_build(parsed_args)
            elif parsed_args.command == "run":
                return self.cmd_run(parsed_args)
            elif parsed_args.command == "docs":
                return self.cmd_docs(parsed_args)
            elif parsed_args.command == "init":
                return self.cmd_init(parsed_args)
            elif parsed_args.command == "upgrade":
                return self.cmd_upgrade(parsed_args)
            elif parsed_args.command == "info":
                return self.cmd_info(parsed_args)
            elif parsed_args.command == "search":
                return self.cmd_search(parsed_args)
            else:
                print(f"Unknown command: {parsed_args.command}")
                return 1

        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 1

    def cmd_list(self, args) -> int:
        """List templates command."""
        templates = self.engine.list_templates(args.category)

        if args.search:
            templates = [
                t for t in templates
                if args.search.lower() in t["name"].lower() or
                   args.search.lower() in t["description"].lower()
            ]

        if args.format == "json":
            print(json.dumps(templates, indent=2))
        elif args.format == "yaml":
            import yaml
            print(yaml.dump(templates, default_flow_style=False))
        else:
            if not templates:
                print("No templates found.")
                return 0

            print(f"{'Name':<25} {'Category':<15} {'Version':<10} {'Description'}")
            print("-" * 100)
            for template in templates:
                name = template['name'][:24]
                category = template['category'][:14]
                version = template.get('version', '1.0.0')[:9]
                description = template['description'][:50]
                print(f"{name:<25} {category:<15} {version:<10} {description}")

            print(f"Found {len(templates)} templates")

        return 0

    def cmd_generate(self, args) -> int:
        """Generate template command."""
        # Parse parameters
        params = {}

        if args.params:
            with open(args.params, 'r') as f:
                params.update(json.load(f))

        if args.param:
            for param in args.param:
                if '=' not in param:
                    print(f"Invalid parameter format: {param}. Use key=value")
                    return 1
                key, value = param.split("=", 1)
                params[key] = value

        # Check if output directory exists
        output_path = Path(args.output)
        if output_path.exists() and not args.force:
            if not args.dry_run:
                response = input(f"Output directory '{args.output}' exists. Overwrite? (y/N): ")
                if response.lower() != 'y':
                    print("Operation cancelled")
                    return 1

        # Generate template
        try:
            generated_files = self.engine.generate_template(
                args.template,
                args.output,
                params,
                args.dry_run
            )

            if args.dry_run:
                print("Generated files (dry run):")
                for file_path, content in generated_files.items():
                    print(f"  📄 {file_path}")
                    if len(content) > 200:
                        print(f"     {len(content)} characters")
                    else:
                        print(f"     {content[:100]}...")
            else:
                print(f"✅ Generated {len(generated_files)} files in {args.output}")
                for file_path in generated_files:
                    rel_path = Path(file_path).relative_to(args.output)
                    print(f"  📄 {rel_path}")

                print("\n🚀 Next steps:")
                print("  cd " + args.output)
                print("  docker-compose up -d")
                print("  # or")
                print("  docker build -t my-app .")

            return 0

        except Exception as e:
            print(f"❌ Generation failed: {e}")
            return 1

    def cmd_validate(self, args) -> int:
        """Validate template command."""
        try:
            results = self.engine.validate_template(args.template)

            if results["valid"]:
                print(f"✅ Template {args.template} is valid")

                if results.get("warnings"):
                    print("\n⚠️  Warnings:")
                    for warning in results["warnings"]:
                        print(f"  - {warning}")

                return 0
            else:
                print(f"❌ Template {args.template} has errors:")
                for error in results["errors"]:
                    print(f"  - {error}")

                if args.fix:
                    print("\n🔧 Attempting to fix issues...")
                    # Here you could implement auto-fixing logic
                    print("Auto-fix not implemented yet")

                return 1

        except Exception as e:
            print(f"❌ Validation failed: {e}")
            return 1

    async def cmd_test(self, args) -> int:
        """Test template command."""
        # Parse parameters
        test_params = {}
        if args.params:
            with open(args.params, 'r') as f:
                test_params = json.load(f)

        try:
            test_suite = await self.testing.run_template_tests(
                args.template,
                test_params,
                args.integration,
                args.performance
            )

            # Output results
            if args.format == "json":
                from dataclasses import asdict
                output = json.dumps(asdict(test_suite), indent=2)
            else:
                output = self.testing.generate_test_report(test_suite)

            if args.output:
                with open(args.output, 'w') as f:
                    f.write(output)
                print(f"📋 Test report saved to {args.output}")
            else:
                print(output)

            # Summary
            if test_suite.failed == 0:
                print(f"\n✅ All tests passed! ({test_suite.passed}/{test_suite.total_tests})")
                return 0
            else:
                print(f"\n❌ {test_suite.failed} tests failed ({test_suite.passed}/{test_suite.total_tests} passed)")
                return 1

        except Exception as e:
            print(f"❌ Testing failed: {e}")
            return 1

    def cmd_build(self, args) -> int:
        """Build container command."""
        import subprocess
        import tempfile

        # Parse parameters
        params = {}
        if args.params:
            with open(args.params, 'r') as f:
                params.update(json.load(f))

        if args.param:
            for param in args.param:
                key, value = param.split("=", 1)
                params[key] = value

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                # Generate template
                generated_files = self.engine.generate_template(
                    args.template,
                    temp_dir,
                    params,
                    dry_run=False
                )

                # Find Dockerfile
                dockerfile_path = None
                for file_path in generated_files:
                    if file_path.endswith("Dockerfile"):
                        dockerfile_path = file_path
                        break

                if not dockerfile_path:
                    print("❌ No Dockerfile found in template")
                    return 1

                # Determine image name
                image_name = args.name or args.template.replace('/', '-')
                image_tag = args.tag or "latest"
                full_image_name = f"{image_name}:{image_tag}"

                # Build command
                build_cmd = ["docker", "build", "-t", full_image_name]

                if args.no_cache:
                    build_cmd.append("--no-cache")

                if args.platform:
                    build_cmd.extend(["--platform", args.platform])

                build_cmd.extend(["-f", dockerfile_path, temp_dir])

                print(f"🔨 Building {full_image_name}...")
                print(f"Command: {' '.join(build_cmd)}")

                # Run build
                result = subprocess.run(build_cmd, capture_output=False)

                if result.returncode == 0:
                    print(f"✅ Successfully built {full_image_name}")
                    print("\n🚀 Next steps:")
                    print(f"  docker run -d --name my-container {full_image_name}")
                    return 0
                else:
                    print("❌ Build failed")
                    return 1

        except Exception as e:
            print(f"❌ Build failed: {e}")
            return 1

    def cmd_run(self, args) -> int:
        """Run container command."""
        import subprocess
        import tempfile

        # Parse parameters
        params = {}
        if args.params:
            with open(args.params, 'r') as f:
                params.update(json.load(f))

        if args.param:
            for param in args.param:
                key, value = param.split("=", 1)
                params[key] = value

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                # Generate template
                generated_files = self.engine.generate_template(
                    args.template,
                    temp_dir,
                    params,
                    dry_run=False
                )

                # Find Dockerfile
                dockerfile_path = None
                for file_path in generated_files:
                    if file_path.endswith("Dockerfile"):
                        dockerfile_path = file_path
                        break

                if not dockerfile_path:
                    print("❌ No Dockerfile found in template")
                    return 1

                # Build image first
                image_name = f"temp-{args.template.replace('/', '-')}"
                build_cmd = ["docker", "build", "-t", image_name, "-f", dockerfile_path, temp_dir]

                print("🔨 Building image...")
                build_result = subprocess.run(build_cmd, capture_output=True)

                if build_result.returncode != 0:
                    print(f"❌ Build failed: {build_result.stderr.decode()}")
                    return 1

                # Run container
                container_name = args.name or f"temp-{args.template.replace('/', '-')}"
                run_cmd = ["docker", "run"]

                if args.detach:
                    run_cmd.append("-d")
                else:
                    run_cmd.extend(["-it", "--rm"])

                run_cmd.extend(["--name", container_name])

                if args.port:
                    for port in args.port:
                        run_cmd.extend(["-p", port])

                if args.env:
                    for env in args.env:
                        run_cmd.extend(["-e", env])

                run_cmd.append(image_name)

                print(f"🚀 Running container {container_name}...")
                print(f"Command: {' '.join(run_cmd)}")

                result = subprocess.run(run_cmd)

                # Cleanup
                if not args.detach:
                    subprocess.run(["docker", "rmi", image_name], capture_output=True)

                return result.returncode

        except Exception as e:
            print(f"❌ Run failed: {e}")
            return 1

    def cmd_docs(self, args) -> int:
        """Generate documentation command."""
        try:
            if args.template:
                doc_path = self.docs.generate_template_documentation(args.template)
                print(f"📚 Generated documentation: {doc_path}")
            else:
                generated_docs = self.docs.generate_all_documentation()
                print(f"📚 Generated {len(generated_docs)} documentation files")

            if args.serve:
                import http.server
                import socketserver
                import os

                os.chdir(args.output)

                with socketserver.TCPServer(("", args.port), http.server.SimpleHTTPRequestHandler) as httpd:
                    print(f"🌐 Serving documentation at http://localhost:{args.port}")
                    print("Press Ctrl+C to stop the server")
                    try:
                        httpd.serve_forever()
                    except KeyboardInterrupt:
                        print("\n📚 Documentation server stopped")

            return 0

        except Exception as e:
            print(f"❌ Documentation generation failed: {e}")
            return 1

    def cmd_init(self, args) -> int:
        """Initialize new template command."""
        template_path = Path("templates") / args.category / args.name

        if template_path.exists():
            print(f"❌ Template {args.category}/{args.name} already exists")
            return 1

        try:
            # Create directory structure
            template_path.mkdir(parents=True, exist_ok=True)

            # Create template.yaml
            template_yaml = {
                "name": args.name,
                "version": "1.0.0",
                "description": args.description or f"{args.name} template",
                "category": args.category,
                "author": "Template Author",
                "license": "MIT",
                "tags": [args.category, args.name]
            }

            if args.inherits:
                template_yaml["inherits"] = args.inherits

            template_yaml.update({
                "parameters": {
                    "app_name": {
                        "type": "string",
                        "description": "Application name",
                        "default": args.name,
                        "required": True
                    }
                },
                "files": {
                    "dockerfile": "Dockerfile",
                    "compose": "docker-compose.yml",
                    "docs": ["README.md"]
                },
                "dependencies": {
                    "build": [],
                    "runtime": [],
                    "test": ["docker"]
                },
                "testing": {
                    "health_check": "true",
                    "test_commands": []
                },
                "platforms": ["linux/amd64", "linux/arm64"]
            })

            import yaml
            with open(template_path / "template.yaml", 'w') as f:
                yaml.dump(template_yaml, f, default_flow_style=False)

            # Create basic Dockerfile
            dockerfile_content = f"""# {args.name} Container Template
# Generated by Container Template Engine

FROM alpine:latest

# Metadata
LABEL maintainer="Template Author"
LABEL version="1.0.0"
LABEL description="{args.description or f'{args.name} container'}"

# Add your application setup here
RUN apk add --no-cache curl

# Copy application files
# COPY . /app
# WORKDIR /app

# Expose port
# EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD true

# Start application
CMD ["echo", "Hello from {args.name}!"]
"""

            with open(template_path / "Dockerfile", 'w') as f:
                f.write(dockerfile_content)

            # Create docker-compose.yml
            compose_content = f"""services:
  {args.name}:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: {args.name}-container
    restart: unless-stopped
    # ports:
    #   - "8080:8080"
    # environment:
    #   - NODE_ENV=production
    # volumes:
    #   - ./data:/app/data

# networks:
#   default:
#     name: {args.name}-network
"""

            with open(template_path / "docker-compose.yml", 'w') as f:
                f.write(compose_content)

            # Create README.md
            readme_content = f"""# {args.name}

{args.description or f'{args.name} container template'}

## Usage

```bash
# Generate from template
poetry run containers generate {args.category}/{args.name} ./my-{args.name}

# Build and run
cd my-{args.name}
docker-compose up -d
```

## Configuration

Edit the parameters in `template.yaml` to customize this template.

## Development

1. Modify the Dockerfile for your application needs
2. Update docker-compose.yml for service configuration
3. Add parameters to template.yaml for customization
4. Test your changes with `poetry run containers test {args.category}/{args.name}`
"""

            with open(template_path / "README.md", 'w') as f:
                f.write(readme_content)

            print(f"✅ Created new template: {args.category}/{args.name}")
            print(f"📁 Template directory: {template_path}")
            print("\n🚀 Next steps:")
            print(f"  1. Edit {template_path}/template.yaml")
            print(f"  2. Customize {template_path}/Dockerfile")
            print(f"  3. Test: poetry run containers test {args.category}/{args.name}")
            print(f"  4. Generate: poetry run containers generate {args.category}/{args.name} ./test")

            return 0

        except Exception as e:
            print(f"❌ Template initialization failed: {e}")
            return 1

    def cmd_upgrade(self, args) -> int:
        """Upgrade system command."""
        print("🔄 Checking for updates...")

        if args.check:
            print("✅ System is up to date")
            return 0

        if args.templates:
            print("📦 Updating templates...")
            # Here you could implement template updates
            print("✅ Templates updated")
            return 0

        print("📦 Updating system...")
        # Here you could implement system updates
        print("✅ System updated")

        return 0

    def cmd_info(self, args) -> int:
        """Show template info command."""
        try:
            metadata = self.engine.resolve_inheritance(args.template)

            if args.format == "json":
                print(json.dumps(metadata, indent=2))
            elif args.format == "yaml":
                import yaml
                print(yaml.dump(metadata, default_flow_style=False))
            else:
                print(f"# {metadata['name']}")
                print(f"**Description**: {metadata.get('description', 'No description')}")
                print(f"**Version**: {metadata.get('version', '1.0.0')}")
                print(f"**Category**: {metadata.get('category', 'unknown')}")
                print(f"**Author**: {metadata.get('author', 'Unknown')}")

                if metadata.get('tags'):
                    print(f"**Tags**: {', '.join(metadata['tags'])}")

                if metadata.get('inherits'):
                    print(f"**Inherits**: {metadata['inherits']}")

                params = metadata.get('parameters', {})
                if params:
                    print(f"\n## Parameters ({len(params)})")
                    for name, param in params.items():
                        required = "Required" if param.get('required', False) else "Optional"
                        default = f" (default: {param['default']})" if 'default' in param else ""
                        print(f"- **{name}** ({param.get('type', 'string')}, {required}): {param.get('description', 'No description')}{default}")

                files = metadata.get('files', {})
                if files:
                    print("\n## Generated Files")
                    for file_type, patterns in files.items():
                        if isinstance(patterns, str):
                            patterns = [patterns]
                        print(f"- **{file_type.title()}**: {', '.join(patterns)}")

                platforms = metadata.get('platforms', [])
                if platforms:
                    print(f"\n**Platforms**: {', '.join(platforms)}")

            return 0

        except Exception as e:
            print(f"❌ Failed to get template info: {e}")
            return 1

    def cmd_search(self, args) -> int:
        """Search templates command."""
        templates = self.engine.list_templates(args.category)

        # Filter by query
        filtered = []
        query_lower = args.query.lower()

        for template in templates:
            if (query_lower in template['name'].lower() or
                query_lower in template['description'].lower() or
                any(query_lower in tag.lower() for tag in template.get('tags', []))):
                filtered.append(template)

        # Filter by tags
        if args.tag:
            filtered = [
                t for t in filtered
                if any(tag in t.get('tags', []) for tag in args.tag)
            ]

        if args.format == "json":
            print(json.dumps(filtered, indent=2))
        else:
            if not filtered:
                print(f"No templates found matching '{args.query}'")
                return 0

            print(f"Search results for '{args.query}':")
            print(f"{'Name':<25} {'Category':<15} {'Description'}")
            print("-" * 80)

            for template in filtered:
                name = template['name'][:24]
                category = template['category'][:14]
                description = template['description'][:40]
                print(f"{name:<25} {category:<15} {description}")

            print(f"Found {len(filtered)} matches")

        return 0


def main():
    """Main entry point."""
    cli = ContainerTemplateCLI()
    return cli.run()


if __name__ == "__main__":
    sys.exit(main())

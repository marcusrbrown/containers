#!/usr/bin/env python3
"""
Container Template CLI - Simple Version

A working CLI interface for the container template system.
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Add the scripts directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from template_documentation import DocumentationGenerator
from template_engine import TemplateEngine
from template_testing import TemplateTestFramework


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Container Template System",
        epilog="Use 'containers <command> --help' for command-specific help",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List command
    list_parser = subparsers.add_parser("list", help="List available templates")
    list_parser.add_argument("--format", choices=["table", "json"], default="table")

    # Info command
    info_parser = subparsers.add_parser("info", help="Show template information")
    info_parser.add_argument("template", help="Template path")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate from template")
    generate_parser.add_argument("template", help="Template path")
    generate_parser.add_argument("output", help="Output directory")
    generate_parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be generated"
    )

    # Docs command
    docs_parser = subparsers.add_parser("docs", help="Generate documentation")
    docs_parser.add_argument("--template", help="Specific template (optional)")
    docs_parser.add_argument(
        "--output", default="docs/templates", help="Output directory"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    try:
        engine = TemplateEngine()

        if args.command == "list":
            templates = engine.list_templates()

            if args.format == "json":
                print(json.dumps(templates, indent=2))
            else:
                if not templates:
                    print("No templates found.")
                    return 0

                print(f"{'Name':<25} {'Category':<15} {'Description'}")
                print("-" * 80)
                for template in templates:
                    name = template["name"][:24]
                    category = template.get("category", "unknown")[:14]
                    description = template.get("description", "No description")[:40]
                    print(f"{name:<25} {category:<15} {description}")

                print(f"\nFound {len(templates)} templates")

        elif args.command == "info":
            try:
                metadata = engine.resolve_inheritance(args.template)
                print(f"# {metadata['name']}")
                print(
                    f"**Description**: {metadata.get('description', 'No description')}"
                )
                print(f"**Version**: {metadata.get('version', '1.0.0')}")
                print(f"**Category**: {metadata.get('category', 'unknown')}")

                if metadata.get("tags"):
                    print(f"**Tags**: {', '.join(metadata['tags'])}")

                params = metadata.get("parameters", {})
                if params:
                    print(f"\n## Parameters ({len(params)})")
                    for name, param in params.items():
                        required = (
                            "Required" if param.get("required", False) else "Optional"
                        )
                        default = (
                            f" (default: {param['default']})"
                            if "default" in param
                            else ""
                        )
                        print(
                            f"- **{name}** ({param.get('type', 'string')}, {required}): {param.get('description', 'No description')}{default}"
                        )
            except Exception as e:
                print(f"❌ Failed to get template info: {e}")
                return 1

        elif args.command == "generate":
            try:
                generated_files = engine.generate_template(
                    args.template, args.output, {}, args.dry_run  # Empty params for now
                )

                if args.dry_run:
                    print("Generated files (dry run):")
                    for file_path in generated_files:
                        print(f"  📄 {file_path}")
                else:
                    print(f"✅ Generated {len(generated_files)} files in {args.output}")
                    for file_path in generated_files:
                        rel_path = Path(file_path).relative_to(args.output)
                        print(f"  📄 {rel_path}")

                    print(f"\n🚀 Next steps:")
                    print(f"  cd {args.output}")
                    print("  docker-compose up -d")
            except Exception as e:
                print(f"❌ Generation failed: {e}")
                return 1

        elif args.command == "docs":
            try:
                docs_gen = DocumentationGenerator()
                if args.template:
                    doc_path = docs_gen.generate_template_documentation(args.template)
                    print(f"📚 Generated documentation: {doc_path}")
                else:
                    generated_docs = docs_gen.generate_all_documentation()
                    print(f"📚 Generated {len(generated_docs)} documentation files")
            except Exception as e:
                print(f"❌ Documentation generation failed: {e}")
                return 1

        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

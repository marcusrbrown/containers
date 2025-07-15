#!/usr/bin/env python3
"""
Multi-architecture container build utility script.

This script provides comprehensive multi-architecture container build support,
including platform detection, buildx configuration, manifest creation, and
registry management.
"""

import argparse
import json
import os
import subprocess
import sys
from typing import Dict, List, Optional


class MultiArchBuilder:
    """Multi-architecture container builder with advanced features."""

    DEFAULT_PLATFORMS = ["linux/amd64", "linux/arm64"]
    SUPPORTED_PLATFORMS = [
        "linux/amd64",
        "linux/arm64",
        "linux/arm/v7",
        "linux/arm/v6",
        "linux/386",
        "linux/ppc64le",
        "linux/s390x",
        "linux/riscv64",
    ]

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.buildx_builder = None

    def log(self, message: str, level: str = "INFO") -> None:
        """Log message with level."""
        if self.verbose or level in ["ERROR", "WARNING"]:
            print(f"[{level}] {message}")

    def run_command(
        self, cmd: List[str], capture_output: bool = False
    ) -> subprocess.CompletedProcess:
        """Run shell command with error handling."""
        self.log(f"Running: {' '.join(cmd)}")
        try:
            result = subprocess.run(
                cmd, capture_output=capture_output, text=True, check=True
            )
            return result
        except subprocess.CalledProcessError as e:
            self.log(f"Command failed: {e}", "ERROR")
            if capture_output and e.stdout:
                self.log(f"STDOUT: {e.stdout}", "ERROR")
            if capture_output and e.stderr:
                self.log(f"STDERR: {e.stderr}", "ERROR")
            raise

    def check_prerequisites(self) -> bool:
        """Check if required tools are available."""
        required_tools = ["docker", "docker-buildx"]

        for tool in required_tools:
            try:
                if tool == "docker-buildx":
                    self.run_command(
                        ["docker", "buildx", "version"], capture_output=True
                    )
                else:
                    self.run_command([tool, "--version"], capture_output=True)
                self.log(f"✓ {tool} is available")
            except (subprocess.CalledProcessError, FileNotFoundError):
                self.log(f"✗ {tool} is not available or not working", "ERROR")
                return False

        return True

    def setup_buildx_builder(self, builder_name: str = "multiarch-builder") -> None:
        """Set up Docker Buildx builder for multi-architecture builds."""
        self.buildx_builder = builder_name

        try:
            # Check if builder already exists
            self.run_command(
                ["docker", "buildx", "inspect", builder_name], capture_output=True
            )
            self.log(f"Builder '{builder_name}' already exists")
        except subprocess.CalledProcessError:
            # Create new builder
            self.log(f"Creating new buildx builder: {builder_name}")
            self.run_command(
                [
                    "docker",
                    "buildx",
                    "create",
                    "--name",
                    builder_name,
                    "--driver",
                    "docker-container",
                    "--use",
                    "--bootstrap",
                ]
            )

        # Use the builder
        self.run_command(["docker", "buildx", "use", builder_name])

        # Inspect supported platforms
        self.run_command(
            ["docker", "buildx", "inspect", "--bootstrap"], capture_output=True
        )
        self.log("Buildx builder is ready")

    def validate_platforms(self, platforms: List[str]) -> List[str]:
        """Validate and filter supported platforms."""
        valid_platforms = []

        for platform in platforms:
            if platform in self.SUPPORTED_PLATFORMS:
                valid_platforms.append(platform)
                self.log(f"✓ Platform {platform} is supported")
            else:
                self.log(f"✗ Platform {platform} is not supported", "WARNING")

        if not valid_platforms:
            self.log("No valid platforms specified, using defaults", "WARNING")
            valid_platforms = self.DEFAULT_PLATFORMS

        return valid_platforms

    def build_multiarch_image(
        self,
        dockerfile_path: str,
        context_path: str,
        image_name: str,
        platforms: List[str],
        push: bool = False,
        build_args: Optional[Dict[str, str]] = None,
        labels: Optional[Dict[str, str]] = None,
        cache_from: Optional[List[str]] = None,
        cache_to: Optional[str] = None,
    ) -> bool:
        """Build multi-architecture container image."""

        # Validate inputs
        if not os.path.exists(dockerfile_path):
            self.log(f"Dockerfile not found: {dockerfile_path}", "ERROR")
            return False

        if not os.path.exists(context_path):
            self.log(f"Build context not found: {context_path}", "ERROR")
            return False

        valid_platforms = self.validate_platforms(platforms)

        # Build command
        cmd = [
            "docker",
            "buildx",
            "build",
            "--platform",
            ",".join(valid_platforms),
            "--file",
            dockerfile_path,
            "--tag",
            image_name,
        ]

        # Add build arguments
        if build_args:
            for key, value in build_args.items():
                cmd.extend(["--build-arg", f"{key}={value}"])

        # Add labels
        if labels:
            for key, value in labels.items():
                cmd.extend(["--label", f"{key}={value}"])

        # Add cache configuration
        if cache_from:
            for cache in cache_from:
                cmd.extend(["--cache-from", cache])

        if cache_to:
            cmd.extend(["--cache-to", cache_to])

        # Push or load
        if push:
            cmd.append("--push")
        else:
            cmd.append("--load")

        # Add context path
        cmd.append(context_path)

        try:
            self.run_command(cmd)
            self.log(
                f"Successfully built {image_name} for platforms: {', '.join(valid_platforms)}"
            )
            return True
        except subprocess.CalledProcessError:
            self.log(f"Failed to build {image_name}", "ERROR")
            return False

    def create_manifest(
        self, manifest_name: str, image_references: List[str], push: bool = False
    ) -> bool:
        """Create and optionally push multi-architecture manifest."""

        # Create manifest
        cmd = ["docker", "buildx", "imagetools", "create"]

        if push:
            cmd.append("--tag")
        else:
            cmd.extend(["--dry-run", "--tag"])

        cmd.append(manifest_name)
        cmd.extend(image_references)

        try:
            self.run_command(cmd)
            self.log(f"Successfully created manifest: {manifest_name}")
            return True
        except subprocess.CalledProcessError:
            self.log(f"Failed to create manifest: {manifest_name}", "ERROR")
            return False

    def inspect_multiarch_image(self, image_name: str) -> Optional[Dict]:
        """Inspect multi-architecture image and return metadata."""
        try:
            result = self.run_command(
                [
                    "docker",
                    "buildx",
                    "imagetools",
                    "inspect",
                    image_name,
                    "--format",
                    "{{json .}}",
                ],
                capture_output=True,
            )
            return json.loads(result.stdout)
        except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
            self.log(f"Failed to inspect image {image_name}: {e}", "ERROR")
            return None

    def build_from_directory(
        self,
        directory: str,
        platforms: List[str],
        registry: str,
        namespace: str,
        push: bool = False,
        build_args: Optional[Dict[str, str]] = None,
    ) -> Dict[str, bool]:
        """Build all containers in a directory structure."""
        results = {}

        # Find all Dockerfiles in the directory
        dockerfile_paths = []
        for root, _, files in os.walk(directory):
            if "Dockerfile" in files:
                dockerfile_path = os.path.join(root, "Dockerfile")
                context_path = root
                rel_path = os.path.relpath(root, directory)

                # Generate image name based on directory structure
                path_parts = rel_path.split(os.sep)
                if path_parts == ["."]:
                    image_name = os.path.basename(directory)
                else:
                    image_name = "-".join(path_parts)

                full_image_name = f"{registry}/{namespace}/{image_name}"

                dockerfile_paths.append(
                    {
                        "dockerfile": dockerfile_path,
                        "context": context_path,
                        "image": full_image_name,
                        "name": image_name,
                    }
                )

        self.log(f"Found {len(dockerfile_paths)} Dockerfiles to build")

        # Build each image
        for build_info in dockerfile_paths:
            self.log(f"Building {build_info['name']}...")
            success = self.build_multiarch_image(
                dockerfile_path=build_info["dockerfile"],
                context_path=build_info["context"],
                image_name=build_info["image"],
                platforms=platforms,
                push=push,
                build_args=build_args,
            )
            results[build_info["name"]] = success

        return results

    def generate_build_report(
        self, results: Dict[str, bool], output_file: Optional[str] = None
    ) -> None:
        """Generate build report."""
        successful = sum(1 for success in results.values() if success)
        total = len(results)

        report = {
            "summary": {
                "total_builds": total,
                "successful_builds": successful,
                "failed_builds": total - successful,
                "success_rate": (
                    f"{(successful / total * 100):.1f}%" if total > 0 else "0%"
                ),
            },
            "results": results,
            "timestamp": subprocess.run(
                ["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                capture_output=True,
                text=True,
                check=False,
            ).stdout.strip(),
        }

        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2)
            self.log(f"Build report saved to: {output_file}")

        # Print summary
        print("\n" + "=" * 50)
        print("BUILD SUMMARY")
        print("=" * 50)
        print(f"Total builds: {total}")
        print(f"Successful: {successful}")
        print(f"Failed: {total - successful}")
        print(f"Success rate: {report['summary']['success_rate']}")
        print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="Multi-architecture container build utility",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Build single container for ARM64 and AMD64
  %(prog)s build --dockerfile ./Dockerfile --context . --image myapp:latest --platforms linux/amd64,linux/arm64

  # Build all containers in directory
  %(prog)s build-all --directory ./containers --registry ghcr.io --namespace myorg --platforms linux/amd64,linux/arm64 --push

  # Setup buildx builder
  %(prog)s setup --builder-name custom-builder

  # Inspect multi-arch image
  %(prog)s inspect --image myapp:latest
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Global options
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    # Setup command
    setup_parser = subparsers.add_parser("setup", help="Setup buildx builder")
    setup_parser.add_argument(
        "--builder-name", default="multiarch-builder", help="Buildx builder name"
    )

    # Build command
    build_parser = subparsers.add_parser(
        "build", help="Build single multi-arch container"
    )
    build_parser.add_argument("--dockerfile", required=True, help="Path to Dockerfile")
    build_parser.add_argument("--context", required=True, help="Build context path")
    build_parser.add_argument("--image", required=True, help="Image name and tag")
    build_parser.add_argument(
        "--platforms",
        default="linux/amd64,linux/arm64",
        help="Comma-separated platforms",
    )
    build_parser.add_argument("--push", action="store_true", help="Push to registry")
    build_parser.add_argument(
        "--build-arg", action="append", help="Build arguments (KEY=value)"
    )
    build_parser.add_argument(
        "--label", action="append", help="Image labels (KEY=value)"
    )

    # Build-all command
    build_all_parser = subparsers.add_parser(
        "build-all", help="Build all containers in directory"
    )
    build_all_parser.add_argument(
        "--directory", required=True, help="Directory containing containers"
    )
    build_all_parser.add_argument(
        "--registry", required=True, help="Container registry"
    )
    build_all_parser.add_argument(
        "--namespace", required=True, help="Registry namespace"
    )
    build_all_parser.add_argument(
        "--platforms",
        default="linux/amd64,linux/arm64",
        help="Comma-separated platforms",
    )
    build_all_parser.add_argument(
        "--push", action="store_true", help="Push to registry"
    )
    build_all_parser.add_argument(
        "--build-arg", action="append", help="Build arguments (KEY=value)"
    )
    build_all_parser.add_argument("--report", help="Output file for build report")

    # Inspect command
    inspect_parser = subparsers.add_parser("inspect", help="Inspect multi-arch image")
    inspect_parser.add_argument("--image", required=True, help="Image name to inspect")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    builder = MultiArchBuilder(verbose=args.verbose)

    # Check prerequisites
    if not builder.check_prerequisites():
        sys.exit(1)

    if args.command == "setup":
        builder.setup_buildx_builder(args.builder_name)

    elif args.command == "build":
        builder.setup_buildx_builder()

        # Parse build args and labels
        build_args = {}
        if args.build_arg:
            for arg in args.build_arg:
                if "=" in arg:
                    key, value = arg.split("=", 1)
                    build_args[key] = value

        labels = {}
        if args.label:
            for label in args.label:
                if "=" in label:
                    key, value = label.split("=", 1)
                    labels[key] = value

        platforms = [p.strip() for p in args.platforms.split(",")]

        success = builder.build_multiarch_image(
            dockerfile_path=args.dockerfile,
            context_path=args.context,
            image_name=args.image,
            platforms=platforms,
            push=args.push,
            build_args=build_args if build_args else None,
            labels=labels if labels else None,
        )

        sys.exit(0 if success else 1)

    elif args.command == "build-all":
        builder.setup_buildx_builder()

        # Parse build args
        build_args = {}
        if args.build_arg:
            for arg in args.build_arg:
                if "=" in arg:
                    key, value = arg.split("=", 1)
                    build_args[key] = value

        platforms = [p.strip() for p in args.platforms.split(",")]

        results = builder.build_from_directory(
            directory=args.directory,
            platforms=platforms,
            registry=args.registry,
            namespace=args.namespace,
            push=args.push,
            build_args=build_args if build_args else None,
        )

        builder.generate_build_report(results, args.report)

        # Exit with error if any builds failed
        sys.exit(0 if all(results.values()) else 1)

    elif args.command == "inspect":
        metadata = builder.inspect_multiarch_image(args.image)
        if metadata:
            print(json.dumps(metadata, indent=2))
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()

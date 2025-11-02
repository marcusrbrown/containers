import argparse
import json
import os
from typing import Dict, List, Optional

# Platform-specific configurations
PLATFORM_CONFIGS = {
    "linux/amd64": {
        "arch": "amd64",
        "platform": "linux/amd64",
        "go_arch": "amd64",
        "rust_target": "x86_64-unknown-linux-gnu",
        "node_arch": "x64",
        "python_platform": "linux_x86_64",
    },
    "linux/arm64": {
        "arch": "arm64",
        "platform": "linux/arm64",
        "go_arch": "arm64",
        "rust_target": "aarch64-unknown-linux-gnu",
        "node_arch": "arm64",
        "python_platform": "linux_aarch64",
    },
    "linux/arm/v7": {
        "arch": "armv7",
        "platform": "linux/arm/v7",
        "go_arch": "arm",
        "go_arm": "7",
        "rust_target": "armv7-unknown-linux-gnueabihf",
        "node_arch": "armv7l",
        "python_platform": "linux_armv7l",
    },
}

# Package managers and their installation commands
PACKAGE_MANAGERS = {
    "alpine": {
        "update": "apk update",
        "install": "apk add --no-cache",
        "clean": "",
        "packages": {
            "build-essential": "build-base",
            "curl": "curl",
            "wget": "wget",
            "git": "git",
            "python3": "python3",
            "python3-pip": "py3-pip",
            "nodejs": "nodejs",
            "npm": "npm",
            "go": "go",
            "rust": "rust cargo",
        },
    },
    "debian": {
        "update": "apt-get update -qq",
        "install": "apt-get install -y --no-install-recommends",
        "clean": "rm -rf /var/lib/apt/lists/*",
        "packages": {
            "build-essential": "build-essential",
            "curl": "curl",
            "wget": "wget",
            "git": "git",
            "python3": "python3",
            "python3-pip": "python3-pip",
            "nodejs": "nodejs",
            "npm": "npm",
            "go": "golang-go",
            "rust": "rustc cargo",
        },
    },
    "rhel": {
        "update": "yum update -y",
        "install": "yum install -y",
        "clean": "yum clean all",
        "packages": {
            "build-essential": "gcc gcc-c++ make",
            "curl": "curl",
            "wget": "wget",
            "git": "git",
            "python3": "python3",
            "python3-pip": "python3-pip",
            "nodejs": "nodejs",
            "npm": "npm",
            "go": "golang",
            "rust": "rust cargo",
        },
    },
}


def detect_package_manager(base_image: str) -> str:
    """Detect package manager based on base image."""
    base_image_lower = base_image.lower()
    if "alpine" in base_image_lower:
        return "alpine"
    elif any(distro in base_image_lower for distro in ["debian", "ubuntu"]):
        return "debian"
    elif any(
        distro in base_image_lower
        for distro in ["rhel", "centos", "fedora", "rocky", "almalinux"]
    ):
        return "rhel"
    else:
        # Default to debian for unknown distributions
        return "debian"


def normalize_package_names(packages: List[str], package_manager: str) -> List[str]:
    """Normalize package names for specific package manager."""
    if package_manager not in PACKAGE_MANAGERS:
        return packages

    pkg_config = PACKAGE_MANAGERS[package_manager]
    normalized = []

    for package in packages:
        if package in pkg_config["packages"]:
            normalized.append(pkg_config["packages"][package])
        else:
            normalized.append(package)

    return normalized


def generate_package_installation_commands(
    packages: List[str], package_manager: str, architecture: Optional[str] = None
) -> List[str]:
    """Generate optimized package installation commands."""
    if not packages or package_manager not in PACKAGE_MANAGERS:
        return []

    pkg_config = PACKAGE_MANAGERS[package_manager]
    normalized_packages = normalize_package_names(packages, package_manager)

    commands = []

    # Architecture-specific optimizations
    if architecture and architecture in ["arm64", "armv7"]:
        # Add architecture-specific repositories or configurations if needed
        if package_manager == "debian":
            commands.append("# Architecture-specific optimizations for ARM")
            commands.append("export DEBIAN_FRONTEND=noninteractive")

    # Build installation command
    install_cmd_parts = []

    if pkg_config["update"]:
        install_cmd_parts.append(pkg_config["update"])

    if normalized_packages:
        install_cmd_parts.append(
            f"{pkg_config['install']} {' '.join(normalized_packages)}"
        )

    if pkg_config["clean"]:
        install_cmd_parts.append(pkg_config["clean"])

    # Combine into single RUN command for better layer caching
    if install_cmd_parts:
        combined_cmd = "RUN " + " && \\\n    ".join(install_cmd_parts)
        commands.append(combined_cmd)

    return commands


def generate_platform_specific_optimizations(
    platform: str, base_image: str, build_type: str = "production"
) -> List[str]:
    """Generate platform-specific optimizations."""
    lines = []

    if platform not in PLATFORM_CONFIGS:
        return lines

    config = PLATFORM_CONFIGS[platform]

    # Add platform-specific environment variables
    lines.append(f"# Platform-specific optimizations for {platform}")
    lines.append(f"ENV TARGETPLATFORM={platform}")
    lines.append(f"ENV TARGETARCH={config['arch']}")

    # Add build-specific optimizations
    if build_type == "production":
        # Production optimizations
        if config["arch"] in ["arm64", "armv7"]:
            lines.append("# ARM-specific optimizations")
            lines.append("ENV ARM_OPTIMIZATIONS=1")

        if "alpine" in base_image.lower():
            lines.append("# Alpine-specific optimizations")
            lines.append(
                "RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories"
            )

    # Add cross-compilation environment variables for common languages
    lines.append("# Cross-compilation environment variables")
    lines.append("ENV GOOS=linux")
    lines.append(f"ENV GOARCH={config['go_arch']}")

    if "go_arm" in config:
        lines.append(f"ENV GOARM={config['go_arm']}")

    lines.append(f"ENV RUST_TARGET={config['rust_target']}")
    lines.append(f"ENV NPM_CONFIG_TARGET_ARCH={config['node_arch']}")

    return lines


def generate_multiarch_dockerfile_content(
    base_image: str,
    packages: Optional[str] = None,
    env_vars: Optional[str] = None,
    platforms: Optional[List[str]] = None,
    build_type: str = "production",
    existing_dockerfile_content: Optional[str] = None,
    enable_buildkit: bool = True,
) -> str:
    """Generate multi-architecture Dockerfile content with platform-specific optimizations."""
    lines = []

    # Add syntax directive for BuildKit
    if enable_buildkit:
        lines.append("# syntax=docker/dockerfile:1.4")
        lines.append("")

    if existing_dockerfile_content:
        lines.extend(existing_dockerfile_content.split("\n"))
        return "\n".join(lines)

    # Use ARG for platform detection
    lines.append("# Build arguments for multi-architecture support")
    lines.append("ARG TARGETPLATFORM")
    lines.append("ARG TARGETOS")
    lines.append("ARG TARGETARCH")
    lines.append("ARG BUILDPLATFORM")
    lines.append("")

    # Base image with platform support
    lines.append(f"FROM --platform=$TARGETPLATFORM {base_image}")
    lines.append("")

    # Detect package manager
    package_manager = detect_package_manager(base_image)

    # Add platform-specific optimizations
    if platforms:
        for platform in platforms:
            platform_opts = generate_platform_specific_optimizations(
                platform, base_image, build_type
            )
            if platform_opts:
                lines.extend(platform_opts)
                lines.append("")

    # Install packages with platform optimizations
    if packages:
        package_list = packages.split()
        install_commands = generate_package_installation_commands(
            package_list,
            package_manager,
            None,  # Architecture detection handled in optimizations
        )
        lines.extend(install_commands)
        lines.append("")

    # Add environment variables
    if env_vars:
        lines.append("# Environment variables")
        for env_var in env_vars.split():
            if "=" in env_var:
                lines.append(f"ENV {env_var}")
            else:
                lines.append(f"ENV {env_var}=")
        lines.append("")

    # Add security best practices
    lines.extend(
        [
            "# Security best practices",
            "RUN groupadd -r appuser && useradd -r -g appuser appuser",
            "USER appuser",
            "",
            "# Health check placeholder",
            "# HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\",
            "#   CMD your-health-check-command",
            "",
            "# Default command placeholder",
            '# CMD ["your-application"]',
        ]
    )

    return "\n".join(lines)


def save_platform_build_info(
    output_dir: str, platforms: List[str], metadata: Dict
) -> None:
    """Save build information for multi-platform builds."""
    build_info = {
        "platforms": platforms,
        "metadata": metadata,
        "generated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
        "buildkit_enabled": True,
    }

    info_path = os.path.join(output_dir, ".build-info.json")
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(build_info, f, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Generate multi-architecture Dockerfile with platform-specific optimizations."
    )
    parser.add_argument(
        "--base-image", required=True, help="Base image for the Dockerfile."
    )
    parser.add_argument(
        "--packages", help="Space-separated list of packages to install."
    )
    parser.add_argument(
        "--env",
        help="Space-separated list of environment variables to set (format: KEY=value).",
    )
    parser.add_argument(
        "--platforms",
        default="linux/amd64,linux/arm64",
        help="Comma-separated list of platforms to optimize for.",
    )
    parser.add_argument(
        "--build-type",
        choices=["production", "development", "minimal"],
        default="production",
        help="Build type for optimization level.",
    )
    parser.add_argument(
        "--output-dir", default=".", help="Directory to save the generated Dockerfile."
    )
    parser.add_argument(
        "--existing-dockerfile", help="Path to an existing Dockerfile to build upon."
    )
    parser.add_argument(
        "--disable-buildkit",
        action="store_true",
        help="Disable BuildKit syntax and features.",
    )

    args = parser.parse_args()

    # Parse platforms
    platforms = [p.strip() for p in args.platforms.split(",")]

    # Read existing Dockerfile if provided
    existing_dockerfile_content = None
    if args.existing_dockerfile:
        with open(args.existing_dockerfile, "r", encoding="utf-8") as file:
            existing_dockerfile_content = file.read()

    # Generate Dockerfile content
    dockerfile_content = generate_multiarch_dockerfile_content(
        args.base_image,
        args.packages,
        args.env,
        platforms,
        args.build_type,
        existing_dockerfile_content,
        enable_buildkit=not args.disable_buildkit,
    )

    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    # Save Dockerfile
    output_path = os.path.join(args.output_dir, "Dockerfile")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(dockerfile_content)

    # Save build information
    metadata = {
        "base_image": args.base_image,
        "packages": args.packages,
        "env_vars": args.env,
        "build_type": args.build_type,
        "buildkit_enabled": not args.disable_buildkit,
    }
    save_platform_build_info(args.output_dir, platforms, metadata)

    print(
        f"Multi-architecture Dockerfile has been generated and saved to {output_path}"
    )
    print(f"Platforms supported: {', '.join(platforms)}")
    print(
        f"Build information saved to {os.path.join(args.output_dir, '.build-info.json')}"
    )


if __name__ == "__main__":
    main()

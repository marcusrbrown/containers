import argparse
import os

def generate_dockerfile_content(base_image, packages, env_vars, architecture=None, os_type=None, existing_dockerfile_content=None):
    lines = []
    if existing_dockerfile_content:
        lines.extend(existing_dockerfile_content.split("\n"))
    else:
        base_image_line = f"FROM {base_image}"
        if architecture:
            base_image_line += f" AS build-{architecture}"
        lines.append(base_image_line)

    if packages:
        package_install_cmd = "RUN "
        if "alpine" in base_image or os_type == "alpine":
            package_install_cmd += f"apk add --no-cache {packages}"
        else:
            package_install_cmd += f"apt-get update && apt-get install -y {packages}"
        lines.append(package_install_cmd)
    
    if env_vars:
        for env_var in env_vars.split(" "):
            lines.append(f"ENV {env_var}")

    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Dockerfile.")
    parser.add_argument("--base-image", required=True, help="Base image for the Dockerfile.")
    parser.add_argument("--packages", help="Space-separated list of packages to install.")
    parser.add_argument("--env", help="Space-separated list of environment variables to set.")
    parser.add_argument("--architecture", help="CPU architecture for the Docker image.")
    parser.add_argument("--os-type", help="Operating system type for the Docker image.")
    parser.add_argument("--output-dir", required=True, help="Directory to save the generated Dockerfile.")
    parser.add_argument("--existing-dockerfile", help="Path to an existing Dockerfile to build upon.")
    args = parser.parse_args()

    existing_dockerfile_content = None
    if args.existing_dockerfile:
        with open(args.existing_dockerfile, "r") as file:
            existing_dockerfile_content = file.read()

    dockerfile_content = generate_dockerfile_content(args.base_image, args.packages, args.env, args.architecture, args.os_type, existing_dockerfile_content)

    output_path = os.path.join(args.output_dir, "Dockerfile")
    with open(output_path, "w") as file:
        file.write(dockerfile_content)

    print(f"Dockerfile has been generated and saved to {output_path}.")

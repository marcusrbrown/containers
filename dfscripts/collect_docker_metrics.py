import os
import time
import yaml
import argparse
import requests

def identify_target_dockerfiles(repo_path):
    dockerfiles = []
    for root, _, files in os.walk(repo_path):
        if 'Dockerfile' in files:
            dockerfiles.append(os.path.join(root, 'Dockerfile'))
    return dockerfiles

def collect_build_metrics(dockerfile_path):
    start_time = time.time()
    os.system(f"docker build -t test_image -f {dockerfile_path} .")
    end_time = time.time()
    build_time = end_time - start_time
    return {'build_time': build_time}

def collect_image_metrics(image_name):
    image_data = os.popen(f"docker image inspect {image_name}").read()
    size = image_data.split('"Size": ')[1].split(",")[0]
    return {'image_size': size}

def collect_usage_metrics(image_name, registry):
    if registry == "dockerhub":
        url = f"https://hub.docker.com/v2/repositories/{image_name}"
    elif registry == "github":
        url = f"https://api.github.com/user/packages/container/{image_name}"
    else:
        return {}
    response = requests.get(url)
    data = response.json()
    return {'pull_count': data.get('pull_count', 0)}

def main():
    parser = argparse.ArgumentParser(description='Collect Docker metrics')
    parser.add_argument('--registry', choices=['dockerhub', 'github'], default='dockerhub',
                        help='Select the registry for collecting usage metrics')
    args = parser.parse_args()

    repo_path = '.'  # Replace with actual repo path
    dockerfiles = identify_target_dockerfiles(repo_path)

    all_metrics = {}
    for dockerfile in dockerfiles:
        build_metrics = collect_build_metrics(dockerfile)
        image_metrics = collect_image_metrics('test_image')
        usage_metrics = collect_usage_metrics('test_image', args.registry)
        
        all_metrics[dockerfile] = {
            'build_metrics': build_metrics,
            'image_metrics': image_metrics,
            'usage_metrics': usage_metrics
        }

    with open('collected_metrics.yaml', 'w') as file:
        yaml.dump(all_metrics, file)

if __name__ == '__main__':
    main()

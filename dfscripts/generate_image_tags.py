import os
import json

def identify_target_dockerfiles(repo_path):
    dockerfiles = []
    for root, _, files in os.walk(repo_path):
        if 'Dockerfile' in files:
            dockerfiles.append(os.path.join(root, 'Dockerfile'))
    return dockerfiles

def extract_metadata(dockerfile_path):
    metadata = {}
    with open(dockerfile_path, 'r') as file:
        for line in file:
            if line.startswith('FROM'):
                metadata['base_image'] = line.split()[1]
            if line.startswith('LABEL'):
                label_data = line[6:].strip()
                key, value = label_data.split('=', 1)
                metadata[key] = value
    return metadata

def generate_tags(metadata):
    tags = []
    base_image = metadata.get('base_image', 'unknown')
    version = metadata.get('version', 'latest')
    tags.append(f"{base_image.replace(':', '-')}-{version}")
    return tags

def main():
    repo_path = '.'  # Replace with actual repo path
    dockerfiles = identify_target_dockerfiles(repo_path)
    
    all_tags = {}
    for dockerfile in dockerfiles:
        metadata = extract_metadata(dockerfile)
        tags = generate_tags(metadata)
        all_tags[dockerfile] = tags

    with open('generated_tags.json', 'w') as file:
        json.dump(all_tags, file, indent=4)

if __name__ == '__main__':
    main()

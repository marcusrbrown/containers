import os
import re

def extract_python_docstrings(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    docstrings = re.findall(r'"""(.*?)"""', content, re.DOTALL)
    return '\n'.join(docstrings)

def main():
    # Identify all Markdown and Python files
    markdown_files = []
    python_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
            elif file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    # Extract Python docstrings and generate Markdown documentation
    python_docs = {}
    for python_file in python_files:
        doc_content = extract_python_docstrings(python_file)
        python_docs[python_file] = doc_content

    # Compile all documentation
    compiled_docs_content = ""
    for md_file in markdown_files:
        with open(md_file, "r") as file:
            compiled_docs_content += file.read() + "\n\n---\n\n"
    for doc_content in python_docs.values():
        compiled_docs_content += doc_content + "\n\n---\n\n"

    # Save the compiled documentation as a Markdown file
    compiled_docs_md_path = "./docs/COMPILED_DOCS.md"
    os.makedirs("./docs", exist_ok=True)
    with open(compiled_docs_md_path, "w") as file:
        file.write(compiled_docs_content)

if __name__ == "__main__":
    main()

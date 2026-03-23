import os
import json

def generate_metadata(root_dir="."):
    """
    Recursively walks through directories to find PDF files and generates a JSON tree.
    Skips hidden files, system files, and development files.
    """
    skip_names = {'.git', '.github', 'generate_metadata.py', 'index.html', 'findings.md', 'task_plan.md', 'progress.md', '.DS_Store', 'metadata.json', 'node_modules'}

    def build_tree(path):
        name = os.path.basename(path) if path != "." else "root"

        # If it's a directory
        if os.path.isdir(path):
            contents = []
            for item in sorted(os.listdir(path)):
                if item in skip_names or item.startswith('.'):
                    continue

                child_path = os.path.join(path, item)
                child_node = build_tree(child_path)
                if child_node:
                    contents.append(child_node)

            # Only return directory if it has contents
            if contents:
                return {
                    "name": name if name != "root" else "Activity Books",
                    "type": "directory",
                    "path": path if path != "." else "",
                    "contents": contents
                }
            return None

        # If it's a file
        elif path.lower().endswith('.pdf'):
            return {
                "name": name,
                "type": "file",
                "path": path,
                "size": os.path.getsize(path)
            }
        return None

    return build_tree(root_dir)

if __name__ == "__main__":
    data = generate_metadata()
    with open("metadata.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("metadata.json (tree structure) generated successfully.")

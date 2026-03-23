import os
import json
import mimetypes

def generate_metadata(root_dir="."):
    """
    Recursively walks through directories to find PDF files and generates a JSON map.
    Skips hidden files and directories (starting with '.').
    """
    metadata = {
        "title": "Activity Books",
        "description": "Educational activity books for all ages.",
        "last_updated": None, # Will be set by GitHub Actions
        "files": []
    }

    # Top-level standalone PDFs and directories
    for item in sorted(os.listdir(root_dir)):
        if item.startswith('.'):
            continue

        full_path = os.path.join(root_dir, item)

        if os.path.isdir(full_path):
            directory_info = {
                "name": item,
                "type": "directory",
                "contents": []
            }
            # Recursively find PDFs inside the directory
            for sub_item in sorted(os.listdir(full_path)):
                if sub_item.startswith('.'):
                    continue
                sub_full_path = os.path.join(full_path, sub_item)
                if os.path.isfile(sub_full_path) and sub_item.lower().endswith('.pdf'):
                    directory_info["contents"].append({
                        "name": sub_item,
                        "type": "file",
                        "size": os.path.getsize(sub_full_path),
                        "path": os.path.join(item, sub_item)
                    })
            if directory_info["contents"]:
                metadata["files"].append(directory_info)

        elif os.path.isfile(full_path) and item.lower().endswith('.pdf'):
            metadata["files"].append({
                "name": item,
                "type": "file",
                "size": os.path.getsize(full_path),
                "path": item
            })

    return metadata

if __name__ == "__main__":
    data = generate_metadata()
    with open("metadata.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("metadata.json generated successfully.")

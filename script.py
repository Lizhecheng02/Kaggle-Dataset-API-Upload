import os
import json
import subprocess


def upload_to_kaggle(dataset_folder, title, username, license_name="CC0-1.0"):
    metadata_path = os.path.join(dataset_folder, "dataset-metadata.json")
    metadata = {
        "title": title,
        "id": f"{username}/{title.replace(' ', '-').lower()}",
        "licenses": [{"name": license_name}]
    }
    with open(metadata_path, "w") as f:
        json.dump(metadata, f)

    try:
        subprocess.run(["kaggle", "datasets", "create", "-p", dataset_folder], check=True)
        print("Dataset uploaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


upload_to_kaggle(
    dataset_folder="",
    title="",
    username=""
)

import os
import json
import subprocess


def contains_subdirectory(directory):
    return any(os.path.isdir(os.path.join(directory, item)) for item in os.listdir(directory))


def upload_to_kaggle(dataset_folder, title, username, license_name="CC0-1.0"):
    metadata_path = os.path.join(dataset_folder, "dataset-metadata.json")
    metadata = {
        "title": title,
        "id": f"{username}/{title.replace(' ', '-').lower()}",
        "licenses": [{"name": license_name}]
    }
    with open(metadata_path, "w") as f:
        json.dump(metadata, f)

    if contains_subdirectory(dataset_folder):
        print("Zipping the dataset folder...")
        try:
            subprocess.run(["kaggle", "datasets", "create", "-p", dataset_folder, "--dir-mode", "zip"], check=True)
            print("Dataset uploaded successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    else:
        print("Uploading the dataset folder...")
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

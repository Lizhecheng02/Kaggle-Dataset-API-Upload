## Step-by-Step Guide: Uploading Your Dataset to Kaggle Using the API

### 1. Set Up Kaggle API Key

- Log in to Kaggle.
- Your username is the name displayed in your Kaggle profile link, e.g., `https://www.kaggle.com/xxx`.
- Click on your profile avatar in the upper right corner and select "Settings".
- Scroll down to find the API section and click "Create New API Token".
- The downloaded `kaggle.json` file contains your API key.

### 2. Install and Configure the Kaggle CLI

- Install the `kaggle` Python package on your server:

```bash
pip install kaggle
```

- Verify the installation:

```bash
kaggle --version
```

- Set up the `kaggle.json` file for use:

```bash
mkdir -p ~/.kaggle
mv ./kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

**Alternatively, you can directly enter the following commands in the terminal:**

- Use the ``export`` method:

```bash
export KAGGLE_USERNAME="YOUR_KAGGLE_USERNAME"
export KAGGLE_KEY="YOUR_KAGGLE_API_KEY"
```

### 3. Prepare Data for Upload

Organize the data you want to upload into a folder. The dataset folder must contain at least the following:

- At least one data file (e.g., `.csv`, `.xlsx`, `.json`).
- A `dataset-metadata.json` file defining the metadata for the dataset.

**Here, I provide an example where the `./dataset` folder contains all the data to be uploaded.**

An example of a `dataset-metadata.json` file can be found in this GitHub repository.

- ``title``: Name of your dataset.
- ``id``: Path to your dataset, in the format `username/dataset-name`.
- ``licenses``: License type.

### 4. Upload Data to Kaggle

Here are two different scenarios:

- If there are no subfolders under ``./dataset``.

Run the following command to upload the dataset to Kaggle:

```bash
kaggle datasets create -p ./dataset
```

Here, the string following `-p` specifies the directory that contains the data files and the `dataset-metadata.json` file.

To update an existing dataset, use the following command:

```bash
kaggle datasets version -p ./dataset -m "update message"
```

- If there are subfolders under ``./dataset``.

Run the following command to upload the dataset to Kaggle:

```bash
kaggle datasets create -p ./dataset --dir-mode zip
```

To update an existing dataset, use the following command:

```bash
kaggle datasets version -p ./dataset --dir-mode zip -m "update message"
```

### 5. Automated Upload Script

Run the following command and input your information into the code after completing **Step 2**.

```bash
python script.py
```

### 6. Check Dataset

You will receive a link to your dataset, which will default to **private** when opened (ensuring your data remains secure).

### Questions

You are welcome to discuss any issues you encounter while running this GitHub repository.


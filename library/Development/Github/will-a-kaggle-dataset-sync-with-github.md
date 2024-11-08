---
title: "Will a Kaggle dataset sync with Github"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


No, mirroring your GitHub repository onto Kaggle does **not** automatically keep the dataset in sync with the repository. Once you upload your dataset to Kaggle, it becomes a separate entity from your GitHub repository, and any updates or changes you make in the GitHub repo will **not** automatically reflect on Kaggle.

### Keeping Your Kaggle Dataset in Sync with GitHub

To keep the dataset in sync, you'll need to manually update the Kaggle dataset whenever you make changes to the GitHub repository. Here’s how you can do it:

### 1. **Manual Updates via Kaggle CLI**
   - You can update the dataset on Kaggle whenever you push changes to GitHub by using the **Kaggle CLI**.
   - First, ensure that the changes are committed and pushed to your GitHub repo.
   - Then, run the following command to update the Kaggle dataset with the new files:
     ```bash
     kaggle datasets version -p /path/to/local/repo -m "Updated data from GitHub"
     ```
   - This command will upload the updated files from your local directory to Kaggle and create a new version of the dataset.

### 2. **Automation via GitHub Actions (Optional)**
   If you want to automate the process of keeping Kaggle in sync with your GitHub repository, you can set up **GitHub Actions** to automatically update the Kaggle dataset whenever you push new changes to the GitHub repository.

   Example steps:
   - Set up a **GitHub Action** workflow that triggers on every push to your repository.
   - The workflow would use the **Kaggle API** to update the Kaggle dataset with new data.
   - This setup ensures the Kaggle dataset stays up-to-date with the latest changes in your GitHub repository without needing manual intervention.

Would you like guidance on setting up GitHub Actions for automatic updates?
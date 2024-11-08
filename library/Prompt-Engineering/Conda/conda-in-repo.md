---
title: "Setting up a Conda virtual environment within an (existing) Github repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



## Creating the Environment

1. Navigate to your project directory in the terminal:

```bash
cd path/to/your/github/repo
```

2. Create a new Conda environment with Python and Pandas:

```bash
conda create -n your_project_name python pandas
```

## Activating and Verifying

After creation, activate your new environment:

```bash
conda activate your_project_name
```

## Managing Dependencies

To help others reproduce your environment, create an environment.yml file:

```bash
conda env export > environment.yml
```

Add this file to your repository so others can recreate your environment with:

```bash
conda env create -f environment.yml
```

## Git Configuration

Add the following to your .gitignore file to exclude environment-specific files:

```
# Conda environment files
/envs/
```

## Best Practices

- Install all required packages at once to avoid dependency conflicts\[1]
- If you need packages only available via pip, install pip within your conda environment first:

````bash
conda install pip
pip install package_name
```[2]

- To update your environment later, modify environment.yml and run:
```bash
conda env update --file environment.yml --prune
```[1]

This approach allows you to add a Conda environment to your existing project while maintaining proper version control and making it easy for others to reproduce your development environment[1][4].

Citations:
[1] https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
[2] https://pandas.pydata.org/pandas-docs/version/2.0.0/getting_started/install.html
[3] https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/installing-with-conda.html
[4] https://betterdatascience.com/how-to-install-pandas/
[5] https://docs.anaconda.com/working-with-conda/packages/install-packages/
````

<br>

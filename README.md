# MLOps Project Setup Guide

This document outlines the initial steps required to set up an MLOps project. The process includes creating the project structure, preparing the dataset, and initializing version control and data versioning tools.

---

## 1. Create the Project Template

Start by creating the project directory and organizing the initial folder structure for your machine learning pipeline.

Example structure:

```
project_name/
│
├── data_given/
│   └── data.csv
│
├── src/
├── notebooks/
├── configs/
├── README.md
└── requirements.txt
```

---

## 2. Prepare the Dataset

Place the dataset inside the `data_given/` directory.

Example:

```
data_given/data.csv
```

This dataset will later be tracked using **DVC (Data Version Control)**.

---

## 3. Initialize Git Repository

Initialize Git to start version control for the project.

```bash
git init
```

---

## 4. Initialize DVC

DVC is used to track datasets and machine learning artifacts.

```bash
dvc init
```

---

## 5. Track the Dataset with DVC

Add the dataset to DVC tracking.

```bash
dvc add data_given/data.csv
```

This command will create:

- `data.csv.dvc`
- Updates to `.gitignore`

---

## 6. Commit the Initial Project Setup

Add the project files and make the first commit.

```bash
git add .
git commit -m "Initial project setup"
```

---

## 7. Update README or Project Files

Whenever documentation or files are updated, commit the changes.

```bash
git add .
git commit -m "Update README"
```

---

## Summary

The basic workflow for initializing an MLOps project is:

1. Create project template  
2. Add dataset  
3. Initialize Git  
4. Initialize DVC  
5. Track dataset with DVC  
6. Commit project files  

This setup ensures both **code versioning (Git)** and **data versioning (DVC)** are properly managed.

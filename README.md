# Master Thesis - Data Exploration and Modeling

This repository contains the two main notebooks used for data analysis and predictive modeling in the context of volcanic activity monitoring at Rincon de la Vieja:

- `DataExploration.ipynb`
- `Model.ipynb`

These notebooks form the core workflow for exploratory data analysis and machine learning model development used in the thesis project.

---

## Overview

The project focuses on analyzing multiple time-series datasets and geophysical measurements related to volcanic activity, including:

- eruption and event-related data,
- acoustic and vibration data (VRBA, RSAM, DSAR),
- precipitation data,
- lahar-related records,
- environmental time-series and volcanic indicators.

The goal is to understand the relationships between these variables, identify the most relevant signals, and build models capable of classifying or detecting events from the available features.

---

## 1. Notebook: DataExploration.ipynb

### Purpose

This notebook is dedicated to data exploration, validation, and preparation. It serves as the analytical foundation before the modeling stage.

### Main tasks

- loading datasets from the `MSc_Bryan_Rincon/Datasets` folder,
- converting time columns to a consistent format,
- setting time indices for time-series analysis,
- inspecting dataset structure and data types,
- removing irrelevant columns,
- analyzing distributions, trends, and outliers,
- visualizing time-series behavior,
- exploring correlations and relationships between variables,
- preparing the dataset for the modeling pipeline.

### Typical workflow

1. Import required Python libraries.
2. Load the reference datasets.
3. Normalize date formats and time indices.
4. Check data quality (types, missing values, dimensions).
5. Analyze temporal patterns and signal behavior.
6. Select relevant variables for the study.
7. Prepare the data for the model-building phase.

### Key value

- helps understand the structure of the data,
- supports anomaly detection and signal identification,
- provides a global view of variable interactions,
- prepares the dataset for downstream modeling.

---

## 2. Notebook: Model.ipynb

### Purpose

This notebook builds on the exploration phase to train and evaluate machine learning models for event classification or detection tasks.

### Main tasks

- feature preparation from cleaned data,
- construction of labels or target variables associated with events,
- train/test split and data partitioning,
- feature selection,
- model training,
- hyperparameter optimization,
- performance evaluation using metrics such as:
  - precision,
  - recall,
  - F1-score,
  - accuracy,
  - confusion matrix,
  - F-beta score.

### Models and methods used

Based on the code, this notebook includes common machine learning and feature-selection tools such as:

- scikit-learn,
- RandomForest,
- linear regression,
- stratified cross-validation,
- randomized hyperparameter search,
- feature importance-based selection,
- multiclass and binary classification evaluation.

The notebook is designed to compare several configurations and assess the robustness of predictions under the available data conditions.

---

## 3. Recommended workflow

To use the notebooks correctly, it is recommended to follow this order:

1. Open `DataExploration.ipynb`
2. Inspect the data quality and structure
3. Identify useful variables and required transformations
4. Open `Model.ipynb`
5. Reuse the prepared data and selected features
6. Train and evaluate the models
7. Compare results and refine hyperparameters if needed

---

## 4. Project structure

The repository is organized as follows:

- `DataExploration.ipynb` — data exploration and preparation
- `Model.ipynb` — model training and evaluation
- `MSc_Bryan_Rincon/` — study data and project resources
- `all/` — auxiliary analyses and intermediate results
- `Report/` — thesis documents and reporting materials

---

## 5. Main dependencies

The notebooks rely on several Python libraries, including:

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- scikit-learn
- fasteda
- openTSNE
- ruptures
- tsfresh
- joblib

A properly configured Python environment with these dependencies is recommended.

---

## 6. Important notes

- The notebooks assume execution from the project root or with correctly configured relative paths.
- The data is located in the `MSc_Bryan_Rincon/Datasets` folder, and file paths are often defined explicitly at the beginning of the notebooks.
- These notebooks are designed as a research workflow and may require minor adjustments depending on the environment or dataset version.

---

## 7. Summary

- `DataExploration.ipynb`: data cleaning, visualization, and feature preparation.
- `Model.ipynb`: model training, validation, and performance evaluation.

Together, these two notebooks form the analytical core of the project and enable the transition from raw data to an actionable predictive workflow.

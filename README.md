<div align="center">
      <h1><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="400px" style="vertical-align: middle;" />
        <br/>Python WorkSpace</h1>
     </div>
<p align="center"> <a href="https://www.linkedin.com/in/chiraggupta1706" target="_blank"><img alt="" src="https://img.shields.io/badge/LinkedIn-0077B5?style=medium&logo=linkedin&logoColor=white" style="vertical-align:center" /></a> </p>

# Description
Welcome to the Python Projects Repository. This repository showcases the Python projects I have developed and am currently working on. It will be regularly updated with new projects, improvements, and enhancements. You are encouraged to clone the repository and utilize the code for learning, reference, or development purposes.

# Features
The repository features a diverse collection of Python projects, each demonstrating various aspects of application development. These projects serve as practical examples, offering valuable insights for learning, development, or as a reference to enhance and accelerate your own projects.

Key Features:

• Comprehensive Projects: The repository contains a diverse range of projects demonstrating various Python functionalities.

• Free to Use: All code in this repository is available for you to clone and use freely.

# Tech Used
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white) ![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Sever-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-F4F8D3?style=for-the-badge&logo=FastAPI&logoColor=019486E) ![SQLite](https://img.shields.io/badge/SQLite-222222?style=for-the-badge&logo=SQLite&logoColor=B6B6B6E) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-98D2C0?style=for-the-badge&logo=SQLAlchemy&logoColor=000000)
 
# Getting Started

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Project Setup](#project-setup)
* [Next Steps](#next-steps)
* [FastAPI](#fastapi)

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python:** Version 3.x is recommended.  Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **Git:** A version control system. Download from: [https://git-scm.com/downloads](https://git-scm.com/downloads)
* **pip:** Python's package installer (usually included with Python).

## Installation

1.  **Clone the Repository:**

    Open your terminal or command prompt and clone the repository:

    ```bash
    git clone https://github.com/chirag876/PythonWorkSpace.git
    cd PythonWorkSpace
    ```

## Project Setup

1.  **Create a Virtual Environment:**

    It is highly recommended to use a virtual environment to isolate project dependencies.

    ```bash
    python -m venv myenv
    ```

2.  **Activate the Virtual Environment:**

    Activate the virtual environment:

    * **macOS and Linux:**

        ```bash
        source myenv/bin/activate
        ```
    * **Windows:**

        ```bash
        myenv\Scripts\activate
        ```

    You should see `(myenv)` at the beginning of your terminal prompt.

3.  **Install Dependencies (if applicable):**

    If a project has a `requirements.txt` file, navigate to the project directory and install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Next Steps
After completing these steps, you're ready to explore the projects within this repository.  Refer to individual project directories for specific instructions.

# Firebase Project Setup Guide (Backend Integration)

Follow this step-by-step guide to set up your Firebase project with Authentication, Firestore, and Realtime Database. This guide is tailored for backend development using Python.

---

## Table of Contents

1. [Create a Firebase Project](#step-1-create-a-firebase-project)
2. [Set Up Firebase Features](#step-2-set-up-build-features)
   - [Authentication Setup](#step-21-authentication-setup)
   - [Firestore Database Setup](#step-22-firestore-database-setup)
   - [Realtime Database Setup](#step-23-realtime-database-setup)
3. [Register Your App](#step-3-register-your-app)
4. [Generate Firebase Admin SDK Credentials](#step-4-generate-firebase-admin-sdk-credentials)

---

## Step 1: Create a Firebase Project

1. **Go to Firebase Console:**
   - Open your browser and navigate to the [Firebase Console](https://console.firebase.google.com/).

2. **Create New Project:**
   - Click on **Go to Console** (top-right corner).
   - Then click **Get Started with a Firebase Project**.

3. **Enter Project Name:**
   - Enter a unique name for your project, e.g., `Music App`.

4. **Finalize Project Creation:**
   - A unique project identifier will be automatically generated.
   - Click **Continue** through the prompts and then click **Create Project**.
   - Wait a few seconds while Firebase creates your project.

5. **Open Dashboard:**
   - Once the project is created, click **Continue** to open your Firebase project dashboard.

---

## Step 2: Set Up Build Features

Now, let’s configure Authentication, Firestore, and Realtime Database.

### Step 2.1: Authentication Setup

1. **Go to Authentication:**
   - From the left-hand menu, click on **Authentication** under the **Build** section.

2. **Enable Email/Password Sign-in:**
   - Click **Get Started**.
   - Under the **Sign-in method** tab, select **Email/Password**.
   - Enable **Email/Password** and click **Save**.

3. **Authentication is Now Configured**.

### Step 2.2: Firestore Database Setup

1. **Go to Firestore Database:**
   - From the left-hand menu, select **Firestore Database** under **Build**.

2. **Create Database:**
   - Click **Create Database**.
   - Choose the default location for your database and click **Next**.
   - Select **Start in test mode** and click **Enable**.

3. **Firestore Database is Now Configured**.

### Step 2.3: Realtime Database Setup

1. **Go to Realtime Database:**
   - Select **Realtime Database** from the **Build** section on the left.

2. **Create Database:**
   - Click **Create Database**.
   - Choose the default location and click **Next**.
   - Select **Start in test mode** and click **Enable**.

3. **Realtime Database is Now Configured**.

---

## Step 3: Register Your App

1. **Go to Project Settings:**
   - Click the **Settings** icon next to **Project Overview** in the Firebase Console.

2. **Navigate to "Your Apps" Section:**
   - Scroll down to the **Your Apps** section.

3. **Register Web App:**
   - Click the **Code icon (</>)** to register a new **Web app**.
   - Enter an **App nickname** of your choice.
   - Click **Register app**.

4. **Skip Firebase SDK Setup:**
   - Skip the **Firebase SDK setup** for now (since this guide is for backend integration).
   - Click **Continue to Console**.

   Your Firebase app is now registered.

---

## Step 4: Generate Firebase Admin SDK Credentials

1. **Go to Service Accounts:**
   - In **Project Settings**, navigate to the **Service Accounts** tab.

2. **Choose Backend Language (Python):**
   - Choose **Python** as your backend language.

3. **Generate New Private Key:**
   - Click **Generate new private key**.
   - Confirm by clicking **Generate Key**.

4. **Download the Credentials File:**
   - A **.json** file will be downloaded to your local machine.
   - **Store this file securely** as it contains sensitive credentials.

   > **Important:** Do **not** share this file with anyone.

---

## Conclusion

You have successfully set up your Firebase project with Authentication, Firestore, and Realtime Database! Now you're ready to integrate these services into your backend code using the Firebase Admin SDK.

---

### Next Steps:

- Install the Firebase Admin SDK for Python.
- Start integrating Firebase services into your backend code.

---
# 🧠 Mostly AI Challenge - [Flat Data Synthetic Generation](https://github.com/chirag876/PythonWorkSpace/tree/main/SyntheticDataProject)
## 🚀 Challenge Overview

The **Flat Data Challenge** by Mostly AI is focused on generating high-quality synthetic tabular data that closely mimics the structure and patterns of a real dataset.

- **Dataset**: `flat-training.csv`
- **Records**: 100,000
- **Columns**: 80 total → 60 numeric, 20 categorical
- **Goal**: Generate a synthetic dataset that maintains:
  - **Data utility** (preserves useful patterns)
  - **Privacy** (doesn’t leak individual records)
  - **Statistical fidelity** (distributions match well)

**Evaluation Metrics**:
- Overall Accuracy  
- DCR (Distance to Closest Record)  
- NNDR (Nearest Neighbor Distance Ratio)

---

## 📈 My Approach

| Step | Description |
|------|-------------|
| 1. Data Acquisition | Downloaded the `flat-training.csv` file and verified the shape and structure. |
| 2. Data Exploration | Performed exploratory data analysis using `pandas`, `matplotlib`, and `jupyter`. Checked distributions, missing values, and data types. |
| 3. Model Selection | Selected `CTGAN` from the `sdv` library, optimized for mixed-type tabular data. |
| 4. Model Training | Trained the `CTGAN` model on the dataset. Tuned parameters like `epochs` for better performance. |
| 5. Synthetic Data Generation | Generated a new synthetic dataset using the trained model with the same schema and row count. |
| 6. Visualizing Distribution Comparison of Real and Synthetic Data | Compared distributions of real and synthetic data for the first five columns using overlaid histograms.|
| 7. Generating a Synthetic Data Quality Report | Generated a quality report comparing real and synthetic datasets, saving it as formatted text and Html files.|
| 8. Submission Preparation | Exported the synthetic data to CSV format per submission guidelines and uploaded it to the Mostly AI platform. |

---

## 📦 Libraries & Tools Used

Installed via pip:

```bash
pip install pandas numpy scikit-learn matplotlib jupyter
pip install sdv
````

| Library      | Purpose                               |
| ------------ | ------------------------------------- |
| pandas       | Data manipulation and cleaning        |
| numpy        | Numerical operations                  |
| matplotlib   | Data visualization                    |
| scikit-learn | Preprocessing (if needed)             |
| jupyter      | Interactive development and analysis  |
| sdv          | Synthetic data generation using CTGAN |

---

## 🧠 Sample Insights from EDA

* Numeric columns had varying scales — **normalization wasn’t strictly needed** due to CTGAN’s internal handling.
* Categorical columns had **distinct and non-overlapping values**, helping the model learn categories effectively.
* Data was **clean and had no missing values**, so **no imputation** was required.

---

## 💡 What I Learned

* `CTGAN` is **highly capable** when working with complex tabular data including both numerical and categorical features.
* Simple EDA using `pandas` and `matplotlib` provides powerful insights to shape training decisions.
* The quality of synthetic data depends on how well the generator captures **statistical patterns** in the original data.
* **Privacy metrics** like DCR and NNDR are more advanced than just comparing basic feature distributions.
---
## License

This project is licensed under the [MIT License](./LICENSE).  
© 2025 Chirag Gupta. Please credit if reused.


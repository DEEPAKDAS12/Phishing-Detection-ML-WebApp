# Phishing Detection Web Application

## Overview
This project is a **machine learning-based web application** that detects phishing websites. It utilizes **ML models** to classify URLs as **phishing or legitimate** and provides a user-friendly interface for checking website safety.

## Features
- **Web-based Interface**: Simple UI for checking URLs.
- **Machine Learning Model**: Uses a **Voting Classifier** trained on phishing and legitimate website data.
- **Vectorization**: Converts URL text data into numerical format using **TF-IDF Vectorizer**.
- **Git LFS Support**: Model files are tracked using **Git Large File Storage (LFS)**.
- **Implementation in Google Colab**: Jupyter Notebook for model training and evaluation.
- **Project Documentation**: Includes implementation details and output screenshots.

## Tech Stack
- **Backend**: Python (Flask)
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Frontend**: HTML, CSS
- **Model Storage**: Git LFS

## Project Structure
```
├── models/                     # Trained ML models (tracked using Git LFS)
├── templates/                  # HTML templates for UI
├── vectorizer/                 # Vectorization models
├── app.py                      # Main Flask application
├── requirements.txt            # Dependencies for the project
├── Implementation_collab-notebook.ipynb  # Colab Notebook for model training
├── Output_Screens_Project.docx  # Screenshots of app outputs
├── Project_Documentation.docx   # Detailed project documentation
├── .gitattributes               # Tracking large files with Git LFS
└── README.md                    # Project overview and instructions
```

## Setup and Installation
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/DEEPAKDAS12/Phishing-Detection-ML-WebApp.git
   ```
2. **Navigate to the Project Folder**:
   ```sh
   cd Phishing-Detection-ML-WebApp
   ```
3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Application**:
   ```sh
   python app.py
   ```
5. **Access the Web App**:
   Open `http://127.0.0.1:5000/` in a browser.

## Model Training (Google Colab)
- The model training is done using **Google Colab**.
- You can find the **implementation notebook** in `Implementation_collab-notebook.ipynb`.
- To retrain the model, upload the dataset and run the notebook cells step by step.

## Screenshots
- The `Output_Screens_Project.docx` file contains screenshots demonstrating the app’s functionality.

## Documentation
- Detailed explanation of the project, methodology, and implementation is available in `Project_Documentation.docx`.

## Contributing
- Fork the repository and create a new branch.
- Make your changes and submit a pull request.

Heart Disease Prediction

<br><br>

Table of Contents

1. Project Overview
2. Technologies Used
3. Dataset
4. Features
5. Installation and Setup
6. Usage
7. Model Training
8. Results

<br>

1. Project Overview :-
- This machine learning project focuses on predicting the likelihood of heart disease in individuals based on medical data. By analyzing factors such as age, blood pressure, cholesterol levels, and other key health metrics, the model classifies whether an individual is at risk of heart disease. The goal of the project is to assist healthcare providers with early diagnosis, enabling better preventive measures and personalized treatment.


2. Technologies Used
- Programming Language : Python
- Libraries/Frameworks :
  - Pandas
  - NumPy
  - Scikit-learn
  - XGBoost
  - Matplotlib / Seaborn
  - Jupyter Notebook and Google colab (for experiments)


3. Dataset
- Size : 180 rows, 14 features
- Description : The dataset includes various health-related features that are used to predict heart disease risk. These features include age, sex, blood pressure, cholesterol levels, maximum heart rate, and more. The target variable indicates whether or not the individual has heart disease.


4. Features
- Age : Age of the patient
- Sex : Gender of the patient
- Chest Pain Type : Type of chest pain experienced
- Blood Pressure : Systolic blood pressure
- Cholesterol : Cholesterol levels in the blood
- Blood Sugar : Whether fasting blood sugar > 120 mg/dl
- ECG : Electrocardiographic results
- Max Heart Rate : Maximum heart rate achieved
- Exercise Angina : Whether the patient experiences exercise-induced angina
- Oldpeak : Depression induced by exercise relative to rest
- Slope : Slope of the peak exercise ST segment
- CA : Number of major vessels colored by fluoroscopy
- Thalassemia : Thalassemia status (normal, fixed defect, reversible defect)
- Target : 1 if the individual has heart disease, 0 otherwise

5. Installation and Setup
- Clone this repository :
  - git clone https://github.com/Ramrajkrushn25/Heart_Disease_Prediction.git
- Navigate to the project folder :
  - cd Heart_Disease_Prediction


6. Usage
- Run the Jupyter notebook to explore the data, train models, and generate prediction:
  -  jupyter notebook
- The notebook is divided into the following sections :
  - Data Preprocessing : Cleans and prepares the data for training.
  - Model Training : Train and evaluate various machine learning models.
  - Model Evaluation : Evaluate the model's performance using metrics like accuracy, precision, recall, etc.


7. Model Training
- Models Used :
  - Logistic Regression
  - Support Vector Classifier
  - Random Forest
  - Naive Bayes
  - Gradient Boosting
  - KNN
 
- Evaluation Metrics :
  - Accuracy
  - Precision, Recall, F1-Score
  - AUC-ROC


8. Results
- The best model Random Forest achieved an accuracy of 86% on the test dataset.
- The model helps healthcare professionals assess the risk of heart disease in individuals, enabling timely interventions and preventive measures.

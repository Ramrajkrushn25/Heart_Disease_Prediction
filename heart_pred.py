from flask import Flask, request, render_template
import numpy as np
from joblib import load

app = Flask(__name__)

# Load trained model
model = load('Heart_Disease_Prediction.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['slope_of_peak_exercise_st_segment']),
        float(request.form['resting_blood_pressure']),
        int(request.form['chest_pain_type']),
        int(request.form['num_major_vessels']),
        int(request.form['fasting_blood_sugar_gt_120_mg_per_dl']),
        int(request.form['resting_ekg_results']),
        float(request.form['serum_cholesterol_mg_per_dl']),
        float(request.form['oldpeak_eq_st_depression']),
        int(request.form['sex']),
        int(request.form['age']),
        int(request.form['max_heart_rate_achieved']),
        int(request.form['exercise_induced_angina']),
        int(request.form['thal_normal']),
        int(request.form['thal_reversible_defect'])
    ]

    prediction = model.predict([features])[0]
    output = 'Presence of Heart Disease' if prediction == 1 else 'No Heart Disease Detected'

    return render_template('index.html', prediction_text=output)

if __name__ == '__main__':
    app.run(debug=True)

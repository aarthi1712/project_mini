from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('prediction.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    model = joblib.load('thyroid_model.pkl')

    if request.method == 'POST':
        age = float(request.form['age'])
        gender = request.form['gender']
        sick=request.form['sick']
        pregnant = request.form['pregnant']
        thyroid_surgery = request.form['thyroid-surgery']
        hypothyroid = request.form['hypothyroid']
        hyperthyroid = request.form['hyperthyroid']
        goiter = request.form['goiter']
        TSH = float(request.form['TSH'])
        T3_measured = request.form['T3-measured']
        T3 = float(request.form['T3'])
        TT4 = float(request.form['TT4'])
        T4U = float(request.form['T4U'])
        FTI = float(request.form['FTI'])

        sick=1 if sick=='yes' else 0
        gender = 1 if gender == 'female' else 0
        pregnant = 1 if pregnant == 'yes' else 0
        thyroid_surgery = 1 if thyroid_surgery == 'yes' else 0
        hypothyroid = 1 if hypothyroid == 'yes' else 0
        hyperthyroid = 1 if hyperthyroid == 'yes' else 0
        goiter = 1 if goiter == 'yes' else 0
        T3_measured = 1 if T3_measured == 'yes' else 0

        input_data = [[age, gender, sick, pregnant, thyroid_surgery, hypothyroid, hyperthyroid, goiter, TSH, T3_measured, T3, TT4, T4U, FTI]]

       
        prediction = model.predict(input_data)
        output=prediction[0]
    if output == 0:
        return render_template('prediction.html', prediction_result='Sick')
    elif output == 1:
        return render_template('prediction.html', prediction_result='Hypothyrid')
    elif output == 2:
        return render_template('prediction.html', prediction_result= 'Hypothyrid')
    else:
        return render_template('prediction.html', prediction_result='Negative')

if __name__ == '__main__':
    app.run(debug=True)

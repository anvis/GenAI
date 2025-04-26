from flask import Flask, render_template, flash

app = Flask(__name__)

# Route to display the form
@app.route('/')
def home():
    return render_template('button.html')


# Route to handle form submission and prediction
@app.route('/Predict', methods=['POST'])
def predict():
    # Get the values from the form
   # loan = float(request.form['loan'])   
    flash('You are already registered, please log in')

    # Return the prediction
    return render_template('button.html')       


# To Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
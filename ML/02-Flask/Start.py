from flask import Flask, render_template

app = Flask(__name__)

# Route to display the form
@app.route('/')
def home():
    return "<p>Hello, World!</p>"

# To Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
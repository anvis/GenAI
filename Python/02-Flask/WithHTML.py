from flask import Flask, render_template

app = Flask(__name__)

# Route to display the form
@app.route('/')
def home():
    return render_template('index.html')


# Route to display the form
@app.route('/Product')
def home2():
    return render_template('Product.html')

# To Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)

# Team folder will not render as we didnot add it to Route. But files in Static folder will be rendered on browser.


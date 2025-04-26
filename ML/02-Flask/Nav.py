# we will use get bootstrap for initial templates.


from flask import Flask, render_template

app = Flask(__name__)

# Route to display the form
@app.route('/')
def home():
    return render_template('Nav.html')


# To Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)

# Team folder will not render as we didnot add it to Route. But files in Static folder will be rendered on browser.


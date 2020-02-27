from flask import (
    Flask
)

# Create the application instance
app = Flask(__name__, template_folder="templates")


@app.route('/api/predict')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return '<p>Hello world</p>'


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)

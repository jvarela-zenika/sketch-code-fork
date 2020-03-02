from flask_cors import cross_origin
from firebase import Firebase

config = {
    "apiKey": "AIzaSyBgtpmqpfdqBOA6sQcYNaqzY5xOLnkG3tg",
    "authDomain": "mockup-to-html.firebaseapp.com",
    "databaseURL": "https://mockup-to-html.firebaseio.com",
    "projectId": "mockup-to-html",
    "storageBucket": "mockup-to-html.appspot.com",
    "messagingSenderId": "735909160162",
    "appId": "1:735909160162:web:ac85fa4f9e97a3a53a2abb"
}

firebase = Firebase(config)

from flask import render_template, Flask

# Create the application instance
from src.classes.inference.Sampler import Sampler

app = Flask(__name__, template_folder="")
sampler = None


@app.route('/api/predict', methods=['GET'])
@cross_origin()
def home():
    global sampler
    storage = firebase.storage()
    storage.child("mockup.png").download("mockup.png")
    sampler = Sampler(
        model_json_path="../../bin/model_json.json",
        model_weights_path="../../bin/weights.h5"
    ) if sampler is None else sampler

    sampler.convert_single_image("./", png_path="./mockup.png", print_generated_output=False,
                                 get_sentence_bleu=False, original_gui_filepath=None,
                                 style="default")

    return render_template("./mockup.html")


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)

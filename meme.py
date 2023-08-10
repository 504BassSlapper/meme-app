from flask import Flask, render_template
import os
import json
import requests

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/")
def index():
    url = "https://meme-api.com/gimme"
    response = json.loads (requests.request ("GET", url).text)
    meme_pic = response["preview"][-2]
    subreddit = response["subreddit" ]
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)
    

if __name__ == "__main__":
    app.run(debug=True)


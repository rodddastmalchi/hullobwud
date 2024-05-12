import os
from random import randint

from flask import Flask, redirect, render_template, request, send_from_directory

import constants

app = Flask(__name__)

emotion_to_image_map = {
    constants.Emotions.HAPPY: constants.HAPPY,
    constants.Emotions.MEMEY: constants.MEMEY,
    constants.Emotions.SAD: constants.SAD,
    constants.Emotions.SLOSHED: constants.SLOSHED,
    constants.Emotions.RANDOM: constants.RANDOM,
    constants.Emotions.TIRED: constants.TIRED
}


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route("/6months", methods=['GET', 'POST'])
def six_months():
    return render_template('six_months.html')


@app.route("/2years", methods=['GET', 'POST'])
def two_years():
    show_modal = False
    img = None
    text = None

    if request.method == 'POST':
        emotion = request.form["type"].lower()
        print(f'EMOTION = {emotion}')
        if emotion in emotion_to_image_map:
            index = randint(0, len(emotion_to_image_map[emotion]) - 1)
            img = emotion_to_image_map[emotion][index].img_path
            text = emotion_to_image_map[emotion][index].text
            show_modal = True

    return render_template('two_years.html', showModal=show_modal, img=img, text=text)


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if request.form["type"] == '6 months':
            return redirect("/6months", code=302)
        elif request.form["type"] == '2 years':
            return redirect("/2years", code=302)
    return render_template('main.html')


@app.errorhandler(500)
def internal_error(error):
    return render_template("500error.html")

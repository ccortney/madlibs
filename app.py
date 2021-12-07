from flask import Flask, request, render_template
from stories import stories

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("choice.html", stories=stories.values())

@app.route('/form')
def get_answers():
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts
    return render_template("form.html", prompts = prompts,story_id=story_id)

@app.route('/yourstory')
def save_answers():
    answers = request.args
    story_id = request.args['story_id']
    story = stories[story_id]
    story_text = story.generate(answers)
    
    return render_template("yourstory.html", story_text=story_text)






from flask import Flask, request, render_template
import stories

story = stories.story

app = Flask(__name__)

@app.route('/')
def homepage():
    prompts = story.prompts
    return render_template("form.html", prompts = prompts)

@app.route('/yourstory')
def save_answers():
    answers = request.args
    story_text = story.generate(answers)
    
    return render_template("yourstory.html", story_text=story_text)






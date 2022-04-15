from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
from trivia_question import get_question
import html

app = Flask(__name__)

data = get_question()
q = html.unescape(data['results'][0]['question'])
correct_ans = data['results'][0]['correct_answer']
incorrect_ans = data['results'][0]['incorrect_answers']

@app.route('/')
def landing():
    return render_template("trivia.html", question = q)

@app.route('/question', methods=['POST'])
def question():
    if request.method == "POST":
        if request.form.get("answer"):
            if request.form.get("answer").title() == correct_ans:
                return redirect(url_for("correct"))
            else:
                return redirect(url_for("landing"))
        else:
            return redirect(url_for("landing"))

@app.route('/correct')
def correct():
    return 'Congratulations! Your answer was correct!'
            

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)
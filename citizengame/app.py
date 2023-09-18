from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Import your citizenship_questions dictionary from another file
from questions import citizenship_questions

@app.route('/')
def index():
    # Get the current question from the session or choose a random one
    current_question = session.get('current_question')
    if current_question is None:
        current_question = random.choice(list(citizenship_questions.keys()))
        session['current_question'] = current_question

    # Get the user's current score from the session or initialize it to 0
    user_score = session.get('user_score', 0)

    answer =  citizenship_questions[current_question]

    return render_template('index.html', question=current_question, score=user_score, answer=answer)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('user_answer', '').strip().lower()
    current_question = session.get('current_question')
    correct_answer = citizenship_questions[current_question]

    if type(correct_answer) == str:
        if user_answer == correct_answer.lower():
            result = "Correct!"
            # Increment the user's score by 1 for a correct answer
            user_score = session.get('user_score', 0)
            user_score += 1
            session['user_score'] = user_score
        else:
            result = "Wrong!<br>The correct answers are: " + correct_answer

    elif type(correct_answer) == list:
        if user_answer in [answer.lower() for answer in correct_answer]:
            result = "Correct!"
            # Increment the user's score by 1 for a correct answer
            user_score = session.get('user_score', 0)
            user_score += 1
            session['user_score'] = user_score
        else:
            result = "Wrong!<br>The correct answers are: " + ', '.join(correct_answer)

    
    # Remove the current question from the session
    session.pop('current_question', None)

    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from flask_admin import Admin
import sqlite3
import markdown

app = Flask(__name__)


def get_questions():
  conn = sqlite3.connect('questions.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM questions")
  courses = cursor.fetchall()
  conn.close()
  return courses


def get_questions_by_id(course_id):
  conn = sqlite3.connect('questions.db')
  cursor = conn.cursor()
  cursor.execute("SELECT title, markdown FROM questions WHERE id=?",
                 (course_id, ))
  question = cursor.fetchone()
  conn.close()
  return question


def render_markdown(markdown_path):
  html = markdown.markdown(markdown_path)
  return html


@app.route("/")
def hello_world():
  questions = get_questions()
  return render_template('home.html', questions=questions)


@app.route('/questions/<int:question_id>')
def course(question_id):
  question = get_questions_by_id(question_id)
  if question:
    title, markdown_path = question
    content = render_markdown(markdown_path)
    return render_template('question.html', title=title, content=content)
  else:
    return "question not found", 404


admin = Admin(app, name='MyApp', template_mode='bootstrap3')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)

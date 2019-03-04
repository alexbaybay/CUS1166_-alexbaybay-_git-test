import sys
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

#basedir = os.path.abspath(os.path.dirname(__file__))
#DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')

#initializes database
#engine = create_engine(DATABASE_URL)

#scopped_session manages multiple connection in the database
#db = scopped_session(sessionmaker(bind=engine))

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route("/add_course", methods=["post"])
def course():
    id = request.form.get("id")
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")

    course = Course(id=id, course_number=course_number, course_title=course_title)
    db.session.add(course)
    db.session.commit()

    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route("/register_student/<int:course_id", methods=["GET","POST"])
def course(course_id):
    course = Course.query.all(course_id)

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")
        id = request.form.get("id")
        course.add_student(id, name, grade)

    students = course.registeredstudents
    return render_template("course_details.html", course=course, students=students)

if __name__ == '__main__':
    main()

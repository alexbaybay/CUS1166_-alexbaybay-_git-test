import os
import flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')

#initializes database
engine = create_engine(DATABASE_URL)

#scopped_session manages multiple connection in the database
db = scopped_session(sessionmaker(bind=engine))

app = Flask(__name__)
@app.route("/")
def index():
    courses = db.execute("SELECT * from courses")
    return render_template('index.html', courses=courses)
@app.route("/add_course", methods=["post"])
def course():
    
    return
@app.route("/register_student/")

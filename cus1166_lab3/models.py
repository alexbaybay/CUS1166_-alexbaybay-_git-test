from flask_sqlalchemy import flask_sqlalchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__="courses"
    #Unique ID
    id = db.Colulmn(db.Integer, primary_keys=True)
    #Course # CUS1166
    course_number = db.Colulmn(db.String, nullable=False)
    #String
    course_title = db.Colulmn(db.String, nullable=False)

class RegisteredStudent(db.Model):
    __tablename__="registeredstudents"
    #Unique ID
    id = db.Column(db.Integer, primary_keys=True)
    #First and last name
    name = db.Column(db.String, nullable=False)
    #Number
    grade = db.Column(db.String, nullable=False)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#defines a  course model
class Course(db.Model):
    __tablename__="courses"
    #Unique ID Column
    id = db.Colulmn(db.Integer, primary_keys=True)
    #Course number column (example: CUS1166)
    course_number = db.Colulmn(db.String, nullable=False)
    #title column
    course_title = db.Colulmn(db.String, nullable=False)

    #Specifying relationships in fields
    students = db.relationship("RegisteredStudents", backref = "courses", lazy=True)

    def add_student(id, name, grade):
        new_student = RegisteredStudent(id = id, name = name, grade = grade)
        db.session.add(new_student)
        db.session.commit()

class RegisteredStudent(db.Model):
    __tablename__="registeredstudents"
    #Unique ID
    id = db.Column(db.Integer, primary_keys=True)
    #First and last name
    name = db.Column(db.String, nullable=False)
    #Number
    grade = db.Column(db.String, nullable=False)

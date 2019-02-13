#importing flask class from flsk module
from flask import Flask

#Creating Instance for flask class
app = Flask(__name__)

#defining a route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    class_roster = [("Alex", "89", "Junior"), ("Christopher", "79", "Freshman"),
    ("Selina", "90", "Junior"), ("Mike", "85", "Sophomore"), ("Frances", "95", "Senior"),
    ("Chris", "88", "Senior"), ("Rich", "80", "Junior")]
    return render_template("roster.html", grade_view=grade_view, class_roster=class_roster)

if __name__ == '__main__':
    app.run()

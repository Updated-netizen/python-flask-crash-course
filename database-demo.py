from flask import FLASK, request, jsonify
from flask_sqlalchemy import SQLALCHEMY

app = FLASK(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
db = SQLALCHEMY(app)

class Student(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True, unique=True)
    password = db.Column(db.String(50), nullable=True)
    reg_no = db.Column(db.String(50), nullable=True, unique=True)
    departmebnt = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(50), nullable=True)

@app.route("/student", methods=["POST"])
def create_student():
    data = request.get_json(silent=True) or {}

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = date.get("email")
    password = data.get("password")
    reg_no = data.get("reg_no")
    depart
    if not all([first_name, email, password, reg_no, department])
        return jsonify({"error": "missing required fields"})

    if Student.query

    def to_response(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "reg_no": self.reg_no,
            "department": self.department,
            "address": self.address
        }

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.app_context



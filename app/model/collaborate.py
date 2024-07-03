from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Collaborate(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    phone_num = db.Column(db.String(13), unique=False, nullable=False)
    email_id = db.Column(db.String(40), unique=False, nullable=False)
    subject_comments = db.Column(db.String(200), unique=True, nullable=False)
    date_time = db.Column(db.String(20), unique=False, nullable=True)

    def __init__(self, first_name:str,last_name:str, phone_num:str, email_id:str, subject_comments:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.email_id = email_id
        self.subject_comments = subject_comments
        self.date_time = datetime.now()

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} contacted regarding {self.subject_comments} on {self.date_time}"

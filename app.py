import os
from datetime import datetime

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "GlassBase.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MedOrganizationName = db.Column(db.String(80), unique=True, nullable=False)
    Sex = db.Column(db.String(120), unique=False, nullable=False)
    BirthYear = db.Column(db.Integer, unique=False, nullable=False)
    Position = db.Column(db.String(100), unique=False, nullable=False)
    Diagnosis = db.Column(db.String(100), unique=False, nullable=False)
    MkbCode = db.Column(db.String(100), unique=False,nullable=False)
    TakeDate = db.Column(db.Integer, unique=False, nullable=False)
    Mark = db.Column(db.String(100), unique=False,nullable=False)

    def __repr__(self):
        return '<Diagnosis %r>' % self.Diagnosis


@app.route('/CreateNewEntity')
def CreateFields():
    test = User(id=1, MedOrganizationName="Test", Sex="Male",
                BirthYear=1980, Position="Selo", Diagnosis="Smert",MkbCode="123",
                TakeDate=datetime.strptime("2019-01-01", '%Y-%m-%d'), Mark="Prost")
    db.session.add(test)
    db.session.commit()
    return render_template("NewItemCreation.html")

@app.route('/index')
def Search():
    test = User(id=1, MedOrganizationName="Test", Sex="Male",
                BirthYear=1980, Position="Selo", Diagnosis="Smert",MkbCode="123",
                TakeDate=datetime.strptime("2019-01-01", '%Y-%m-%d'), Mark="Prost")
    return render_template("SearchField.html.html")


@app.route('/CreateNewEntity', methods=['POST'])
def Creation():
    data = request.form['Sex']
    return "NewItemCreation.html"


if __name__ == '__main__':
    app.run()

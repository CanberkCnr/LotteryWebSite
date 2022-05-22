from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/canbe/OneDrive/Masaüstü/RoolSite/rool.db'

db = SQLAlchemy(app)
class Rool(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))

@app.route("/")
def index():
    rools = Rool.query.all()
    return render_template("index.html",rools = rools)

@app.route("/delete/<string:id>")
def delete(id):
    rools = Rool.query.filter_by(id = id).first()
    db.session.delete(rools)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/add",methods=["POST"])
def add():
    username = request.form.get("username")
    new = Rool(username = username)
    db.session.add(new)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/cek")
def cek():
    bilgiler = Rool.query.all()
    lottery = []
    for i in bilgiler:
        lottery.append(i)
    rools = random.choice(lottery)
    return render_template("cek.html",rools = rools)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
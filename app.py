from flask import Flask
# from database import db
from models.user import User
from database import db

app = Flask(__name__)
# secret key: por ser teste, deixar algo simples
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Ola"


if __name__ == "__main__":
    app.run(debug=True)
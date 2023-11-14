from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = '^%nknsvknnjsljaiozjojojfjijjiosjeg(jks)^'
<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:phuphan13@localhost/saledbv1?charset=utf8mb4"
=======
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4" % quote('Admin@123')
>>>>>>> 01dae9c619b16595e334ffb64663443053e05f32
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

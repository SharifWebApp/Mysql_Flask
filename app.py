from flask import Flask
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from datetime import datetime

app = Flask(__name__)
#############################################################
# Engine For Database Creation ##############################
#############################################################

URL = "mysql://root:root@localhost"
DATABASE = "flaskapp"

engine = sqlalchemy.create_engine(URL)
engine.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE} ;")
engine.execute("USE %s;"%(DATABASE))

############################################################
# Connecting App to the Database ###########################
############################################################
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/flaskapp"
db = SQLAlchemy(app)

############################################################

############################################################
class User(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String(20), nullable=False)
    lastname=db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    joinedMail = db.Column(db.String(3), nullable=False)
    emailConf = db.Column(db.Boolean, default=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User({self.username})"


@app.route("/")
def home():
    ####################################################################
    # Testing Connection to the Database ###############################
    ####################################################################
    newUser = User(firstname="ali", lastname="ali", username="asdasd", email="email",password="12323", phone="21312312", joinedMail=True)
    db.session.add(newUser)
    db.session.commit()
    return "This is Home"


if __name__ == '__main__':

    ##############################################################
    # Use Connection to Databse for Creating Tabels (Models) #####
    ##############################################################
    db.create_all()
    ##############################################################
    app.run(debug=True)

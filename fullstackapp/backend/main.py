from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask import request
import logging

#
# PSCFSA backend (PXL super-complicated full-stack app)
#
app = Flask(__name__)

# log time
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# This keeps the warning messages away
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# get env variables
db_user = os.environ.get('DATABASE_USER', 'postgres')
db_password = os.environ.get('DATABASE_PASSWORD', 'postgres')
db_server = os.environ.get('DATABASE_URI', 'localhost')
db_port = os.environ.get('DATABASE_PORT', '5432')
db_name = os.environ.get('DATABASE_NAME', 'postgres')
backend_network = os.environ.get('BACKEND_NETWORK', '0.0.0.0')
backend_port = os.environ.get('BACKEND_PORT', '5000')

logging.info('DATABASE_USER: ' + db_user)
logging.info('DATABASE_PASSWORD: ' + db_password)
logging.info('DATABASE_URI: ' + db_server)
logging.info('DATABASE_PORT: ' + db_port)
logging.info('DATABASE_NAME: ' + db_name)
logging.info('BACKEND_NETWORK: ' + backend_network)
logging.info('BACKEND_PORT: ' + backend_port)

# postgress connection string
# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
db_connection = "postgresql://" + db_user + ":" + \
    db_password + "@" + db_server + "/" + db_name

logging.info('database connection string: ' + db_connection)

# connect to db
app.config['SQLALCHEMY_DATABASE_URI'] = db_connection

db = SQLAlchemy(app)
db.init_app(app)


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"<Text {self.text}>"


@app.route('/fetch')
def fetch():
    words = Text.query.all()
    results = [
        {
            "text": word.text
        } for word in words]
    return {"texts": results}, 200


@app.route('/add', methods=['POST'])
def add():
    text = request.json['text']
    db.session.add(Text(text=text))
    db.session.commit()
    return 'Done', 201


@app.route('/delete', methods=['DELETE'])
def delete():
    db.session.query(Text).delete()
    db.session.commit()
    return 'Done', 200


if __name__ == "__main__":
    logging.info('starting backend server on ' +
                 backend_network + ' port ' + backend_port)
    app.run(host=backend_network, port=backend_port)

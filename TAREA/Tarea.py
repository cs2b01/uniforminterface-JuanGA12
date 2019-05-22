from flask import Flask,render_template,url_for, request, session, Response, redirect, jsonify, json
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/users")
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.Book)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/create_users', methods = ['GET'])
def create_test_books():
    db_session = db.getSession(engine)
    book = entities.Book(name="Juan", last_name="Galvez", password="Ut3c2108")
    db_session.add(book)
    db_session.commit()
    return "Congrats, user created!\n"

if __name__ == "__main__":
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))

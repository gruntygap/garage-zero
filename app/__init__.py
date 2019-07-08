from flask import Flask, request, abort
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)


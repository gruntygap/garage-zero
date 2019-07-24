from flask import Flask, request, abort
from app.routes import routes 

app = Flask(__name__)
app.register_blueprint(routes)


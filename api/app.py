import os
from flask import Flask
from mongoengine import connect
from config import *
from v1.resources.submissions import submissions

app = Flask(__name__)
app.register_blueprint(submissions, url_prefix='/api/v1/submissions')

config = globals()[os.environ['ENV']]
app.config.from_object(config)
connect('app', host=config.MONGODB_URL)


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)

#!/usr/bin/python
from flask import Flask
# fix https redirect issue on cloud foundry
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
# fix https redirect issue on cloud foundry
app.wsgi_app = ProxyFix(app.wsgi_app)

from app import views

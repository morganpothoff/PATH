#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import *
from datetime import datetime

#import DB_Connections


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def home():
	return render_template("Home.html")

@app.route("/AddEvents")
def addEvents():
	return render_template("AddEvents.html")

@app.route("/Timeline")
def timeline():
	return render_template("Timeline.html")


app.run(host="localhost", port=8000, debug=True)
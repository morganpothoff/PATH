#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import *
from datetime import datetime

#import DB_Connections


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def home():
	return render_template("Home.html")


@app.route("/AddAssignments")
def newDream():
	return render_template("AddAssignments.html")


app.run(host="localhost", port=8000, debug=True)
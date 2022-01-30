#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import *
from datetime import datetime
import databaseOperations
import json
import os

#import DB_Connections


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def home():
	return render_template("Home.html")

@app.route("/AddEvents", methods=["GET", "POST"])
def addEvents():
	import re
	with open("../Variables.env", "r") as file:
		lines = file.read()	
	env_vars = [val[1:-1] for val in re.findall(r"\".+\"", lines)[:2]] + ["PATH_DB"]
	# username = os.getenv("GC_DB_USER")
	print(os.environ)
	# print(username)
	# password = os.getenv("GC_DB_PASSWORD")
	# ip_address = os.getenv("GC_DB_IP")
	
	if(request.method == "POST"):
		cnx, cursor = databaseOperations.__CONNECT__(*env_vars)

		# cnx, cursor = databaseOperations.__CONNECT__(username, password, db_name)
		print(str(request.form.get('time')))
		print(f"{int(request.form.get('time')):02}:00:00")
		databaseOperations.insert_new_event(
		# print(
			cnx, cursor, 
			request.form.get('Title'), 
			request.form.get('Course'), 
			request.form.get('Type'), 
			request.form.get('Date'), 
			f"{int(request.form.get('time')):02}:00:00"
		)
		return render_template("AddEvents.html")
	else:
		return render_template("AddEvents.html")

@app.route("/Timeline")
def timeline():
	return render_template("Timeline.html")

# get all events
@app.route("/Api/AllEvents", methods=["GET", "POST"])
def api_AllEvents():
	import re
	with open("../Variables.env", "r") as file:
		lines = file.read()	
	env_vars = [val[1:-1] for val in re.findall(r"\".+\"", lines)[:2]] + ["PATH_DB"]
	# username = os.getenv("GC_DB_USER")
	# print(username)
	# password = os.getenv("GC_DB_PASSWORD")
	# ip_address = os.getenv("GC_DB_IP")
	
	if(request.method == "POST"):
		cnx, cursor = databaseOperations.__CONNECT__(*env_vars)
		events = databaseOperations.select_all_events(cursor)
		[event.update({"dueDate": datetime.strftime(event["dueDate"], "%Y-%m-%d %H:%M:%S")}) for event in events]
		[event.update({"duration": event["duration"].total_seconds()}) for event in events]
		return json.dumps(events)



		# return render_template("Timeline.html")
	else:
		return render_template("Timeline.html")

# # get one event
# @app.route("/Api/OneEvent")
# def api_OneEvent():
# 	return render_template("Timeline.html")

# get events in range
@app.route("/Api/RangeEvents")
def api_RangeEvents():
	return render_template("Timeline.html")

@app.route("/Api/events", methods=["POST", "GET"])
def api_events():	
	pass

	# databaseOperations.select_event_range(cursor, request.form[], end)
	# 	# databaseOperations.select_all_events(cursor)


app.run(host="localhost", port=8000, debug=True)
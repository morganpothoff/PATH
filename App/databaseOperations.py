

from datetime import datetime
import os


def __CONNECT__(user: str, password: str, db_name: str):
	import mysql.connector;
	cnx = mysql.connector.connect(user=user, password=password, host="34.71.64.211", port="3306",  database=db_name);
	return cnx, cnx.cursor(buffered=True);


def __UTILITY__associate_query(cursor):
	headers = [header[0] for header in cursor._description];
	return [{header: (row[x] if row[x] else None) for x, header in enumerate(headers)} for row in cursor._rows];


def __UTILITY__query(cursor: object, query: str, *params) -> list:
	if(len(params)): cursor.execute(query, params);
	else: cursor.execute(query);
	return __UTILITY__associate_query(cursor);


def __UTILITY__insert(cnx: object, cursor: object, query: str, *params) -> int:
	if(len(params)): cursor.execute(query, params);
	else: cursor.execute(query);
	cnx.commit();
	return cursor.lastrowid;



def select_all_events(cursor):
	query = "SELECT * FROM `Events`;"
	return __UTILITY__query(cursor, query)


def insert_new_event(cnx: object, cursor, title, className, type, dueDate: datetime, duration: str):
	query =	"""
				INSERT INTO `Events` (title, className, type, dueDate, duration) 
				VALUES (%s, %s, %s, %s, %s);
			"""
	
	return __UTILITY__insert(cnx, cursor, query, title, className, type, dueDate, duration)


def select_event_range(cursor, start: datetime, end: datetime):
	query = """
				SELECT * FROM `Events`
				WHERE dueDate >= %s
				AND dueDate <= %s;
			"""
	start_string = start.strftime("%Y-%m-%d %H:%M:%S")
	end_string = end.strftime("%Y-%m-%d %H:%M:%S")

	return __UTILITY__query(cursor, query, start_string, end_string)



def main():
	username = os.getenv("GC_DB_USER")
	password = os.getenv("GC_DB_PASSWORD")
	db_name = "PATH_DB"
	ip_address = "34.71.64.211" #os.getenv("GC_DB_IP")

	cnx, cursor = __CONNECT__("pathuser", "pathuserpassword", db_name)

	# insert_new_event(cnx, cursor, "HW2", "CS 4384", "homework", datetime.strptime("2022-02-06 23:59:59", "%Y-%m-%d %H:%M:%S"), "01:00:00")
	print(select_all_events(cursor))
	# print("\n\n\n\n")
	# print(select_event_range(cursor, datetime.strptime("2022-01-30 23:59:59", "%Y-%m-%d %H:%M:%S"), datetime.strptime("2022-02-06 23:59:59", "%Y-%m-%d %H:%M:%S")))




if __name__ == '__main__':
	main()

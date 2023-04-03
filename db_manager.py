import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f'the error {e} occured')

def execute_query(conn, query, data=""):
    cursor = conn.cursor()
    try:
        if data == "":
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        conn.commit()
        print("Zapytanie zakończone sukcesem")
    except Error as e:
        print(query)
        print(f'the error {e} occured')

def create_tasks_table(conn):
    create_users_table = """
            CREATE TABLE IF NOT EXISTS tasks (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              task TEXT NOT NULL
            );
            """
    execute_query(conn, create_users_table)

def read_whole_table(conn, table):
    select_all = """SELECT * from """ + table
    cursor = conn.cursor()
    cursor.execute(select_all)
    return cursor.fetchall()

def insert_task(conn, task):
    insert_query = """ INSERT INTO tasks (task)
              VALUES(?) """
    execute_query(conn, insert_query, task)

def update_task(conn, old_task, new_task):
    update_query = """ UPDATE tasks
              SET task = ?
              WHERE task = ? """
    execute_query(conn, update_query, (new_task, old_task))

def delete_task(conn, task):
    delete_query = """ DELETE FROM tasks
                   WHERE task = ? """
    execute_query(conn, delete_query, task)

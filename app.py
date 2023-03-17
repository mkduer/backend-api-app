from flask import Flask
from constants import LOCALHOST, PORT, DATABASE
from sqlite3 import connect, Error
import os

# flask app
app = Flask(__name__)

def select_all():
    """Connects to database and selects all employees

    Returns:
        List of dictionary objects: key, value pair of column header and value
        Example: [{ "gender": female, "id": 5 }] or None if table has no rows
    """
    rows = None

    try: 
        database_path = os.getcwd() + '\\' + DATABASE
        connection = connect(database_path)
        connection.row_factory = row_to_dictionary_factory
        cursor = connection.cursor()
    except Error:
        print(f'Failed to connect to DB: {Error}')
    else:
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
    finally:
        cursor.close()

    return rows

def row_to_dictionary_factory(cursor, row):
    """Converts cursor row from tuple to dictionary

    Returns:
        Dictionary: key, value pair of column header and value
    """
    fields = [column[0] for column in cursor.description]
    return { key : value for key, value in zip(fields, row) }

@app.route("/employees")
def employees():
    result = select_all()
    return result

if __name__ == "__main__":
    app.run(host=LOCALHOST, port=PORT, debug=True)
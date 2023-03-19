import os
from constants import DATABASE
from models.employee_model import EmployeeModel
from sqlite3 import connect, Error, Cursor

class SqliteDatastore(EmployeeModel):

    def __init__(self):
        # check for successful DB connection
        current_path = os.getcwd()
        self.database_path = os.path.join(current_path, DATABASE)

        try: 
            connection = connect(self.database_path)
            cursor = connection.cursor()
        except Error:
            print(f'Failed to connect to DB: {Error}')
        finally:
            cursor.close()


    def select_all(self) -> dict:
        """Connects to database to select all employees

        Returns:
            List of dictionary objects: key, value pair of column header and value
            Example: [{ "gender": female, "id": 5 }] or None if the table has no rows
        """
        rows = None

        try: 
            connection = connect(self.database_path)
            connection.row_factory = self.row_to_dictionary_factory
            cursor = connection.cursor()
        except Error:
            print(f'Retrieval failed. Database connection error: {Error}')
        else:
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
        finally:
            cursor.close()

        return rows

    def row_to_dictionary_factory(self, cursor: Cursor, row: tuple[tuple]) -> dict:
        """Converts cursor row from tuple to dictionary

        Args:
            cursor (Cursor): the cursor location
            row (tuple of tuples): a row in the table

        Returns:
            Dictionary: key, value pair of column header and value
        """
        fields = [column[0] for column in cursor.description]
        return { key : value for key, value in zip(fields, row) }

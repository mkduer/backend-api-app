from constants import LOCALHOST, PORT
from flask import Flask, Response, jsonify
from os import environ
from services.employee import EmployeeService

app = Flask(__name__)

@app.route("/employees", methods=['GET'])
def get_employees() -> Response:
    return jsonify(EmployeeService.get())

def get_port() -> int:
    """Sets the port value to a system variable if it exists, otherwise sets a default

    Returns:
        int: port value
    """
    port = environ.get('PORT')
    
    if (port is None):
        port = PORT

    return port
    
if __name__ == "__main__":
    app.run(host=LOCALHOST, port=get_port(), debug=False)
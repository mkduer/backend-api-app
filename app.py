from constants import LOCALHOST, PORT
from flask import Flask, jsonify
from services.employee import EmployeeService

app = Flask(__name__)

@app.route("/employees", methods=['GET'])
def get_employees():
    return jsonify(EmployeeService.get())


if __name__ == "__main__":
    app.run(host=LOCALHOST, port=PORT, debug=True)
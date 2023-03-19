# Backend Api App



## Instructions

Specifications: Windows OS, `Python 3.11.2`, and using `py` launch command in the Git Bash Terminal.

An assumption is made that this program will be run on the latest Python versions for either Windows/Linux operating systems, and `python3` should alias a latest version on Linux in the following instructions.

* Clone the repository with `git clone git@github.com:mkduer/backend-api-app.git`
  


### Run Program without a Virtual Environment
* Install the Flask library if needed `pip install -r requirements.txt`
* Optionally, set a `PORT` environment variable from the CLI with `export PORT=8888` (otherwise, the default port 8000 will be used)
* Start the program
  * windows: `py -m venv test_env`
  * linux: `python3 -m venv test_env`


### Run Program in a Virtual Environment
The `venv` virtual environment package is included with the standard Python library, and will ensure that local state will remain unaffected by this program.

**Create a virtual environment**

* windows: `py -m venv test_env`
* linux: `python3 -m venv test_env`

**Activate the virtual environment**
* windows: `source test_env/Scripts/activate`
* linux: `source test_env/bin/activate`

**Run the program**
* Install necessary packages `pip install -r requirements.txt`
* Optionally, set a `PORT` environment variable from the CLI with `export PORT=8888` (otherwise, the default port 8000 will be used)
* Start the program
  * windows: `py -m venv test_env`
  * linux: `python3 -m venv test_env`


### Call the API

* After the program has compiled, call the endpoint with one of the following options:
  * Curl command in CLI  `curl localhost:$PORT/employees`
  * Postman `GET` `http://localhost:{PORT}/employees`
  * Browser by visiting `http://localhost:{PORT}/employees`
* The resulting JSON should match the following

```json
[
    {
        "gender": "male",
        "id": 1
    },
    {
        "gender": "male",
        "id": 2
    },
    {
        "gender": "male",
        "id": 3
    },
    {
        "gender": "female",
        "id": 4
    },
    {
        "gender": "female",
        "id": 5
    },
    {
        "gender": "female",
        "id": 6
    }
]
```



**Deactivate the Virtual Environment**

If running on a virtual environment, deactivate the environment

* windows/linux: `deactivate`



## Resources
- [PyPA: Running a Program on a Virtual Environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
# Synd.io Backend App



## Instructions

* Clone the app locally with `git clone git@github.com:mkduer/syndio-backend-api-app.git`
* Run the app with `py app.py`
* After the program has compiled, call the endpoint with one of the following options:
  * Curl command in CLI  `curl localhost:$PORT/employees`
  * Postman `GET` `https://localhost:8080/employees`
  * Browser at [https://localhost:8080/employees](https://localhost:8080/employees)

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



## MVP

- Api runs when following setup instructions
- The curl command returns the described response
- The api is written in Python
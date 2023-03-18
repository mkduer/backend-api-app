# Synd.io Backend App



## Instructions

* Clone the app locally with `git clone TODO: add github URL`
* Run the app with `py app.py`
* After the program has compiled, call the endpoint with one of the following options:
  * Call the endpoint with curl `curl localhost:$PORT/employees`
  * Postman `GET` `https://localhost:8080/employees`
  * Open up the browser at [https://localhost:8080/employees](https://localhost:8080/employees) 

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

- We can run the api from your setup instructions :heavy_check_mark:
- The curl returns the described response :heavy_check_mark:
- The api is written in Python or Go :heavy_check_mark:
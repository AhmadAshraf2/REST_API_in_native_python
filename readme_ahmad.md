# blog rest api using native python

## Setting up:
    -1 Simply run 'docker-compose up --build' to build and start the containers.
    -2 There are 2 containers one for postgres instance and the other to run recipe_api.
    -3 The Api is accessible outside the container on localhost:8080.
    -4 The Database is accessible on localhost:5442.
    -5 wait_for_it is a bash script that ensures that the python_app container waits for postgres container to start
       and initialize. Also this script is taken from an online resource.


## Architecture:
    -1 I have implemented the MVC architecture for this API.
    -2 Python native base http server is used to entertain requests.
    -3 Server recieves the request and passes it on to the appropriate controller function.
    -4 Controller then corresponds with model layer which then access data access layer to communicate with DB.
    -5 I have used Json Web tokens for authorization.
    -6 The assumption is tht the mechanism to generate a secret key is already in place and has been shared with the client.
    -7 For protected endpoints json data is sent after it is encrypted using a secret key.

### A few curl commands for sending encrypted data:

        To add a new recipe with correct secret token:
        curl -H "Content-Type: application/json" -X "POST" -d 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aXRsZSI6Im15YmxvZyIsImNvbnRlbnQiOiJ4eXoiLCJjYXRlZ29yeSI6InRlY2hub2xvZ3kifQ.AsvJjb9bfhBO1GOR-d7BQ2M6R-7KelKUuR-Iiioh4KQ' localhost:8080/recipe/9

        To add new recipe with wrong secret token:
        curl -H "Content-Type: application/json" -X "POST" -d 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoicGFrb3JheSIsInByZXBfdGltZSI6IjExMiIsImRpZmYiOjMsInZlZ2FuIjp0cnVlfQ.kKoiLM9poKXQoDJETMMo-T6mLa-ue7Rk5PtPw7YX' localhost:8080/recipe/9

    -8 Unit tests are placed in tests directory and can be run by simply running the recipe_tests.py file


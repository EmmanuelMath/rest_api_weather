# WEATHER API SET UP 

### Set Up A Virtual Env and API KEY
Navigate to main folder
```
python3 -m venv virtualenv_name

```

**Create a credentials.py file to store your API_KEY**

### Install dependencies 
```
 'pip install  -r requirements.txt'

```
### Run APIs

**The main API requires two parameters as follow:**

    - The name of a city 
    - A date in YYYY-MM-DD format

_To test the main API using a test API:_

**Run the main API**
```
python weather_rest_api.py

```
**Open a new terminal and run the test API**

```
python test_main_api.py 

```


## Room for improvement

- build a ci/cd pipeline with Github actions using YAML file 
- create a user interface where users can provide required data (using Streamlit maybe)
- organise files in folders such as sources/ tests/
- create a file per class for isolation 
- implement an algorithm to reformat dates in case a user uses a different format
- create unit tests report using pytest reporting and integrate it to ci/cd
- proof test every single functions 
- refactor the code and make it more concise 

## Resources 

- https://flask.palletsprojects.com/en/3.0.x/
- https://docs.python.org/3/library/unittest.html
- https://docs.pytest.org/en/7.1.x/contents.html
- https://openweathermap.org/api/one-call-3

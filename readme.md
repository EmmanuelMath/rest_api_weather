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

_To run the test main API:_

**Run the main API
```
python weather_rest_api.py

```
**Open a new terminal and run the test API

```
python test_main_api.py 

```


## Room for improvement

- build a ci/cd pipeline with Github actions using YAML file 
- create a user interface where users can provide required data
- organise files in folders such as sources/ tests/
- implement an algorithm to reformat dates in case a user uses a different format

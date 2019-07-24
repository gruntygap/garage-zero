# garage-zero
Code managing a rasp pi zero / relay based garage opener.

## Setting up the env
You will need to be able to utilize venv
The command to create the env is:
```python3 -m venv <path-for-env-dir>```
and the command to run the env is:
```. <path-for-env-dir>/bin/activate```

## Running the server
```gunicorn run:app --bind 0.0.0.0:80```

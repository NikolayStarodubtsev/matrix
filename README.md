# Simple asynchronous web server

This is a simple asynchronous web server which can perform 3 operations:
* Find n prime number
* Factorize number
* Ping specified server specified amount of times

## How to use

### Preparations
To implement this server we use aiohttp Python library which requires
Python 3.5.x, so I suggest to prepare venv with python 3.5 in it. And then
install aiohttp library. All instruction is provided for Ubuntu 16.04.
* Prepare virtualenv

```
sudo apt-get install python3-venv
python3.5 -m venv venv3.5/
source venv3.5/bin/activate
```

* After that install aiohttp lib into venv

```
pip install aiohttp
```

### Run web server

Navigate to source code directory then execute:

```
cd server/polls/
python web_app.py
```
The server is up and running on port 8080

### Requests examples

As it said above the server can operate 3 types of requests.

* Find n prime number

```
curl -d "n=150" localhost:8080/find_prime
```

* Factorize number

```
curl -d "n=12" localhost:8080/factorize
```

* Ping specified server n times

```
curl -d "host=codephobos.com&reps=10" localhost:8080/ping
```

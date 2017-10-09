# Purpose
Do basic Python flask tutorial

# References

## Build a Python-powered web server with Flask
https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet

# Results

## install flask from anaconda/miniconda

Activate environment

    source activate beepscore

Install flask

    conda install -n beepscore flask

## run on raspberry pi, view in macos browser
    python app.py

shows Running on http://0.0.0.0:5000

### Fing
fing shows raspberry pi is on local network at 10.0.0.4  

On macos browser enter 10.0.0.4:5000  

## run on macos, view in macos browser
    python app.py

 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 250-850-674
127.0.0.1 - - [09/Oct/2017 12:19:40] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [09/Oct/2017 12:19:40] "GET /favicon.ico HTTP/1.1" 404 -

On macos browser can use either of 2 ip addresses
    http://127.0.0.1:5000/
    or
    10.0.0.0:5000

## run on macos, view in ios browser

    http://10.0.0.7:5000/hello/joe


# Appendix: git repo

    git init

## push to github
can use 2 factor authentication or https with token

from flask import Flask, render_template

# flask uses jinja to render templates
# http://jinja.pocoo.org/

app = Flask(__name__)


# / is the website root, the entry point
@app.route('/')
def index():
    # render_template searches directory templates
    return render_template('index.html')


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'


# route passes name from url to hello function
# allow for empty name
# https://stackoverflow.com/questions/14023664/flask-url-route-route-several-urls-to-the-same-function
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        return render_template('page.html', name='')

    # pass name from hello to render_template
    spaced_name = ' ' + name
    return render_template('page.html', name=spaced_name)


@app.route('/echo/<text>')
def echo(text=None):
    if text is None:
        return render_template('echo.html', text='')

    # example use web app to call python to run a subprocess command
    # https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call
    from subprocess import PIPE, run

    command = ['echo', text]
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.returncode, result.stdout, result.stderr)
    return render_template('echo.html', text=result.stdout)


if __name__ == '__main__':

    # ipv4
    # '0.0.0.0' accessible to any device on the network, including localhost http://127.0.0.1
    # for example on server machine http://0.0.0.0:5000/ may redirect to localhost http://127.0.0.1:5000
    # https://www.digitalocean.com/community/questions/accessing-debugger-for-flask-127-0-0-1-5000
    host = '0.0.0.0'

    # alternatively could use ipv6
    # https://stackoverflow.com/questions/21673068/dual-ipv4-and-ipv6-support-in-flask-applications#21689979
    # host = '::'
    # e.g. http://[::]:9092/

    # flask default port is 5000
    port = '5000'
    # port = '9092'

    app.run(debug=True, host=host, port=port)

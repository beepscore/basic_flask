from flask import Flask, render_template

# flask uses jinja to render templates
# http://jinja.pocoo.org/

app = Flask(__name__)

# / is the website root, the entry point
# http://127.0.0.1:5000
# home http://127.0.0.1
# port :5000
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
    else:
        # pass name from hello to render_template
        spaced_name = ' ' + name
        return render_template('page.html', name=spaced_name)

if __name__ == '__main__':
    # '0.0.0.0' accessible to any device on the network
    app.run(debug=True, host='0.0.0.0')

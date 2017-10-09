from flask import Flask, render_template


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
@app.route('/hello/<name>')
def hello(name):
    # pass name from hello to render_template
    return render_template('page.html', name=name)

if __name__ == '__main__':
    # '0.0.0.0' accessible to any device on the network
    app.run(debug=True, host='0.0.0.0')

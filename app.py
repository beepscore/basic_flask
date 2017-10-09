from flask import Flask


app = Flask(__name__)

# / is the website root, the entry point
# http://127.0.0.1:5000
# home http://127.0.0.1
# port :5000
@app.route('/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    # '0.0.0.0' accessible to any device on the network
    app.run(debug=True, host='0.0.0.0')

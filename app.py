from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    # '0.0.0.0' accessible to any device on the network
    app.run(debug=True, host='0.0.0.0')

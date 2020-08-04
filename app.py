from flask import Flask

#flask obj
app = Flask(__name__)

#decorater route to the main page
@app.route('/home/<string:name>') #used in dynamic url like name keep changing  etc
def hello(name):
    return "Hello "+name


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask

#flask obj
app = Flask(__name__)

#decorater route to the main page
@app.route('/')
@app.route('/home') # multipe route with one method
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)


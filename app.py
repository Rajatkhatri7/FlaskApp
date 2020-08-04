from flask import Flask,render_template

#flask obj
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


#decorater route to the main page
@app.route('/home/users/<string:name>/posts/<int:id>') #used in dynamic url like name keep changing  etc
def hello(name,id):
    return "Hello "+name+" your id is "+ str(id)
# can add images if we render images on every refresh


#page to allow get req
@app.route("/getpage", methods = ['GET']) # POST for post method 
def get_req():
    return "only getthis web page."


if __name__ == '__main__':
    app.run(debug=True)


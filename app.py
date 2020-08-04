from flask import Flask,render_template

#flask obj
app = Flask(__name__)


#dummy data

all_posts = [

    {   'title':'Post1',

        'content':'this is my content',
        'author':"Kush"
    },


    {   'title':'Post2',

        'content':'this is my content2'
    }




]





@app.route("/")
def index():
    return render_template('index.html')

@app.route("/posts")
def posts():
    return render_template('post.html',posts = all_posts)

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


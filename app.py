from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy helps to interact with databaselike Mysql,postgrlsql with flask like app
from datetime import datetime




#flask obj
app = Flask(__name__)
#database path and add to data
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db  = SQLAlchemy(app)
#it will connect add flask to database

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#commands for python shell to connect darabase
#from app import db
#db.create_all()
#from app import className
#classname.query.all()    it will show the list of all the blog post in the database
#db.session.add(classname(put the variable name and their values here))


#Databse operations
#BlogPost.query.filter_by(author = "kush").all()
#BlogPost.query.get(id) this take blog post by id no
# >>> db.session.delete( BlogPost.query.get(3)) >>> db.session.commit() Delete a post
# >>> BlogPost.query.get(1).title = "New POSSSSSr"  >>> db.session.commit()  Change the variables
    # represent the database
    def __repr__(self):
        return "Blog Post "+str(self.id)

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

@app.route("/posts",methods = ['GET','POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
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


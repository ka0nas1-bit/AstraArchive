from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app) 



class Table(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    intro = db.Column(db.String(300), nullable = False)
    text = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return "<Table %r>" % self.id



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")



@app.route("/posts")
def posts():
    posts = Table.query.all()
    return render_template("posts.html", posts=posts)



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        intro = request.form['intro']

        post = Table(title=title, text=text, intro=intro)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return 'After add article happened error, sorry'

    else:
        return render_template("create.html")







if __name__ == "__main__":
    app.run(debug=True)
    

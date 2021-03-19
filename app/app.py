from flask import Flask, render_template, request, session, redirect, url_for
from models.models import Post, User
from models.database import db_session,Base
from datetime import datetime
from app import key
from hashlib import sha256
from datetime import datetime,date
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = key.SECRET_KEY


@app.route("/")
@app.route("/index",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        if "user_name" in session:
            name = session["user_name"]
            posts = Post.query.order_by(Post.due,Post.title).all()
            all_user = User.query.order_by(User.user_name).all()
            title_name = 'index'

            return render_template("index.html", name=name, posts=posts, all_user=all_user, today=date.today(),title_name=title_name)
        else:
            return redirect(url_for("top", status="logout"))
    else:
        title = request.form.get('title')
        detail = request.form.get('detail')
        due = request.form.get('due')
        due = datetime.strptime(due, '%Y-%m-%d')
        user_name = session['user_name']
        
        new_post = Post(title=title, detail=detail, due=due, user_name=user_name)
        db_session.add(new_post)
        db_session.commit()

        return redirect('/index')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/detail/<int:id>')
def read(id):
    name = session["user_name"]
    post = Post.query.get(id)
    return render_template('detail.html', post=post, today=date.today(),name=name)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')
        post.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')

        db_session.commit()
        return redirect('/')

    return render_template('detail.html', post=post)


@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)

    db_session.delete(post)
    db_session.commit()
    return redirect('/index')


@app.route("/top")
def top():
    status = request.args.get("status")
    title_name = 'top'
    return render_template("top.html", status=status,title_name=title_name)

@app.route("/login", methods=["post"])
def login():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        if user.hashed_password == hashed_password:
            session["user_name"] = user_name
            return redirect(url_for("index"))
        else:
            return redirect(url_for("top", status="wrong_password"))
    else:
        return redirect(url_for("top", status="user_notfound"))

@app.route("/newcomer")
def newcomer():
    status = request.args.get("status")
    title_name = 'newcomer'
    return render_template("newcomer.html", status=status, title_name=title_name)

@app.route("/registar", methods=["post"])
def registar():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return redirect(url_for("newcomer", status="exist_user"))
    else:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        user = User(user_name, hashed_password)
        db_session.add(user)
        db_session.commit()
        session["user_name"] = user_name
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top", status="logout"))


if __name__ == "__main__":
    app.run()

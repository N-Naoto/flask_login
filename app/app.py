from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    name = request.args.get('name')
    words = ['月','火','水','木','金','土','日']
    return render_template('index.html',name=name,words=words)

@app.route('/index',methods=['post'])
def post():
    name = request.form['name']
    words = ['月','火','水','木','金','土','日']
    return render_template('index.html',name=name,words=words)

if __name__ == '__main__':
    app.run()
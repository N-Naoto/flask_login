from flask import Flask,render_template,request

from models.models import OnegaiContent

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    name = request.args.get('name')
    all_onegai = OnegaiContent.query.all()
    return render_template('index.html',name=name,all_onegai=all_onegai)

@app.route('/index',methods=['post'])
def post():
    name = request.form['name']
    all_onegai = OnegaiContent.query.all()
    return render_template('index.html',name=name,all_onegai=all_onegai)

if __name__ == '__main__':
    app.run()
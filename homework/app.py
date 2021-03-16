from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
app=Flask(__name__)
app.config['SECRET_KEY'] = 'abc654_@123dda'

#使用GET方法，首頁
@app.route("/")
def index():
    return render_template("index.html")

#使用POST方法，驗證帳號密碼
@app.route("/signin",methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        session["account"]=account
        session["password"]=password
        return redirect("/member")
    else:
        return redirect("/error")
@app.route("/member")
def member():
    if session["account"]== "test" and session["password"]== "test":
        return render_template("member.html")
    else:
        return redirect('/')
    

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/signout")
def signout():
    session['account'] = None
    session['password'] = None
    return redirect('/')


app.run(port=3000)

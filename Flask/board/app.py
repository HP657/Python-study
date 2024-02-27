from flask import Flask, request, render_template, redirect, url_for, make_response
from db import DB


db = DB("데이터베이스명", "유저명", "비밀번호")


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def main():
    ID = request.cookies.get('ID')
    if ID:
        return render_template("main.html", ID=ID)
    else:
        return render_template("main.html")

@app.route("/join", methods=['POST', 'GET'])
def join():
    if request.method == 'POST':
        userID = request.form.get("userID")
        PW1 = request.form.get("PW1")
        PW2 = request.form.get("PW2")

        if db.select_user(userID):
            return render_template('join.html', message='이미 존재하는 아이디입니다.')
        elif PW1 == PW2:
            db.insert_user(userID, PW1)
            return render_template('join.html', message='회원가입되었습니다.', clear=True)
        else:
            return render_template('join.html', message='비밀번호가 일치하지 않습니다. 다시 입력해주세요.')
    return render_template('join.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userID = request.form.get("userID")
        password = request.form.get("password")
        
        if db.select_user_password(userID, password):
            resp = make_response(redirect(url_for('main')))
            resp.set_cookie('ID', userID)
            return resp
        else:
            return render_template('login.html', message='아이디 또는 비밀번호가 일치하지 않습니다.')
    return render_template("login.html")

@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for('main')))
    resp.delete_cookie('ID')
    return resp

@app.route("/quit")
def quit():
    ID = request.cookies.get('ID')
    if ID:
        db.delete_user(ID)
        resp = make_response(redirect(url_for('logout')))
        return resp
    else:
        return redirect(url_for('login'))

@app.route("/gaesi", methods=['GET','POST'])
def gaesi():
    if request.method == 'POST':
        return redirect(url_for("gaesi"))
    ID = request.cookies.get('ID')
    posts = db.select_post()
    return render_template("gaesi.html", posts=posts, ID=ID)

@app.route("/add_post", methods=['POST'])
def add_post():
    ID = request.cookies.get('ID')
    title = request.form.get("title")
    content = request.form.get("content")
    db.insert_post(ID, title, content)
    return redirect(url_for("gaesi"))

@app.route("/del_post/<post_id>", methods=['POST','GET'])
def del_post(post_id):
    db.delete_post(post_id)
    return redirect(url_for("gaesi"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
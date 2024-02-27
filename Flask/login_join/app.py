from flask import Flask, request, render_template, redirect, url_for, make_response
import psycopg2


def db(men_sql, params):
    global conn, cur
    cur.execute(men_sql, params)
    conn.commit()
    return cur


conn = psycopg2.connect(
        database="데이터베이스명",
        user="유저명",
        password="비밀번호"
    )
cur = conn.cursor()


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

        cur = db("SELECT * FROM 테이블명 WHERE ID = %s;", (userID,))
        if cur.fetchone():
            return render_template('join.html', message='이미 존재하는 아이디입니다.')
        elif PW1 == PW2:
            db("INSERT INTO 테이블명 VALUES (%s, %s);", (userID, PW1))
            return render_template('join.html', message='회원가입되었습니다.', clear=True)
        else:
            return render_template('join.html', message='비밀번호가 일치하지 않습니다. 다시 입력해주세요.')
    return render_template('join.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userID = request.form.get("userID")
        password = request.form.get("password")
        
        cur = db("SELECT * FROM 테이블명 WHERE ID = %s AND PW = %s;", (userID, password))
        result = cur.fetchone()
        if result:
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
        db("DELETE FROM 테이블명 WHERE ID = %s;", (ID,))
        resp = make_response(redirect(url_for('logout')))
        return resp
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host="0.0.0.0")

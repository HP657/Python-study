import psycopg2

class DB:
    def __init__(self, database, user, password):
        self.conn = psycopg2.connect(
        database=database,
        user=user,
        password=password,
    )
        self.cur = self.conn.cursor()

    def execute_query(self, query, params):
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur
    
    def select_user(self, userID):
        return self.execute_query("SELECT * FROM 유저테이블 WHERE user_id = %s;", (userID,)).fetchone()

    def select_user_password(self, userID, password):
        return self.execute_query("SELECT * FROM 유저테이블 WHERE user_id = %s AND user_pw = %s;", (userID, password)).fetchone()

    def insert_user(self, userID, password):
        self.execute_query("INSERT INTO 유저테이블 VALUES (%s, %s);", (userID, password))

    def delete_user(self, userID):
        self.execute_query("DELETE FROM 유저테이블 WHERE user_id = %s;", (userID,))

    def insert_post(self, user_id, title, content):
        self.execute_query("INSERT INTO 게시물테이블 (user_id, title, content) VALUES (%s, %s, %s)", (user_id, title, content,))

    def select_post(self):
        return self.execute_query("SELECT * FROM 게시물테이블 ORDER BY created_at DESC",()).fetchall()
    
    def delete_post(self, post_id):
        self.execute_query("DELETE FROM 게시물테이블 WHERE post_id=%s", (post_id,))
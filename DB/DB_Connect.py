import psycopg2

# PostgreSQL에 연결
conn = psycopg2.connect(
    database="dbcon",
    user="admin",
    password="hyojun5070!"
)

# 커서 생성
cur = conn.cursor()

while True:
    mung = input("SQL문 입력:")
    if mung == 'FIN':
        break
    else:
        cur.execute(mung)
        if mung.startswith('SELECT'):
            result = cur.fetchall()
            print(result)
        conn.commit()

# 연결 종료
cur.close()
conn.close()

import sqlite3

def connect_db(db_name):
    try:
        # DB 생성 (오토 커밋)
        conn_db = sqlite3.connect(f'{db_name}.db', isolation_level=None)
        return conn_db
    except Exception as e:
        print(e)

def make_db(db_name):
    conn = connect_db(db_name).cursor()

    # 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
    conn.execute("CREATE TABLE IF NOT EXISTS ZombieMOD \
        (id integer PRIMARY KEY, title text, description text, time_updated integer)")
    
    conn.close()


def insert_db(db_name, mod_id, json_title, json_description, json_time_updated):
    c = connect_db(db_name)

    # 데이터 삽입 방법 1
    c.execute(f"INSERT INTO ZombieMOD \
        VALUES({int(mod_id)}, '{json_title}', '{json_description}', {int(json_time_updated)})")

    c.close()


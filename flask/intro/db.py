

import psycopg2

db_config={
    'dbname':'postgres',
    'user':'postgres.erojatpkqtqexubknucv',
    'password':'4zY63KNsPFznj2oX',
    'host':'aws-0-ap-south-1.pooler.supabase.com',
    'port':'5432'
}

class DB():
    def __init__(self) -> None:
        try:
            conn=psycopg2.connect(**db_config)
            self.conn = conn
            cur=conn.cursor()
            self.cur=cur
        except Exception as e:
            print(f"an error occured:{e}")
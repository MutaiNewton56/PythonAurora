import psycopg2

db_config={
    'dbname':'postgres',
    'user':'postgres.gcvllmlwgjpzsqshrugs.dasda',
    'password':'tetYxiJEwcNfvaov',
    'host':'aws-0-eu-west-2.pooler.supabase.com',
    'port':'5432'
}

def connection():
    try:
        conn=psycopg2.connect(**db_config)
        print("Conncetion Establish")
        cur=conn.cursor()

        # Fetch results
        cur.execute("""
         SELECT table_name 
         FROM information_schema.tables
         where table_schema='public'
        """)

        tables=cur.fetchall()
        print("List of all tables")

        for table in tables:
            print(table[0])

        cur.close()
        conn.close()

    except Exception as e:
        print(f"an error occured:{e}")

connection()
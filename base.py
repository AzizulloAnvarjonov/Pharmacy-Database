import psycopg2 as psql



class Database:
    @staticmethod
    def connect(host, database, user, password, query):
        postgres_db = psql.connect(host=host, database=database, user=user, password=password)
        cursor = postgres_db.cursor()
        cursor.execute(query)
        postgres_db.commit()
        return "Successful"

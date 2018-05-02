import psycopg2


class Database:

    conn = psycopg2.connect(database="myBlog", user="myBlog", password="myBlog", host="postgres", port="5432")
    db = conn.cursor()

    def retrieve_request(self, sql_command):
        try:
            self.db.execute(sql_command)
            records = self.db.fetchall()
            return records

        except (Exception, psycopg2.DatabaseError) as error:
            return error


    def request(self, sql_command):
        try:
            self.db.execute(sql_command)
            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            return error


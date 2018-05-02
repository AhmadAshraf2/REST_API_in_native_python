from dal.db_requests import *
import json


class Blog:

    recipe_id = 0
    name = ''
    prep_time = ''
    diff = 0
    vegan = False

    def __init__(self, blog_id, title, content, category):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.category = category

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def save_blog(self):
        db = Database()
        sql_command = "INSERT INTO blogs (ID, title, content, category) VALUES ({}, '{}', '{}', '{}');"
        sql_command = sql_command.format(self.blog_id, self.title, self.content, self.category)
        result = db.request(sql_command)

        return result

    @staticmethod
    def del_blog(blog_id):
        db = Database()
        sql_command = "DELETE FROM blogs WHERE ID={}".format(blog_id)
        result = db.request(sql_command)
        return result

    @staticmethod
    def get_blog(blog_id):
        db = Database()
        blogs = []
        sql_command = "Select * from blogs"

        if blog_id:
            sql_command = "Select * from blogs where ID={}".format(blog_id)

        records = db.retrieve_request(sql_command)

        for record in records:
            blogs.append(Blog(record[0], record[1], record[2], record[3]))

        return blogs

    def update_blog(self):
        db = Database()
        sql_command = "UPDATE blogs SET title='{}', content='{}', category='{}'  WHERE ID={};"
        sql_command = sql_command.format(self.title, self.content, self.category, self.recipe_id)
        result = db.request(sql_command)

        return result

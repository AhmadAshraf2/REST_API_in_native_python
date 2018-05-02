from authentication.JWT_auth import *
from models.blog_model import *


class BlogController:

    @staticmethod
    @Authenticator.validate
    def add_blog(request=None, record=None):
        blog_id = request.path.split('/')[-1]
        blog = Blog(blog_id, record['title'], record['content'], record['category'])
        response_message = blog.save_blog()

        return response_message

    @staticmethod
    @Authenticator.validate
    def del_blog(request=None, record=None):
        blog_id = request.path.split('/')[-1]
        response_message = Blog.del_blog(blog_id)
        return response_message

    @staticmethod
    def get_blog(request):
        blog_id = request.path.split('/')[-1]
        records = Blog.get_blog(blog_id)
        return serialize(records) if records else None

    @staticmethod
    @Authenticator.validate
    def update_blog(request=None, record=None):
        blog_id = request.path.split('/')[-1]
        blog = Blog(blog_id, record['title'], record['content'], record['category'])
        response_message = blog.update_blog()

        return response_message

    @staticmethod
    def list_blogs():
        records = Blog.get_blog(None)
        return serialize(records) if records else None


def serialize(records):
    records = [record.toJSON() for record in records]
    return "[{}]".format(''.join(records))



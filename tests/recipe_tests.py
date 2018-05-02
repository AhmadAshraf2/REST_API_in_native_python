import json
import unittest
import requests
import jwt


class TestBlog(unittest.TestCase):

    def setUp(self):
        pass

    def test_1_add_blog(self):
        data = {"title": "iphone vs android", "content": "12345", "category": "technology"}
        data = jwt.encode(data, 'secret', algorithm='HS256')
        response = requests.post('http://0.0.0.0:80/blog/1', data=data)
        self.assertEqual(response.text, 'blog added')

    def test_2_get_blog(self):
        response = requests.get('http://0.0.0.0:80/blog/1')
        blog = json.loads(response.text)[0]
        self.assertEqual(blog['blog_id'], 1)

    def test_3_update_blog(self):
        data = {"title": "iphone vs android", "content": "54321", "category": "technology"}
        data = jwt.encode(data, 'secret', algorithm='HS256')
        response = requests.put('http://0.0.0.0:80/blog/1', data=data)
        self.assertEqual(response.text, 'updated record')

    def test_5_del_blog(self):
        data = {'token': 'test'}
        data = jwt.encode(data, 'secret', algorithm='HS256')
        response = requests.delete('http://0.0.0.0:80/blog/1', data=data)
        self.assertEqual(response.text, 'record deleted')


if __name__ == '__main__':
    unittest.main()
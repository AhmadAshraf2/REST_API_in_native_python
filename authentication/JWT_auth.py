import jwt
from controllers.blog_controller import *


class Authenticator:

    @staticmethod
    def get_request_body(request):
        length = int(request.headers.get('content-length'))
        record = request.rfile.read(length).decode('utf-8')
        try:
            return jwt.decode(record, 'secret', algorithms=['HS256'])
        except:
            return None

    @staticmethod
    def validate(request_method):

        def check_token(*args,):
            record = Authenticator.get_request_body(*args)

            if record:
                return request_method(*args, record)

            return 'You shall not pass!!!! 401: Authentication error'

        return check_token

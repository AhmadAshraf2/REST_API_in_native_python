class Response:

    @staticmethod
    def response_200(request, response_message, content_type):
            response_message = bytes('200: ' + response_message, 'utf-8')
            request.send_response(200)
            request.send_header('Content-Type', content_type)
            request.end_headers()
            request.wfile.write(response_message)

    @staticmethod
    def response_400(request, response_message='record does not exist'):
            request.send_response(400, '400 Bad Request: ' + response_message)
            request.send_header('Content-Type', 'text/plain')
            request.end_headers()
            request.wfile.write(bytes('400 Bad Request: ' + response_message, 'utf-8'))

    @staticmethod
    def response_409(request, response_message):
        response_message = bytes('409: Conflict: ' + response_message, 'utf-8')
        request.send_response(409)
        request.send_header('Content-Type', 'text/plain')
        request.end_headers()
        request.wfile.write(response_message)

    @staticmethod
    def response_401(request, response_message):
        response_message = bytes(response_message, 'utf-8')
        request.send_response(401)
        request.send_header('Content-Type', 'text/plain')
        request.end_headers()
        request.wfile.write(response_message)

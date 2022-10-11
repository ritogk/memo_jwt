from flask import make_response, Response


class base_response:
    @classmethod
    def generate_response(self, body: dict) -> Response:
        response = make_response(body)
        response.headers.set('Content-Type', 'application/json')
        response.headers.add('X-Content-Type-Options', 'nosniff')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

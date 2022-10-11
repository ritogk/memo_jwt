import json
import jwt
from functools import wraps
from flask import request, current_app, Response


def validate_jwt(fnc):
    # jwt検証用のmiddleware
    @wraps(fnc)
    def decorate(*args, **kwargs):
        token = request.cookies.get('token', None)
        print('★★★★')
        if token == None:
            return Response(response=json.dumps({'message': 'jwtなし'}), status=401)
        try:
            result = jwt.decode(token.encode(
                'utf-8'), current_app.config['JWT_SECRET'], algorithms="HS256")
        except:
            return Response(response=json.dumps({'message': 'jwt改ざん検知'}), status=401)
        return fnc(*args, **kwargs)
    return decorate

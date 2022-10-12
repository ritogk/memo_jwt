import jwt
from Config import Config


class JwtService:
    @classmethod
    def generate_jwt(self, content: dict) -> str:
        secret = Config.getInstance().JWT_SECRET
        return jwt.encode(content, secret, algorithm="HS256").decode('utf-8')

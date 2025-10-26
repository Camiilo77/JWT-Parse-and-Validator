import jwt

class JWTCrypto:
    @staticmethod
    def verify_signature(token, secret, algorithm="HS256"):
        try:
            jwt.decode(token, secret, algorithms=[algorithm])
            return True
        except jwt.InvalidTokenError:
            return False

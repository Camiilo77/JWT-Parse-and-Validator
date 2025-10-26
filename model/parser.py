import base64
import json
from .lexer import JWTLexer

class JWTParser:
    def __init__(self):
        self.lexer = JWTLexer()

    def parse(self, jwt_string):
        tokens = self.lexer.tokenize(jwt_string)
        return {
            'HEADER': tokens[0][1],
            'PAYLOAD': tokens[2][1],
            'SIGNATURE': tokens[4][1]
        }

    def decode_base64url(self, base64url_string):
        missing_padding = len(base64url_string) % 4
        if missing_padding:
            base64url_string += '=' * (4 - missing_padding)
        decoded = base64.urlsafe_b64decode(base64url_string.encode()).decode()
        try:
            return json.loads(decoded)
        except Exception as e:
            return {"error": str(e)}

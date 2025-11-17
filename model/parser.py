import json
from .lexer import JWTLexer
from .encoder import JWTEncoder

class JWTParser:
    """
    Parser para crear estructura objeto JWT y decodificar las partes.
    """
    def __init__(self):
        self.lexer = JWTLexer()

    def parse(self, jwt_string: str):
        """
        Retorna dict {'HEADER', 'PAYLOAD', 'SIGNATURE'}; valida y descompone el JWT.
        """
        tokens = self.lexer.tokenize(jwt_string)
        return {
            'HEADER': tokens[0][1],
            'PAYLOAD': tokens[2][1],
            'SIGNATURE': tokens[4][1]
        }

    def decode_base64url(self, base64url_string: str):
        """
        Decodifica la cadena base64url y retorna dict JSON o error.
        """
        return JWTEncoder.decode_base64url_to_json(base64url_string)

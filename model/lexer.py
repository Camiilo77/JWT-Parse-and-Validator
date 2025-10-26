from .automata import Base64URLDFA

class JWTLexer:
    def tokenize(self, jwt_string):
        parts = jwt_string.split('.')
        if len(parts) != 3:
            raise ValueError("JWT malformado")
        dfa = Base64URLDFA()
        for part in parts:
            if not dfa.process(part):
                raise ValueError("Parte no es Base64URL válida por autómata")
        return [
            ('HEADER', parts[0]),
            ('SEPARATOR', '.'),
            ('PAYLOAD', parts[1]),
            ('SEPARATOR', '.'),
            ('SIGNATURE', parts[2])
        ]

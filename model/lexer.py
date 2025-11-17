from .automata import Base64URLDFA

class JWTLexer:
    """
    Lexer para descomponer el JWT en sus partes léxicas y validar cada una con DFA.
    """
    def tokenize(self, jwt_string: str):
        """
        Retorna lista de tokens léxicos si el JWT es correcto, lanza excepción si no lo es.
        """
        parts = jwt_string.split('.')
        if len(parts) != 3:
            raise ValueError("JWT malformado: no tiene 3 partes")
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

class Base64URLDFA:
    """
    DFA para validar cadenas en alfabeto Base64URL.
    Estados: q0 (inicial/aceptante), qerr (error).
    """

    ALPHABET = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_")

    def __init__(self):
        self.state = 'q0'

    def process(self, input_str: str) -> bool:
        """
        Procesa la entrada y retorna True si es válida Base64URL.
        """
        self.state = 'q0'
        for symbol in input_str:
            if symbol in self.ALPHABET:
                continue
            else:
                self.state = 'qerr'
                break
        return self.state == 'q0' and bool(input_str)

    def reset(self):
        self.state = 'q0'


class JWTStructureDFA:
    """
    DFA para validar la estructura formal de un JWT: HEADER.PAYLOAD.SIGNATURE,
    donde cada parte es una cadena Base64URL válida.
    """
    def process(self, input_str: str) -> bool:
        parts = input_str.split('.')
        if len(parts) != 3:
            return False
        dfa = Base64URLDFA()
        return all(dfa.process(part) for part in parts)

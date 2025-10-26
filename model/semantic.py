import time

class JWTSemanticAnalyzer:
    def __init__(self):
        self.valid_algorithms = ['HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512']
        self.errors = []
        self.warnings = []

    def analyze(self, header, payload):
        self.errors.clear()
        self.warnings.clear()
        if not isinstance(header, dict):
            self.errors.append('Header no es diccionario')
            return
        if 'alg' not in header or header['alg'] not in self.valid_algorithms:
            self.errors.append('Algoritmo inválido')
        if 'typ' not in header or header['typ'] != 'JWT':
            self.errors.append('Tipo inválido')
        now = int(time.time())
        if 'exp' in payload and payload['exp'] < now:
            self.errors.append('Token ha expirado')
        if 'nbf' in payload and payload['nbf'] > now:
            self.errors.append('Token no es válido aún')
        if 'iat' in payload and (payload['iat'] > now + 300):
            self.warnings.append('Token emitido en el futuro')

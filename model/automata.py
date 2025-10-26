class Base64URLDFA:
    ALPHABET = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_")
    
    def __init__(self):
        self.state = 'q0'
        self.accepting = 'q0'

    def process(self, input_str):
        self.state = 'q0'
        for symbol in input_str:
            if symbol in self.ALPHABET:
                # Permanece en estado aceptante
                continue
            else:
                self.state = 'qerr'
                break
        return self.state == self.accepting and len(input_str) > 0

    def reset(self):
        self.state = 'q0'

# Prueba un token base64url
dfa = Base64URLDFA()
test_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
print("¿Base64URL válido?:", dfa.process(test_token))  # True
print("¿Base64URL inválido?:", dfa.process("eyJhbGci:###"))  # False


class JWTStructureDFA:
    def process(self, input_str):
        parts = input_str.split('.')
        if len(parts) != 3:
            return False
        dfa = Base64URLDFA()
        for part in parts:
            if not dfa.process(part):
                return False
        return True

# Prueba estructura
jwt_dfa = JWTStructureDFA()
print(jwt_dfa.process("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"))  # True
print(jwt_dfa.process("bad.token.string"))  # False

class JWTTDerivationTree:
    def __init__(self, jwt_string):
        self.jwt_string = jwt_string
        self.header, self.payload, self.signature = self.jwt_string.split('.')
    
    def show_tree(self):
        print("JWT")
        print("├── HEADER:    ", self.header)
        print("├── PAYLOAD:   ", self.payload)
        print("└── SIGNATURE: ", self.signature)

tree = JWTTDerivationTree("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
tree.show_tree()
# Salida esperada:
# JWT
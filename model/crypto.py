import jwt

class JWTCrypto:
    """
    Clase para verificar la firma de un JWT usando PyJWT.
    """
    @staticmethod
    def verify_signature(token: str, secret: str, algorithm="HS256") -> bool:
        """
        Verifica la firma criptográfica del JWT con una clave secreta.
        """
        try:
            jwt.decode(token, secret, algorithms=[algorithm])
            return True
        except jwt.InvalidTokenError as e:
            print(f"Firma inválida: {str(e)}")
            return False

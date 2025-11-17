import base64
import json

class JWTEncoder:
    """
    Codificador y decodificador entre JSON y Base64URL.
    """
    @staticmethod
    def encode_json_to_base64url(data: dict) -> str:
        """
        Convierte un dict JSON en una cadena base64url (como en JWT).
        """
        json_str = json.dumps(data, separators=(',', ':'))
        base64url = base64.urlsafe_b64encode(json_str.encode()).decode().rstrip('=')
        return base64url

    @staticmethod
    def decode_base64url_to_json(base64url_string: str) -> dict:
        """
        Convierte una cadena base64url en json, manejando padding.
        """
        padding = '=' * ((4 - len(base64url_string) % 4) % 4)
        try:
            decoded = base64.urlsafe_b64decode(base64url_string + padding).decode()
            return json.loads(decoded)
        except Exception as e:
            return {"error": f"Base64URL/JSON inválido ({str(e)})"}

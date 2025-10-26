import base64
import json

class JWTEncoder:
    @staticmethod
    def encode_json_to_base64url(data):
        json_str = json.dumps(data)
        return base64.urlsafe_b64encode(json_str.encode()).decode().rstrip('=')

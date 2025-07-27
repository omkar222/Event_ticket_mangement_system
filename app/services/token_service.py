import secrets

class TokenService:
    @staticmethod
    def generate_token():
        return secrets.token_hex(32)
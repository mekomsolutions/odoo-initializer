from .base_loader import BaseLoader


class OAuthLoader(BaseLoader):
    model_name = "auth.oauth.provider"
    folder = "auth_providers"
    filters = {}

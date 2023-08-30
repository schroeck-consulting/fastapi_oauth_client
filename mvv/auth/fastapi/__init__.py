#  _____      _                         _      _____ _____
# /  ___|    | |                       | |    |_   _|_   _|
# \ `--.  ___| |__  _ __ ___   ___  ___| | __   | |   | |
#  `--. \/ __| '_ \| '__/ _ \ / _ \/ __| |/ /   | |   | |
# /\__/ / (__| | | | | | (_) |  __/ (__|   <   _| |_  | |
# \____/ \___|_| |_|_|  \___/ \___|\___|_|\_\  \___/  \_/

from .endpoints import token_auth_scheme, auth_router, verify_token
from .settings import oauth_settings as config
from .token_verification import VerifyToken

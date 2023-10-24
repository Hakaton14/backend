from hakaton.app_data import DB_SQLITE
from hakaton.settings import *  # noqa F403

DATABASES = DB_SQLITE

SECRET_KEY = 'test_secret_key'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_test')  # noqa F405

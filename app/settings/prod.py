from app.settings import DATABASES
from .base import *


DATABASES = {}
db_from_env = dj_database_url.config(default='DATABASE_URL', conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)

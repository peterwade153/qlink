import dj_database_url
from .base import *


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

DATABASES['default'].update(dj_database_url.config(
    conn_max_age=500, ssl_require=True),
    engine='heroku_connect.db.backends.postgres',
)

import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI  = "192.168.99.100:32768"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


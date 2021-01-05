import os

ROOT = os.path.dirname(os.path.abspath(__file__))

DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'channel')
DB_PASSWORD = os.environ.get('DB_USER', 'channel')
DB_NAME = os.environ.get('DB', 'sdc_channel')

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sdc_channel.constants import DB_NAME, DB_HOST, DB_PASSWORD, DB_USER

Entity = declarative_base()
Session = sessionmaker(
    bind=create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
)
_session = None


def session():
    global _session
    if not _session:
        _session = Session()
    return _session


def close_session():
    global _session
    if _session:
        _session.close()
        _session = None

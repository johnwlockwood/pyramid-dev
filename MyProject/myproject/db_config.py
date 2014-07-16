import os

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


DB_FMT_STR = 'mysql://{user}:{passwd}@{host}:{port}'
DB_NAME = 'mypyramidproject'


def get_db_connection_dict():
    """
    Build a dict of connection arguments from the environment.

    :return:
    """
    return dict(
        host=os.environ['MYSQL_PORT_3306_TCP_ADDR'],
        user='root',
        port=int(os.environ['MYSQL_PORT_3306_TCP_PORT']),
        passwd=os.environ['MYSQL_ENV_MYSQL_ROOT_PASSWORD'])


def get_db_engine():
    """
    Create the database engine connection
    and attempt to use the database mypyramidproject,
    if it doesn't exist, create it, then use it.

    :return: A database engine.
    """
    db_kwargs = get_db_connection_dict()
    engine = create_engine(DB_FMT_STR.format(**db_kwargs))
    try:
        engine.execute("USE {}".format(DB_NAME))
    except OperationalError:
        engine.execute("CREATE DATABASE {}".format(DB_NAME)) #create db
        engine.execute("USE {}".format(DB_NAME)) # select new db
    return engine

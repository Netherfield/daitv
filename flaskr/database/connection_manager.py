from database import mongodb_config
from pymongo import MongoClient
from database import sql_config
from database import sqlite_config
import mysql.connector
import sqlite3


def sql_type():
    """
    da implementare, in sospeso finchè non si implenta la tabella logging
    :return:
    """
    DB_CONFIG = {
        "host": sql_config.DB_HOST,
        "user": sql_config.DB_USER,
        "password": sql_config.DB_PASSWORD,
        "database": sql_config.DB_NAME
    }
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Exception as e:
        print(f"errore: {e}")
        return None


def mongodb_type():
    """
    ritorna la connessione al Mongo DB
    else: None
    :return:
    """
    try:
        client = MongoClient(mongodb_config.URI_MONGO_DB)
        return client[mongodb_config.DB_NAME]
    except Exception as e:
        print(f"errore: {e}")
        return None

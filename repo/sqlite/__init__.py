'''
Implements the AbstractRepo interface using sqlite3.
'''

import sqlite3
import os
from ..abstract import AbstractRepo

class SQLiteRepo(AbstractRepo):
    def __init__(self, config=None):
        self.config = {
            'db_name': 'db.sqlite3'
        }
        self.db_name = self.config['db_name']
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS data (key text, value text)')
        self.conn.commit()

    def save(self, key, value):
        self.cursor.execute('INSERT INTO data VALUES (?, ?)', (key, value))
        self.conn.commit()

    def get(self, key):
        self.cursor.execute('SELECT value FROM data WHERE key=?', (key,))
        return self.cursor.fetchone()[0]

    def delete(self, key):
        self.cursor.execute('DELETE FROM data WHERE key=?', (key,))
        self.conn.commit()

    def update(self, key, value):
        self.cursor.execute('UPDATE data SET value=? WHERE key=?', (value, key))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM data')
        return self.cursor.fetchall()

    def delete_all(self):
        self.cursor.execute('DELETE FROM data')
        self.conn.commit()

    def get_all_keys(self):
        self.cursor.execute('SELECT key FROM data')
        return self.cursor.fetchall()

    def get_config(self):
        return self.config

    def set_config(self, config):
        self.config = config

    def get_db_name(self):
        return self.db_name

    def set_db_name(self, db_name):
        self.db_name = db_name

    def get_conn(self):
        return self.conn

    def set_conn(self, conn):
        self.conn = conn

    def get_cursor(self):
        return self.cursor

    def set_cursor(self, cursor):
        self.cursor = cursor

    def __del__(self):
        self.conn.close()

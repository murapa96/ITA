'''
Implements json abstractrepo interface.
'''

import json
import os
from ..abstract import AbstractRepo

class JsonRepo(AbstractRepo):
    def __init__(self, config=None):
        self.config = {
            'db_name': 'db.json'
        }
        self.db_name = self.config['db_name']
        self.data = {}
        if os.path.exists(self.db_name):
            with open(self.db_name) as f:
                self.data = json.load(f)

    def save(self, key, value):
        self.data[key] = value
        self._save()

    def get(self, key):
        return self.data[key]

    def delete(self, key):
        del self.data[key]
        self._save()

    def update(self, key, value):
        self.data[key] = value
        self._save()

    def get_all(self):
        return self.data

    def delete_all(self):
        self.data = {}
        self._save()

    def get_all_keys(self):
        return self.data.keys()

    def get_config(self):
        return self.config

    def set_config(self, config):
        self.config = config

    def get_db_name(self):
        return self.db_name

    def set_db_name(self, db_name):
        self.db_name = db_name

    def _save(self):
        with open(self.db_name, 'w') as f:
            json.dump(self.data, f)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

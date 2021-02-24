from pymongo import MongoClient
from flask import current_app as app

class MongoConnections:
    '''
    Create this client once for each process, and reuse it for all operations.
    It is a common mistake to create a new client for each request, which is very inefficient.
    '''

    _g_db_connection = None
    def _get_db_connection(self):
        mongodb_server   = app.config.get('MONGODB_SERVER')
        mongodb_port     = app.config.get('MONGODB_PORT')
        mongodb_username = app.config.get('MONGODB_USERNAME')
        mongodb_password = app.config.get('MONGODB_PASSWORD')
        db_connection = MongoClient(mongodb_server, mongodb_port,maxPoolSize=200)
        if mongodb_username and mongodb_password:
            db_connection.the_database.authenticate(mongodb_username,mongodb_password, source='admin')
        return db_connection

    def connect(self,db_name,collection):
        self._intialize()
        database = self.db_connection[db_name]
        return database[collection]

    def  _intialize(self):
        if MongoConnections._g_db_connection is None:
            MongoConnections._g_db_connection = self._get_db_connection()
        self.db_connection = MongoConnections._g_db_connection
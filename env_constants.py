from logging import ERROR, INFO, DEBUG

"""
    Store the environment related configuration 
"""

from os import environ as env

class MongoDBConfigDevelopment:
    MONGODB_SERVER="localhost"
    MONGODB_PORT=27018
    MONGODB_POOLSIZE=200
    MONGODB_USERNAME=None
    MONGODB_PASSWORD=None

class MongoDBConfig:
    MONGODB_SERVER=env.get('MONGODB_SERVER')
    MONGODB_PORT=int(env.get('MONGODB_PORT',27017))
    MONGODB_POOLSIZE=int(env.get('MONGODB_POOLSIZE',200))
    MONGODB_USERNAME=env.get('MONGODB_USERNAME')
    MONGODB_PASSWORD=env.get('MONGODB_PASSWORD')


class EnvConstants(MongoDBConfig):
    LOG_LEVEL=ERROR
    SWAGGER_UI=True
    pass

class EnvConstantsDevelopment(MongoDBConfigDevelopment):
    LOG_LEVEL=DEBUG
    SWAGGER_UI=True
    pass

class EnvConstantsTesting(MongoDBConfigDevelopment):
    LOG_LEVEL=DEBUG
    SWAGGER_UI=False
    pass

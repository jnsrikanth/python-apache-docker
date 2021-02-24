import logging
import sys
print(sys.path)
import pymongo
sys.stdout=sys.stderr
print("wsgi started")
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/approot/api/app')
from app import app as application
application.root_path = '/home/approot/api/app'
application.secret_key = '$Secret@app'


import os, sys
from pymongo import MongoClient


database = MongoClient('localhost', 27017)
database.drop_database(sys.argv[1])

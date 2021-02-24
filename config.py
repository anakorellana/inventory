import psycopg2 as pg2
from flask import Flask


class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://anakarinaorellana:5432@localhost/anakarinaorellana"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123456'





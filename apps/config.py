# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Tedley Meralus
"""
import os
import psycopg2
from dotenv import load_dotenv
from decouple import config

class Config(object):
    load_dotenv() # load .env variables 
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App keys  
    SECRET_KEY = os.getenv('POSTGRES_USER')
    SECRET_KEY = os.getenv('POSTGRES_PASSWORD') 


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # This will connect to the postgres db container service named 'db' 
    # postgresql+psycopg2://{db_login}:{db_password}@db:5432/postgres
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/postgres'.format(
        config('DB_ENGINE', default='postgresql'),
        config('DB_USERNAME', default='postgres'),
        config('DB_PASS', default='postgres'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=5432),
        config('DB_NAME', default='postgres')
    )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}

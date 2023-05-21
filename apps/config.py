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
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD') 
    DB_USERNAME = os.getenv('DB_USER')
    DB_ENGINE = os.getenv('DB_ENGINE') 
    DB_PASS = os.getenv('POSTGRES_PASS')
    DB_HOST = os.getenv('POSTGRES_HOST') 
    DB_PORT = os.getenv('POSTGRES_PORT') 
    DB_NAME = os.getenv('POSTGRES_NAME')
    # Dev env variables 
    DEV_POSTGRES_USER = os.getenv('DEV_POSTGRES_USER')
    DEV_POSTGRES_PASSWORD = os.getenv('DEV_POSTGRES_PASSWORD') 
    DEV_DB_USERNAME = os.getenv('DEV_DB_USER')
    DEV_DB_ENGINE = os.getenv('DEV_DB_ENGINE') 
    DEV_DB_PASS = os.getenv('DEV_POSTGRES_PASS')
    DEV_DB_HOST = os.getenv('DEV_POSTGRES_HOST') 
    DEV_DB_PORT = os.getenv('DEV_POSTGRES_PORT') 
    DEV_DB_NAME = os.getenv('DEV_POSTGRES_NAME')


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # This will connect to the postgres db container service named 'db' 
    # postgresql+psycopg2://{db_login}:{db_password}@db:5432/postgres
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:{DB_PORT}/{DB_NAME}'.format(
        config('DB_ENGINE', default='{DB_ENGINE}'),
        config('DB_USERNAME', default='{DB_USERNAME}'),
        config('DB_PASS', default='{DB_PASS}'),
        config('DB_HOST', default='{DB_HOST}'),
        config('DB_PORT', default='{DB_PORT}'),
        config('DB_NAME', default='{DB_NAME}')
    )

class DevelopmentConfig(Config):
    DEBUG = True
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # This will connect to the postgres db container service named 'db' 
    # postgresql+psycopg2://{db_login}:{db_password}@db:5432/postgres
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{DEV_POSTGRES_USER}:{DEV_POSTGRES_PASSWORD}@db:{DEV_DB_PORT}/{DEV_DB_NAME}'.format(
        config('DB_ENGINE', default='{DEV_DB_ENGINE}'),
        config('DB_USERNAME', default='{DEV_DB_USERNAME}'),
        config('DB_PASS', default='{DEV_DB_PASS}'),
        config('DB_HOST', default='{DEV_DB_HOST}'),
        config('DB_PORT', default='{DEV_DB_PORT}'),
        config('DB_NAME', default='{DEV_DB_NAME}')
    )

class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Development': DevelopmentConfig,
    'Debug': DebugConfig
}

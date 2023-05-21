# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Tedley Meralus
"""
import os
import psycopg2
from dotenv import load_dotenv
from decouple import config

class Config(object):
    # load .env variables 
    env = os.getenv('ENVIRONMENT', 'development')
    dotenv_path = f'.env.{env}'
    load_dotenv(dotenv_path=dotenv_path)

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

    # This will connect to the postgres db container service using environment variables
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'+ os.environ['POSTGRES_USER']+ ":"+ os.environ['POSTGRES_PASSWORD']+ "@"+ os.environ['DB_HOST']+ ":"+ os.environ['DB_PORT']+ "/"+ os.environ['DB_NAME']

    SQLALCHEMY_TRACK_MODIFICATIONS = False 

class ProductionConfig(Config):
    DEBUG = False

    # load .env variables 
    env = os.getenv('ENVIRONMENT', 'prod')
    dotenv_path = f'.env.{env}'
    load_dotenv(dotenv_path=dotenv_path) 

class DevelopmentConfig(Config):
    DEBUG = True
    # load .env variables 
    env = os.getenv('ENVIRONMENT', 'prod')
    dotenv_path = f'.env.{env}'
    load_dotenv(dotenv_path=dotenv_path) 

class StagingConfig(Config):
    DEBUG = True
    # load .env variables 
    env = os.getenv('ENVIRONMENT', 'stage')
    dotenv_path = f'.env.{env}'
    load_dotenv(dotenv_path=dotenv_path) 

class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Development': DevelopmentConfig,
    'Staging': StagingConfig,
    'Production': ProductionConfig,
    'Debug': DebugConfig
}

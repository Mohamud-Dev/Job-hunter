import os

from flask import Flask, render_template, request


class Config:

    
    SECRET_KEY = '123erty'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vector:12345q@localhost/job_hunter'
    BASE_URL='https://jobs.github.com/positions.json?description={}'
    JOBS_URL='https://jobs.github.com/positions/{}.json?markdown=true'
    
    UPLOADED_PHOTOS_DEST ='app/static/images'
 
   


class ProdConfig(Config):
  
  
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
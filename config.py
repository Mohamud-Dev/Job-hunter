import os


class Config:
    BASE_URL='https://jobs.github.com/positions.json?description={}'
    JOBS_URL='https://jobs.github.com/positions/{}.json?markdown=true'
    SECRET_KEY = os.urandom(32)
   


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
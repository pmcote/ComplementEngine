import os
import urlparse

class Config(object):
    """
    Basic default global configuration variables not specific to any environment
    """
    SQLALCHEMY_ECHO = False
    SOMECOOLCONSTANT = 3 # an example variable you use throughout your application
    SECRET_KEY = 'verysecret'
    DEBUG = True



class DevelopmentConfig(Config):
    """ 
    The Development Configuration, provides default database and facebook credentials and
    configuration to run the application
    """ 
    SQLALCHEMY_DATABASE_URI = 'something local maybe?'
    FACEBOOK_APP_SECRET = "067838d5036c5db87ae2c21a3a37b3b5" #Example variables which change with environment
    FACEBOOK_APP_ID = "587574061260748"
    MONGODB_DB = "silly"
    MONGODB_USERNAME = ""
    MONGODB_PASSWORD = ""
    MONGODB_HOST = "localhost"
    MONGODB_PORT = "27017"


class ProductionConfig(DevelopmentConfig):
    '''
    Extends and overrides declarations from the DevelopmentConfiguration
    '''
    url = urlparse.urlparse(os.environ.get("MONGOHQ_URL", "FAILED TO GET MONGOHQURL"))
    MONGODB_DB = url.path[1:]
    MONGODB_USERNAME = url.username
    MONGODB_PASSWORD = url.password
    MONGODB_HOST = url.hostname
    MONGODB_PORT = url.port
    FACEBOOK_APP_SECRET = "87be773b3a871485f634c85d831ee752"
    FACEBOOK_APP_ID = "581157881916787"

    # FACEBOOK_APP_SECRET = "XXX" Example variables which change with environment
    # FACEBOOK_APP_ID = "XX"
    # SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_ROSE_URL")


def getConfig():
    ''' Should return the proper configuration based upon environmental 
        variables and or other subsequent tests. Currently only distinguishes
        between Heroku and 'other', defaulting other to a local development database.
        TODO: test for local development database, if failed, default to a remote
        database, there should be no need for a full postgres install to test 
        or write client/HTML/CSS/js.
    '''
    if os.environ.get('PYTHONHOME') != None and 'heroku' in os.environ.get('PYTHONHOME'): ##we are on Heroku!
        return ProductionConfig
    else:
        return DevelopmentConfig

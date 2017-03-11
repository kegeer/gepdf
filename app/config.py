class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    SECRET_KEY= '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/pdf-db?charset=utf8'

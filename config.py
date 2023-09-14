import os

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    LINE_PAY_ID = '1654645649'
    LINE_PAY_SECRET = '89d3d4609dc0feffb7971e8c39c4b221'

    STORE_IMAGE_URL = 'https://i.imgur.com/0KinQXT.jpg'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://m1016m:aynpduYUgaD2yAVFd8JLBgj2TPMPSWGD@dpg-cjbor97db61s73aeaou0-a.singapore-postgres.render.com/mspa_d63k'
    
class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')



    

    


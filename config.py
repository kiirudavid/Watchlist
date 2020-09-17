# MOVIE_API_KEY = '<c85da0de991a50053336d90226dd3651>'
# MOVIE_API_KEY = '<Movie API Key>'
# SECRET_KEY = '<Flask WTF Secret Key>'


import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('c85da0de991a50053336d90226dd3651')
    SECRET_KEY = os.environ.get('Flask WTF Secret Key')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/watchlist'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:maich000@localhost/watchlist'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
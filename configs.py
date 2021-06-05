class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost:3306/travel'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    SECRET_KEY = 'you-will-never-guess'

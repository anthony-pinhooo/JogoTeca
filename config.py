import os

SECRET_KEY = 'ikasbdiabsdiuabsdiubaisudbaiuobsudiaub'
SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{password}@{servidor}/{database}".format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        password = '',
        servidor = 'localhost',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
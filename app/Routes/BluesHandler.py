from app.Modules import Auth
from app.Modules import Note
from app.Modules import Star

from flask.app import Flask

def register_modules_blue(app: Flask):
    '''
    向 FlaskApp 注册每个模块的蓝图
    '''
    Auth.register_auth_blue(app)
    Note.register_note_blue(app)
    Star.register_star_blue(app)
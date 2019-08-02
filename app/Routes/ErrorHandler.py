from app.Utils import ErrorUtil, RespUtil
from app.Models.Message import Message

from app.Routes.GlobalErrorHandle import register_global_error_handler
from app.Modules import Auth
from app.Modules import Note
from app.Modules import Star

from flask.app import Flask

def register_error_forward(app: Flask):
    '''
    向 FlaskApp 添加错误转发，包括系统错误和模块内错误
    '''

    @app.errorhandler(404)
    def error_404(error: TypeError):
        return RespUtil.jsonRet(
            dict=ErrorUtil.getErrorMessageJson(error=error, title="Not Found"),
            code=ErrorUtil.NotFound
        )

    @app.errorhandler(405)
    def error_405(error: TypeError):
        return RespUtil.jsonRet(
            dict=ErrorUtil.getErrorMessageJson(error=error, title="Method Not Allowed"),
            code=ErrorUtil.MethodNotAllowed
        )

    @app.errorhandler(500)
    def error_500(error: TypeError):
        '''
        500 Error Forwarding
        '''

        glob = register_global_error_handler(error)
        auth = Auth.forward_auth_error(error)
        note = Note.forward_note_error(error)
        star = Star.forward_star_error(error)

        if not glob == None:
            return glob
        elif not auth == None:
            return auth
        elif not note == None:
            return note
        elif not star == None:
            return star
        else:
            return RespUtil.jsonRet(
                dict=ErrorUtil.getErrorMessageJson(error=error, title="Internal Server Error"),
                code=ErrorUtil.InternalServerError
            )

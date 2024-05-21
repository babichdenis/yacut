from http import HTTPStatus
from flask import jsonify, render_template

from . import app, db


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {'message': self.message}


@app.errorhandler(InvalidAPIUsage)
def handle_invalid_api_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(HTTPStatus.NOT_FOUND)
def handle_not_found_error(error):
    return render_template('errors/404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def handle_internal_server_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), HTTPStatus.INTERNAL_SERVER_ERROR


# Обработка ошибки по умолчанию
@app.errorhandler(Exception)
def handle_default_error(error):
    return jsonify(
        {'error': 'Internal Server Error'}), HTTPStatus.INTERNAL_SERVER_ERROR

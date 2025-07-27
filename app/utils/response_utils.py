from flask import jsonify

def success(data=None, message='Success', status_code=200):
    response = {
        'status': 'success',
        'message': message,
        'data': data
    }
    return jsonify(response), status_code

def error(message='Error', status_code=400, errors=None):
    response = {
        'status': 'error',
        'message': message,
        'errors': errors or {}
    }
    return jsonify(response), status_code
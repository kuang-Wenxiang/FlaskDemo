from commont.utils.status import status_msg


def to_dict_msg(code=200, data=None, msg=None):
    return {
        'status': code,
        'msg': msg if msg else status_msg[code],
        'data': data
    }

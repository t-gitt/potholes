from rest_framework.exceptions import APIException


class NoHolesFoundException(APIException):
    status_code = 404
    default_detail = 'No holes found'
    default_code = 'no_holes_found'
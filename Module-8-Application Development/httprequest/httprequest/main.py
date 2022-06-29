import sys

import functions_framework

@functions_framework.http
def is_valid_user(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    print("complete input json is {0}".format(request_json))
    if request_json and 'empid' in request_json:
        emp_id = request_json['name']
        if emp_id in [123,456,999]:
            return "user {0} is valid ".format(emp_id)
        else:
            return "User {0} is Invalid ".format(emp_id)






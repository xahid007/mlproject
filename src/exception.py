import sys


def error_message_detials(error, error_details:sys):
    '''
    Formulate the custom error message
    '''
    _,_,ex_tb = error_details.exc_info()

    file_name = ex_tb.tb_frame.f_code.co_filename
    line_number = ex_tb.tb_lineno
    message = str(error)
    error_message = "Error Occurred in file [{0}] in line [{1}] error message [{2}]".format(file_name,line_number, message)
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detials(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message

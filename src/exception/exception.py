import sys

def error_message(error, detail: sys):
    _, _, exc_tb = detail.exc_info()

    return f"""
Error occurred

File : {exc_tb.tb_frame.f_code.co_filename}

Line : {exc_tb.tb_lineno}

Error : {str(error)}
"""
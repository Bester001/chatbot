import sys

class customexception(Exception):
    def init(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb=error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename
        
    def str(self):
        return "error occured  in python script [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)) 
        
if name ==  "main":
    try:
        
        a=1/0
        
    except Exception as e:
        raise customexception(e,sys)
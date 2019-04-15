import pyfftw as FFTW

lib = {"library":None}

class backend:

    def __init__(self, library):
    
        if(library == "pyfftw"):
            self.backend_library = FFTW
            
    def set_args(self, arg1, arg2):
        
        self.arg_dict["arg1"]=arg1
        self.arg_dict["arg2"]=arg2
        lib["arg1"]=arg1
        lib["arg2"]=arg2
            
    def __enter__(self):
    
        """
        Code for changing the backend
        """
        self.arg_dict = {"arg1":"default planning_effort",
                         "arg2":"default threads"}
        lib["library"] = self.backend_library

        return self
        
    def __exit__(self, type, value, traceback):
        
        """
        Changing things back to default
        """
    
        lib["library"] = None
        del lib["arg1"]
        del lib["arg2"]
        
        
with backend("pyfftw") as backend_module:
    backend_module.set_args('FFTW_MEASURE',2)
    print(lib)
    
print(lib)
        

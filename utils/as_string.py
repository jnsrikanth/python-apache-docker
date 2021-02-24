class AsString():
    def __init__(self,value=None):
        self.name = value

    def __get__(self,obj,objtype):
        return self.name
    
    def __set__(self,obj,_value):
        raise NotImplementedError

    def __set_name__(self, owner, name):
        if not self.name: self.name = name
    
    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
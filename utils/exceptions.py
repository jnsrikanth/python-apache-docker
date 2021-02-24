class DomainError(Exception):
   def __init__(self,msg=None):
       self.message=msg if msg else "Something went wrong with server"
       self.code=500

class BadRequest(DomainError):
   def __init__(self,msg=None):
       self.message=msg if msg else "invalid request"
       self.code=400

class PartialError(DomainError):
    def __init__(self,msg=None):
       self.message=msg if msg else "partial error"
       self.code=200

class InternalServerError(DomainError):
   def __init__(self,msg=None):
       self.message=msg if msg else "Something went wrong with server"
       self.code=500

import os

ENV = bool(os.environ.get("ENV",false))
if ENV:
     heroku_config import Var as config
else:
    from local_config import Development as congig
    
    
  Var = config  

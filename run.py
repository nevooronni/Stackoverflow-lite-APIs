"""app initializer"""

import os
"""import os to get all that we had defined in .env our environment variables"""
from app import create_app
"""this is imported from the __init__.py file contained in the subdirectory called app"""

config_name = os.getenv("APP_SETTINGS") #GET THE APP SETTINGS FROM THE .env FILE

app = create_app(config_name)

if __name__ == '__main___':
  app.run()

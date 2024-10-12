#!/usr/bin/env python3
""" Module for setting up Blueprint and views import. """

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import views after app_views is defined to avoid circular import issues
from api.v1.views.index import *
from api.v1.views.users import *

# Call any required initialization after all imports are complete
User.load_from_file()  

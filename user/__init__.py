from flask import Blueprint



user_blu = Blueprint('user_blu',__name__,
                     static_folder='static',
                     url_prefix='/user')
					

from . import views






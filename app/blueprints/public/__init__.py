from flask import Blueprint

public_hp = Blueprint('public',
                      __name__,template_folder='../../templates/public'
                      )

from.import routes


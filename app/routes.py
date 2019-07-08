from flask import Blueprint, request, abort
import config

if config.prod:
    import relay
else:
    import relay_faker as relay

routes = Blueprint('routes', __name__)

list = config.creds

# A flask endpoint to hit on the network with a given passcode
@routes.route("/")
def index():
    return "index"

@routes.route("/garage")
def garage():
    name = request.args.get('name')
    if name is None:
        return abort(404)
    else:
        for each in list:
            if each == name:
                relay.initialize()
                relay.trigger()
                return each + ", you are authorized, garage interacting..."
        return abort(404)


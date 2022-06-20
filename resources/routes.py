from .images import getServicios, getHolaEye, getJob, getLog

def initialize_routes(api):

    api.add_resource(getServicios, '/servicios')
    api.add_resource(getHolaEye, '/hola')
    # api.add_resource(getJob, '/get-job')
    # api.add_resource(getLog, '/get-log')

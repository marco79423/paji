import fastapi


def get_config(request: fastapi.Request):
    return request.app.state.config


def get_logger(request: fastapi.Request):
    return request.app.state.logger


def get_scheduler(request: fastapi.Request):
    return request.app.state.scheduler

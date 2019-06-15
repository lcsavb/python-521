import flask
import logging

import functools


logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s [%levelname]s %(name)s' +
        '[%(funcName)s] [%(filename)s], $(lineno)s %(message)s'
    )


logging.debug(flask.session.get('email') or 'Não autorizado')



def log_email(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        message = flask.session.get('email') or 'Não autorizado'
        logging.debug(message)
        return function(*args,**kwargs)
    return wrapper


def login_required(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if 'email' not in flask.session:
            flask.flash('Login necessário', 'danger')
            return flask.redirect('/sign-in')
        return function(*args, **kwargs)
    return wrapper

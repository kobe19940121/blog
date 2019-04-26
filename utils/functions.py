from functools import wraps

from flask import session,redirect,url_for


def is_login(func):#func = index
    @wraps(func)
    def check(*args,**kwargs):
        user_id = session.get('user_id')
        if user_id:
            return func(*args,**kwargs)#func = index
        else:
            return redirect(url_for('back.register'))

    return check
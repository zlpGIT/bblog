from functools import wraps

from flask import session, redirect, url_for

# 判断是否登录
def is_login(func):
    @wraps(func)
    def check():
        user_id = session.get('user_id')
        if user_id:
            return func()
        else:
            return redirect(url_for('back.login'))
    return check



def main():
    pass


if __name__ == '__main__':
    main()  
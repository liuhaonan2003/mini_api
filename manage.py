# coding = utf-8
"""
@author: zhou
@time:2019/1/15 11:31
"""


from app import create_app, db
from flask_script import Manager, Shell, Server
from app.models import User, AdminUser, Picture


app = create_app('testing')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, AdminUser=AdminUser, Picture=Picture)


manager.add_command("runserver", Server(use_debugger=True, host='0.0.0.0', port='9980'))
manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run(default_command='runserver')

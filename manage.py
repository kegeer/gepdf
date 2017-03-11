import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app import models


env = os.environ.get('BLOG_ENV', 'dev')
app = create_app('app.config.%sConfig' % env.capitalize())
manager = Manager(app)

migrate = Migrate(app, models.db)

manager.add_command('server', Server(host='127.0.0.1', port=8090))
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(
        app = app,
        db = models.db,
        Info=models.Info,
        Metabolism=models.Metabolism,
        Species=models.Species,
        Genus=models.Genus,
        Disease=models.Disease,
        Ref=models.Ref
    )

if __name__ == '__main__':
    manager.run()
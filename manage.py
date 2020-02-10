from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from salesapp import create_app, DB, models

app = create_app()

# Initializing the manager
manager = Manager(app)

# Initialize Flask Migrate
migrate = Migrate(app, DB)

# Add the flask migrate
manager.add_command('db', MigrateCommand)

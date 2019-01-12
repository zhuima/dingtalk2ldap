from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate


bootstrap = Bootstrap()


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

mail = Mail()
migrate = Migrate()


@login_manager.user_loader
def load_user(user_id):
    from dingtalk2ldap.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'
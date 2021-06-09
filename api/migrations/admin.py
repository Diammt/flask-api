from ..models import User, Admin
from ..models.database import db

admin_data = {
    "firstname": "Admin0",
    "lastname": "Admin0"
}
user_data = {
        "email": "admin0@gobi.com",
        "password": "gobigobi",
        "telephone": "+22962121212",
        "role_id": 1
    }
class AdminMigration():
    @classmethod
    def migrate(cls):
        user = User(user_data.get("email"), user_data.get("password"), user_data.get("telephone"), user_data.get("role_id"))
        user.hash_password(user.password)
        db.session.add(user)
        db.session.commit()
        admin = Admin(admin_data.get("firstname"), admin_data.get("lastname"), user.id)
        db.session.add(admin)
        db.session.commit()
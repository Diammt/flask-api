from ..models import Role
from ..models.database import db

roles = {
    "admin": "The Administrator",
    "client": "Simple User"
}

class RoleMigration:
    @classmethod
    def migrate(cls): 
        for name, description in roles.items():
            role = Role(name, description)
            db.session.add(role)
        db.session.commit()

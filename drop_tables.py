# drop_table.py
from web import db, create_app
from web.models import User

app = create_app()

with app.app_context():
    User.__table__.drop(db.engine)
    print("Flight table dropped.")

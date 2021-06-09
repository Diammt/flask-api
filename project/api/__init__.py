from . import models
from .api_resource import app, jsonify
from .start import db, API_URL, swagger 
from .migrations import *
import logging as lg
import json

@app.cli.command()
def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    lg.warning('Database initialized!')

@app.cli.command()
def dev_migration():
    lg.warning("Data initialize for developpement")

@app.cli.command()
def prod_migration():
    lg.warning("Data initialize for production")

@app.cli.command()
def api_generate():
    """
        Generate swagger.json file for documentation
    """
    with open("gobi"+API_URL, "w") as f:
        json.dump(swagger(app), f, indent=4)
    lg.warning("API generate successfuly at {}".format(API_URL))


if __name__ == '__main__':
    app.run(debug=True)
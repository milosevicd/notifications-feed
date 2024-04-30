from app.utils.db import db
from app.utils.app_factory import create_app
from app.utils.config import DevelopmentConfig, ProductionConfig, TestingConfig
from app.utils.load_db import process_json_to_db
import os


if __name__ == '__main__':

    if os.environ.get('WORK_ENV') == 'PROD':        
        app = create_app(ProductionConfig)
    elif os.environ.get('WORK_ENV') == 'TEST':
        app = create_app(TestingConfig)
    else:
        app = create_app(DevelopmentConfig)

        with app.app_context():
            # clear all data from the database and re-create it from the JSON file
            db.drop_all()
            db.create_all()
            process_json_to_db()

    app.run()
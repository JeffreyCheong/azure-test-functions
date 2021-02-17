import os
import logging


class Database(object):
    
    def __init__(self) -> None:

        if os.environ['ENV'] == 'local':
            self.db_conn = {
                "host": os.environ["DbHost"],
                "username": os.environ["DbUser"],
                "password": os.environ["DbPass"],
                "database_name": os.environ["DbName"],
                "port": os.environ["DbPort"]
            }
        else:
            self.db_conn = {
                "host": os.environ["ProdDbHost"],
                "username": os.environ["ProdDbUser"],
                "password": os.environ["ProdDbPass"],
                "database_name": os.environ["ProdDbName"],
                "port": os.environ["ProdDbPort"]
            }

    def connect(self, app):
        try:
            app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{self.db_conn['username']}:{self.db_conn['password']}@{self.db_conn['host']}/{self.db_conn['database_name']}"
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        except Exception as identifier:
            return {
                "status": 400,
                "message": identifier.args
            } 

import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_STRING']


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def load_raquets_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from raquets"))
    raquets = []
    for row in result.all():
      raquets.append(row._asdict())
    return raquets
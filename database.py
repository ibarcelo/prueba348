import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://admin:Ii27012003@database-1.cf6kyc60gpxb.us-east-2.rds.amazonaws.com/prueba348?charset=utf8mb4"

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
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

def load_raquets_from_db_by_brand(brand):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from raquets where brand = :brand")
      , {"brand": brand}
    )

def uploadRaquet(brand, model, weight, price, head_size):
  with engine.connect() as conn:
    result = conn.execute(
      text("insert into raquets (brand, model, weight, price, head_size) values (:brand, :model, :weight, :price, :head_size)"),
    {
      "brand": brand,
      "model": model,
      "weight": weight,
      "price": price,
      "head_size": head_size
    }  
    )
    conn.commit()

def elimRaquet(id):
  with engine.connect() as conn:
    result = conn.execute(
        text("DELETE FROM raquets WHERE id = :id"),
        {"id": id}
    )
    conn.commit()

def editRaquet(characteristic, newValue, id):
  with engine.connect() as conn:
    
      query = text(f"UPDATE raquets SET {characteristic} = :newValue WHERE id = :id")
      result = conn.execute(query,
         {
             "newValue": newValue,
             "id": id
         })
      conn.commit()


def disp_raquets(characteristic, value, min_price, max_price):
  with engine.connect() as conn:
      if characteristic == 'price':
          query = text(f"SELECT * FROM raquets WHERE price > {min_price} AND price < {max_price}")
          result = conn.execute(query, 
            {"min_price": min_price,
             "max_price": max_price}
            )
          return result
      elif characteristic == 'everything':
          result = conn.execute(text("SELECT * FROM raquets"))
          
      else:
          query = text(f"SELECT * FROM raquets WHERE {characteristic} = :value")
          result = conn.execute(query,
              {
              "characteristic": characteristic,
              "value": value}
              )

  dispraquets = []
  for row in result.all():
    dispraquets.append(row._asdict())
  return dispraquets
    



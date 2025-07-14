import psycopg2
from psycopg2.extras import RealDictCursor
import os

class Database:
  def __init__ (self):
    self.DB_USER = os.environ['POSTGRES_USER']
    self.DB_HOST = os.environ['POSTGRES_HOST']
    self.DB_NAME = os.environ['POSTGRES_DB']
    self.DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
    self.DB_PORT = os.environ['POSTGRES_PORT']

    self.pgsqlcon = self.connect_pgsql()
    self.pgsql = self.pgsqlcon.cursor(cursor_factory=RealDictCursor)
    self.pgurl = self.construct_pg_url(user=self.DB_USER,password=self.DB_PASSWORD,host=self.DB_HOST,port=self.DB_PORT,database=self.DB_NAME)
    #self.pgdataset = dataset.Database(url=self.pgurl, schema="public")
 
  def __del__(self):
    self.pgsql.close()
    self.pgsqlcon.close()  

  def connect_pgsql(self):
    try:
      #print(self.config)
      with psycopg2.connect(dbname=self.config['DB_NAME'],user=self.config['DB_USER'],password=self.config['DB_PASSWORD'],host=self.config['DB_HOST'],port=self.config['DB_PORT']) as conn:
        #print('Connected to the PostgreSQL server.')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
      print(error)

  def _pg_exec(self, sql, values):
    try:
      self.pgsql.execute(sql, values)
    except (psycopg2.DatabaseError, Exception) as error: 
      print(error)

  
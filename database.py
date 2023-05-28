from sqlalchemy import create_engine,text
import OS
my_secret=os.environ['DB_STRING']
engine = create_engine(my_secret,connect_args={
  "ssl":{
    "ssl_ca":"/etc/ssl/cert.pem"
  }
})
with engine.connect() as conn:
  result=conn.execute(text("select * from students"))
  print(result.all())


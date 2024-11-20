from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Databale_url = "localhost"

#se crea el motoro 
engine = create_engine(Databale_url, connect_args={"check_same_thread": False})

#parametro para el motor
sessionlocalhost = sessionmaker(commit=False,
                                autoflush=False,
                                bind=engine)
#se crea el mapeador
Base = declarative_base()

#sea crea una funcion para 
async def get_db():
    db = sessionlocalhost()
    try:
        #producir
        yield db
    finally:
        db.close()


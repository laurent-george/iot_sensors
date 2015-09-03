import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'Sensor_temp2'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    sensor_name = Column(String(250), nullable=False)
    value = Column(Integer)
    trallala = Column(Integer)


database_name = "test"
# creation of database if neccessary
engine = create_engine("mysql://root:root@127.0.0.1/%s" % database_name)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)


Base.metadata.bind = engine

#import time
#time.time()

DBSession = sessionmaker(bind=engine)
session = DBSession()

new_sensor = Sensor(id=55, sensor_name='test temp', value=88, trallala=12)
session.add(new_sensor)


session.commit()


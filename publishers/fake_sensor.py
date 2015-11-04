import os

from sqlalchemy import Column, Integer,TIMESTAMP, Float, VARCHAR
from sqlalchemy.sql import func
import sqlalchemy
import sqlalchemy.ext
import sqlalchemy.ext.declarative
import sys


import time
import datetime

Base = sqlalchemy.ext.declarative.declarative_base()

engine = sqlalchemy.create_engine("mysql://%s/%s" % (server_ip, server_db))
metadata = sqlalchemy.MetaData(bind=engine)

class Tests(Base):
    __table__ = sqlalchemy.Table('fake_sensor', metadata, autoload=True)

dbsession = sqlalchemy.orm.sessionmaker(bind=engine)
session = dbsession()
 session.query(Tests)[0].value  # to be continued.
session.query(Tests)[-1].value  # to be continued.


class SensorDatabaseModel(Base):
    name = os.path.basename(sys.modules[__name__].__file__)
    name = os.path.splitext(name)[0]
    __tablename__ = name
    id = Column(Integer, primary_key=True,autoincrement=True)
    timestamp = Column( TIMESTAMP,server_default=func.now()) # default='CURRENT_TIMESTAMP',u'timestamp', nullable=False,
    name_sensor = Column(VARCHAR(length=50))
    value = Column(Float)
    seq_number = Column(Integer, primary_key=False)

    # TODO: add a timestamp here
    # TODO: add also an automatic timestamp from mysql db

class DummySensor(object):
    def __init__(self, server_ip):
        self.database_name = "HOME_SENSORS"
        self.name_sensor = "TEMPERATURE"
        self.seq_number = 0
        self.value = 0
        self.server_ip = server_ip

        # creation of database if neccessary
        self.engine = sqlalchemy.create_engine("mysql://%s/%s" % (self.server_ip ,self.database_name)) #("mysql://root:root@127.0.0.1/%s" % self.database_name)
        self.model_db = SensorDatabaseModel
        Base.metadata.create_all(self.engine) # tODO: peut etre a mettre dans le main
        Base.metadata.bind = self.engine
        self.dbsession = sqlalchemy.orm.sessionmaker(bind=self.engine)
        self.session = self.dbsession()

    def update(self):
        self.seq_number += 1
        self.value += 2

    def publish_data(self):
        self.update()  # we update after each get for the dummy
        data = {}
        data['value'] = self.value
        data['timestamp'] = time.time()

        # do sql publish
        print(data)
        new_sensor_val = SensorDatabaseModel(value=self.value, seq_number = self.seq_number, name_sensor=self.name_sensor)
        self.session.add(new_sensor_val)
        self.session.commit()



def main():
    try:
        sensor = DummySensor('10.0.160.255')
        wait_time = 2.0  # 2 seconds
        while True:
            sensor.publish_data()
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print("User pressed ctrl-c, quitting.")

if __name__ == "__main__":
    main()

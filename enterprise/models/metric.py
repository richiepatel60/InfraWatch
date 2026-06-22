# enterprise/models/metric.py

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from enterprise.db.database import Base


class Metric(Base):

    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True)

    timestamp = Column(String)

    cpu_percent = Column(Float)

    memory_percent = Column(Float)

    disk_percent = Column(Float)

    process_count = Column(Integer)
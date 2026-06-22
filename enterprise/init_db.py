from enterprise.db.database import Base
from enterprise.db.database import engine

from enterprise.models.metric import Metric

Base.metadata.create_all(bind=engine)

print("Database tables created.")
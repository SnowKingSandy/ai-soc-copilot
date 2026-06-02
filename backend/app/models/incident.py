from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.database import Base


class Incident(Base):

    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    severity = Column(String)

    attack_type = Column(String)

    detected_threat = Column(String)

    mitre_id = Column(String)

    confidence = Column(Float)

    risk_score = Column(Integer)

    source_ip = Column(String)

    failed_attempts = Column(Integer)

    summary = Column(String)
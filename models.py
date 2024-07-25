from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from database import Base

class Pdf(Base):
    __tablename__ = "pdfs"

    id = Column(Integer, primary_key=True)
    file_name = Column(String, index=True)
    upload_date = Column(DateTime, default=datetime.datetime.utcnow)

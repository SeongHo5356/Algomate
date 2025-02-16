import os
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://algomate:algomate7897@localhost:5432/algomate_db"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Solution(Base):
    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True, index = True)
    problem_id = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    language = Column(String, nullable=False)
    user_id = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)
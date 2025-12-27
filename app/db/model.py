from .database import Base
from sqlalchemy import Integer, String, Column

class PrMetadata(Base):
    __tablename__ = "pr_metadata"
    id = Column(Integer, primary_key=True, index=True)
    pr_number = Column(Integer, index=True)
    repo_name = Column(String, index=True)
    sha = Column(String, index=True)
    action = Column(String, index=True)

    

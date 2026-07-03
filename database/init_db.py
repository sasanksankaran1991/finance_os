from database.database import engine
from database.models import Base

from utils.logger import logger


def initialize_database():

    Base.metadata.create_all(bind=engine)

    logger.info("Database Initialized")
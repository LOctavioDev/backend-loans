"""
This is a configuration module for the database connection
"""

import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    logger.error("\033[91mDATABASE_URL environment variable not set\033[0m")
    raise ValueError("DATABASE_URL environment variable not set")

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    logger.info("\033[92m\n\n=== Database connection successful ===\n\033[0m")

except Exception as e:
    logger.error("\033[91mServer error: %s\033[0m", str(e))
    raise

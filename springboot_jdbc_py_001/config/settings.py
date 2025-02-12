import os
import logging

# Database Configuration
DATABASE_NAME = 'student_database.db'
DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), DATABASE_NAME)

# Logging Configuration
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.INFO

# Application Constants
APP_NAME = 'Student Management System'
VERSION = '1.0.0'

# Environment-specific Settings
DEBUG = True  # Set to False in production

# Secret Key (in a real-world scenario, this would be an environment variable)
SECRET_KEY = 'your-secret-key-here'

# Other settings
MAX_STUDENTS = 1000
PAGINATION_LIMIT = 50

# Resource file paths
SCHEMA_SQL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'schema.sql')
DATA_SQL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'data.sql')

# Test settings
TEST_DATABASE_NAME = 'test_student_database.db'
TEST_DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), TEST_DATABASE_NAME)
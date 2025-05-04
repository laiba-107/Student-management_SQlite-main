import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
    DATABASE_URI = os.path.join(os.path.expanduser('~'), 'Documents', 'student_management.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_URI}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Add this to debug the path
print(f"Database will be created at: {Config.DATABASE_URI}")
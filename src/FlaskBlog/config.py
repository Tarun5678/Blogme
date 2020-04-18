import os

class Config:
  SECRET_KEY = '45c53114509e1a5a4e3cc8ffb936d327'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
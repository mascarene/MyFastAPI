from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
import psycopg2
import time
from psycopg2.extras import RealDictCursor


# Se connecter à la base de données
# structure de l'URL pour Postgres : postgresql://<username>:<password>@<ip-address/hostname>/<database_name>
# To-Do: Secrets !
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:2YuHHakD7fy6tK88aHm2jd7cuKZMFbjsEBYoYGZtMHtX8BPBsLedxEx3mxvANaNWM8zQdqvPjE7oXZzp37KwhRv7iAd3LNwEVjJj58A27GPHeBPvwyBjWfNQwNvygg79@localhost/fastapi'

# Création du moteur (qui va connecter SQLAlchemy a la base Postgres)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative Mapping: Définie la classe 'Base', tous les modèles que nous définirons pour creer nos tables dans Postgress utiliseront cette classe.
Base = declarative_base()

# Dépendance :
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
        password='2YuHHakD7fy6tK88aHm2jd7cuKZMFbjsEBYoYGZtMHtX8BPBsLedxEx3mxvANaNWM8zQdqvPjE7oXZzp37KwhRv7iAd3LNwEVjJj58A27GPHeBPvwyBjWfNQwNvygg79',
        cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was sucessful!")
        break
    except Exception as error:
        print("Connecting to the database failed")
        print("Error: ", error)
        time.sleep(2)

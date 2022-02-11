from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from app import create_app

db = SQLAlchemy(create_app())

db.engine.execute(
    """
    DROP TABLE IF EXISTS game;
    """
)

db.engine.execute(
    """
    CREATE TABLE game (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL UNIQUE,
        price DECIMAL(65 , 5) NOT NULL,   
        space BIGINT NOT NULL
    );
    """
)  # AUTOINCREMENT for id for other databases

print("game table created successfully")

try:
    db.session.execute(text("SELECT 1"))
    print("<h1>It works.</h1>")
except:
    print("<h1>Something is broken.</h1>")

db.engine.execute(
    """
    INSERT INTO game(name, price, space) VALUES 
    ('john.do,e@zmail.,com', 772.1223, 1073741824);
    """
)


for record in db.engine.execute("SELECT * FROM game;"):
    print(record)

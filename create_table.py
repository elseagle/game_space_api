import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from app import create_app
from utils.generate_games import generate

db = SQLAlchemy(create_app())


"""
Check database connection
"""

try:
    db.session.execute(text("SELECT 1"))
    print("<h1>It works.</h1>")
except:
    print("<h1>Something is broken.</h1>")
    sys.exit()

"""
Delete table if it already exists
"""

db.engine.execute(
    """
    DROP TABLE IF EXISTS game;
    """
)


"""
Create game table with name, price and space
"""

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

"""
Insert randomly generated games into the database
"""

for game in generate(1000):
    try:
        db.engine.execute(
            f"""
            INSERT INTO game(name, price, space) VALUES 
            ('{game["name"]}', {game["price"]}, {game["space"]});
            """
        )
        print(f"{game} inserted successfully")
    except:
        print('\n')
        print(f">>>>>>>>>>>>>>>>>>>>>>>DB insert failed for {game}")
        print('\n')

for record in db.engine.execute("SELECT * FROM game;"):
    print(record)

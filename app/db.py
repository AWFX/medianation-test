import os
import psycopg2

class Data:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=int(os.getenv("POSTGRES_PORT", 5432))
        )
        self.ensure_table()

    # Ensure the posts table exists
    def ensure_table(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                );
            """)
            self.conn.commit()

    # Methods to interact with the posts table
    def get_posts(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, title, content FROM posts;")
            rows = cur.fetchall()
            if not rows:
                return {"message": "No posts found"}
            return [{"id": x[0], "title": x[1], "content": x[2]} for x in rows]
    
    # Create a new post
    def create_post(self, title, content):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING id, title, content;",
                (title, content)
            )
            row = cur.fetchone()
            self.conn.commit()
            return {"id": row[0], "title": row[1], "content": row[2]}

    # Close the database connection
    def close(self):
        self.conn.close()


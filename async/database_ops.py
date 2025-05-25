import asyncio
import asyncpg
from datetime import datetime
import random

async def create_pool():
    """Create a connection pool"""
    return await asyncpg.create_pool(
        user='postgres',
        password='your_password',
        database='your_database',
        host='localhost'
    )

async def create_tables(pool):
    """Create necessary tables"""
    async with pool.acquire() as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

async def insert_user(pool, username, email):
    """Insert a new user"""
    async with pool.acquire() as conn:
        try:
            await conn.execute(
                'INSERT INTO users(username, email) VALUES($1, $2)',
                username, email
            )
            return True
        except asyncpg.UniqueViolationError:
            print(f"User {username} or email {email} already exists")
            return False

async def get_user(pool, username):
    """Get user by username"""
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            'SELECT * FROM users WHERE username = $1',
            username
        )

async def main():
    # Create connection pool
    pool = await create_pool()
    
    # Create tables
    await create_tables(pool)
    
    # Example operations
    users = [
        ('john_doe', 'john@example.com'),
        ('jane_smith', 'jane@example.com'),
        ('bob_johnson', 'bob@example.com')
    ]
    
    # Insert users concurrently
    tasks = [insert_user(pool, username, email) for username, email in users]
    results = await asyncio.gather(*tasks)
    
    print(f"Successfully inserted {sum(results)} users")
    
    # Fetch users concurrently
    fetch_tasks = [get_user(pool, username) for username, _ in users]
    fetched_users = await asyncio.gather(*fetch_tasks)
    
    for user in fetched_users:
        if user:
            print(f"Found user: {user['username']} ({user['email']})")
    
    # Close the pool
    await pool.close()

if __name__ == "__main__":
    asyncio.run(main()) 
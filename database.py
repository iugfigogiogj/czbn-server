import sqlite3
import json
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.db_path = 'data/database.db'
        os.makedirs('data', exist_ok=True)
        self.init_db()
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        with self.get_connection() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                image TEXT,
                preview TEXT NOT NULL,
                details TEXT,
                content TEXT,
                tags TEXT
            )''')
            
            conn.execute('''CREATE TABLE IF NOT EXISTS vacancies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                salary TEXT NOT NULL,
                badge TEXT,
                details TEXT,
                apply_link TEXT
            )''')
            
            conn.execute('''CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                rating INTEGER NOT NULL,
                text TEXT NOT NULL,
                date TEXT NOT NULL,
                status TEXT DEFAULT 'pending'
            )''')
    
    # Новости
    def get_all_news(self):
        with self.get_connection() as conn:
            rows = conn.execute('SELECT * FROM news ORDER BY id DESC').fetchall()
            return [dict(row) for row in rows]
    
    def create_news(self, data):
        with self.get_connection() as conn:
            cur = conn.execute('''
                INSERT INTO news (title, date, image, preview, details, content, tags)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['title'], data['date'], data.get('image', ''),
                data['preview'], data.get('details', ''), data.get('content', ''),
                json.dumps(data.get('tags', []))
            ))
            return cur.lastrowid
    
    def update_news(self, news_id, data):
        with self.get_connection() as conn:
            conn.execute('''
                UPDATE news SET title=?, date=?, image=?, preview=?, details=?, content=?, tags=?
                WHERE id=?
            ''', (
                data['title'], data['date'], data.get('image', ''),
                data['preview'], data.get('details', ''), data.get('content', ''),
                json.dumps(data.get('tags', [])), news_id
            ))
    
    def delete_news(self, news_id):
        with self.get_connection() as conn:
            conn.execute('DELETE FROM news WHERE id = ?', (news_id,))
    
    # Вакансии
    def get_all_vacancies(self):
        with self.get_connection() as conn:
            rows = conn.execute('SELECT * FROM vacancies ORDER BY id DESC').fetchall()
            return [dict(row) for row in rows]
    
    def create_vacancy(self, data):
        with self.get_connection() as conn:
            cur = conn.execute('''
                INSERT INTO vacancies (title, company, salary, badge, details, apply_link)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                data['title'], data['company'], data['salary'], data.get('badge', ''),
                json.dumps(data.get('details', [])), data.get('apply_link', '')
            ))
            return cur.lastrowid
    
    def update_vacancy(self, vacancy_id, data):
        with self.get_connection() as conn:
            conn.execute('''
                UPDATE vacancies SET title=?, company=?, salary=?, badge=?, details=?, apply_link=?
                WHERE id=?
            ''', (
                data['title'], data['company'], data['salary'], data.get('badge', ''),
                json.dumps(data.get('details', [])), data.get('apply_link', ''), vacancy_id
            ))
    
    def delete_vacancy(self, vacancy_id):
        with self.get_connection() as conn:
            conn.execute('DELETE FROM vacancies WHERE id = ?', (vacancy_id,))
    
    # Отзывы
    def get_published_reviews(self):
        with self.get_connection() as conn:
            rows = conn.execute('SELECT * FROM reviews WHERE status = "approved" ORDER BY id DESC').fetchall()
            return [dict(row) for row in rows]
    
    def get_pending_reviews(self):
        with self.get_connection() as conn:
            rows = conn.execute('SELECT * FROM reviews WHERE status = "pending" ORDER BY id DESC').fetchall()
            return [dict(row) for row in rows]
    
    def create_review(self, data):
        with self.get_connection() as conn:
            cur = conn.execute('''
                INSERT INTO reviews (name, category, rating, text, date, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                data['name'], data['category'], data['rating'],
                data['text'], data['date'], 'pending'
            ))
            return cur.lastrowid
    
    def approve_review(self, review_id):
        with self.get_connection() as conn:
            conn.execute('UPDATE reviews SET status = "approved" WHERE id = ?', (review_id,))
    
    def reject_review(self, review_id):
        with self.get_connection() as conn:

            conn.execute('DELETE FROM reviews WHERE id = ?', (review_id,))
            
            def delete_review(self, review_id):
    with self.get_connection() as conn:
        conn.execute('DELETE FROM reviews WHERE id = ?', (review_id,))

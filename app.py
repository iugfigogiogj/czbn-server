from flask import Flask, request, jsonify
from flask_cors import CORS
from database import Database

app = Flask(__name__)
# РАЗРЕШАЕМ ВСЁ!
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

db = Database()

# Добавляем обработку OPTIONS запросов (важно для DELETE)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# ========== НОВОСТИ ==========
@app.route('/api/news', methods=['GET', 'OPTIONS'])
def get_news():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify(db.get_all_news())

@app.route('/api/news/<int:news_id>', methods=['GET', 'OPTIONS'])
def get_one_news(news_id):
    if request.method == 'OPTIONS':
        return '', 200
    news = db.get_news(news_id)
    if news:
        return jsonify(news)
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/news', methods=['POST', 'OPTIONS'])
def create_news():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    news_id = db.create_news(data)
    return jsonify({'id': news_id, 'success': True})

@app.route('/api/news/<int:news_id>', methods=['PUT', 'OPTIONS'])
def update_news(news_id):
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    db.update_news(news_id, data)
    return jsonify({'success': True})

@app.route('/api/news/<int:news_id>', methods=['DELETE', 'OPTIONS'])
def delete_news(news_id):
    if request.method == 'OPTIONS':
        return '', 200
    db.delete_news(news_id)
    return jsonify({'success': True})

# ========== ВАКАНСИИ ==========
@app.route('/api/vacancies', methods=['GET', 'OPTIONS'])
def get_vacancies():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify(db.get_all_vacancies())

@app.route('/api/vacancies/<int:vacancy_id>', methods=['GET', 'OPTIONS'])
def get_one_vacancy(vacancy_id):
    if request.method == 'OPTIONS':
        return '', 200
    vacancy = db.get_vacancy(vacancy_id)
    if vacancy:
        return jsonify(vacancy)
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/vacancies', methods=['POST', 'OPTIONS'])
def create_vacancy():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    vacancy_id = db.create_vacancy(data)
    return jsonify({'id': vacancy_id, 'success': True})

@app.route('/api/vacancies/<int:vacancy_id>', methods=['PUT', 'OPTIONS'])
def update_vacancy(vacancy_id):
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    db.update_vacancy(vacancy_id, data)
    return jsonify({'success': True})

@app.route('/api/vacancies/<int:vacancy_id>', methods=['DELETE', 'OPTIONS'])
def delete_vacancy(vacancy_id):
    if request.method == 'OPTIONS':
        return '', 200
    db.delete_vacancy(vacancy_id)
    return jsonify({'success': True})

# ========== ОТЗЫВЫ ==========
@app.route('/api/reviews/published', methods=['GET', 'OPTIONS'])
def get_published_reviews():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify(db.get_published_reviews())

@app.route('/api/reviews/pending', methods=['GET', 'OPTIONS'])
def get_pending_reviews():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify(db.get_pending_reviews())

@app.route('/api/reviews', methods=['POST', 'OPTIONS'])
def create_review():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    review_id = db.create_review(data)
    return jsonify({'id': review_id, 'success': True})

@app.route('/api/reviews/<int:review_id>/approve', methods=['POST', 'OPTIONS'])
def approve_review(review_id):
    if request.method == 'OPTIONS':
        return '', 200
    db.approve_review(review_id)
    return jsonify({'success': True})

@app.route('/api/reviews/<int:review_id>/reject', methods=['POST', 'OPTIONS'])
def reject_review(review_id):
    if request.method == 'OPTIONS':
        return '', 200
    db.reject_review(review_id)
    return jsonify({'success': True})

@app.route('/api/reviews/<int:review_id>', methods=['DELETE', 'OPTIONS'])
def delete_review(review_id):
    if request.method == 'OPTIONS':
        return '', 200
    db.delete_review(review_id)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

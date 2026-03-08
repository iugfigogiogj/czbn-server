from flask import Flask, request, jsonify
from flask_cors import CORS
from database import Database

app = Flask(__name__)
CORS(app)
db = Database()

# ========== НОВОСТИ ==========
@app.route('/api/news', methods=['GET'])
def get_news():
    return jsonify(db.get_all_news())

@app.route('/api/news', methods=['POST'])
def create_news():
    data = request.json
    news_id = db.create_news(data)
    return jsonify({'id': news_id, 'success': True})

@app.route('/api/news/<int:news_id>', methods=['PUT'])
def update_news(news_id):
    data = request.json
    db.update_news(news_id, data)
    return jsonify({'success': True})

@app.route('/api/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    db.delete_news(news_id)
    return jsonify({'success': True})

# ========== ВАКАНСИИ ==========
@app.route('/api/vacancies', methods=['GET'])
def get_vacancies():
    return jsonify(db.get_all_vacancies())

@app.route('/api/vacancies', methods=['POST'])
def create_vacancy():
    data = request.json
    vacancy_id = db.create_vacancy(data)
    return jsonify({'id': vacancy_id, 'success': True})

@app.route('/api/vacancies/<int:vacancy_id>', methods=['PUT'])
def update_vacancy(vacancy_id):
    data = request.json
    db.update_vacancy(vacancy_id, data)
    return jsonify({'success': True})

@app.route('/api/vacancies/<int:vacancy_id>', methods=['DELETE'])
def delete_vacancy(vacancy_id):
    db.delete_vacancy(vacancy_id)
    return jsonify({'success': True})

# ========== ОТЗЫВЫ ==========
@app.route('/api/reviews/published', methods=['GET'])
def get_published_reviews():
    return jsonify(db.get_published_reviews())

@app.route('/api/reviews/pending', methods=['GET'])
def get_pending_reviews():
    return jsonify(db.get_pending_reviews())

@app.route('/api/reviews', methods=['POST'])
def create_review():
    data = request.json
    review_id = db.create_review(data)
    return jsonify({'id': review_id, 'success': True})

@app.route('/api/reviews/<int:review_id>/approve', methods=['POST'])
def approve_review(review_id):
    db.approve_review(review_id)
    return jsonify({'success': True})

@app.route('/api/reviews/<int:review_id>/reject', methods=['POST'])
def reject_review(review_id):
    db.reject_review(review_id)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
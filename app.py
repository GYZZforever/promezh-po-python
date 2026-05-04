from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Функция для создания подключения к базе данных SQLite
def get_db_connection():
    conn = sqlite3.connect('database/database.db')
    conn.row_factory = sqlite3.Row # Позволяет обращаться к колонкам по именам
    return conn

# Главная страница со списком партнеров и пагинацией
@app.route('/')
def index():
    # Получаем текущую страницу из параметров запроса, по умолчанию 1
    page = request.args.get('page', 1, type=int)
    per_page = 2 # Количество записей на одной странице
    offset = (page - 1) * per_page

    conn = get_db_connection()
    
    # Получаем общее количество записей для расчета количества страниц
    total_count = conn.execute('SELECT COUNT(*) FROM partners').fetchone()[0]
    total_pages = (total_count + per_page - 1) // per_page

    # Запрос на получение партнеров с учетом лимита для текущей страницы
    partners = conn.execute('''
        SELECT p.*, t.type_name 
        FROM partners p 
        JOIN partner_types t ON p.type_id = t.id
        LIMIT ? OFFSET ?
    ''', (per_page, offset)).fetchall()
    
    conn.close()
    return render_template('index.html', partners=partners, page=page, total_pages=total_pages)

# Страница добавления нового партнера (Обработка GET и POST запросов)
@app.route('/add', methods=('GET', 'POST'))
def add_partner():
    if request.method == 'POST':
        # Получаем данные из полей формы
        name = request.form['name']
        type_id = request.form['type_id']
        director = request.form['director']
        phone = request.form['phone']
        rating = request.form['rating']

        # Сохраняем нового партнера в базу данных
        conn = get_db_connection()
        conn.execute('INSERT INTO partners (name, type_id, director_fio, phone, rating) VALUES (?, ?, ?, ?, ?)',
                     (name, type_id, director, phone, rating))
        conn.commit()
        conn.close()
        # После сохранения возвращаемся на главную
        return redirect(url_for('index'))

    return render_template('add_partner.html')

if __name__ == '__main__':
    # Запуск сервера в режиме отладки
    app.run(debug=True, port=5000)

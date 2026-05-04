import sqlite3

def seed():
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM partners')

    test_partners = [
        (1, 'ТехноМир', 'Иванов Иван Иванович', 'ivanov@tech.ru', '+7 495 123 45 67', 'г. Москва, ул. Ленина, 1', '1234567890', 10),
        (2, 'Пол И К', 'Петров Петр Петрович', 'petrov@pol.ru', '+7 812 987 65 43', 'г. Санкт-Петербург, пр. Мира, 10', '0987654321', 8),
        (4, 'ИП Сидоров', 'Сидоров Алексей', 'sidorov@mail.ru', '+7 900 111 22 33', 'г. Казань, ул. Центральная, 5', '1112223334', 5)
    ]

    cursor.executemany('''
        INSERT INTO partners (type_id, name, director_fio, email, phone, legal_address, inn, rating) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', test_partners)

    conn.commit()
    conn.close()
    print("Тестовые данные успешно добавлены!")

if __name__ == '__main__':
    seed()

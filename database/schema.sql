CREATE TABLE IF NOT EXISTS partner_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS partners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    name TEXT NOT NULL,
    director_fio TEXT,
    email TEXT,
    phone TEXT,
    legal_address TEXT,
    inn TEXT,
    rating INTEGER DEFAULT 0,
    FOREIGN KEY (type_id) REFERENCES partner_types(id)
);

INSERT INTO partner_types (type_name) VALUES ('ООО'), ('ЗАО'), ('ПАО'), ('ИП');

-- Создание таблицы для статистики посещений
CREATE TABLE IF NOT EXISTS page_visits (
    id SERIAL PRIMARY KEY,
    page_url VARCHAR(255) NOT NULL,
    ip_address INET,
    visit_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_agent TEXT,
    referrer VARCHAR(512)
);

-- Таблица для контактов (если добавим форму)
CREATE TABLE IF NOT EXISTS contact_messages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN DEFAULT FALSE
);

-- Пример данных
INSERT INTO page_visits (page_url, ip_address, user_agent) 
VALUES 
    ('/index.html', '127.0.0.1', 'Initial Docker Setup'),
    ('/about.html', '127.0.0.1', 'Initial Docker Setup');

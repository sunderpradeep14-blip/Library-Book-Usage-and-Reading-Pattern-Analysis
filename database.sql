-- ============================================
-- Library Book Usage & Reading Pattern Analysis
-- Database Setup Script
-- Run this in MySQL Workbench or Command Line
-- ============================================

CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- ── Table 1: ADMIN ──────────────────────────
CREATE TABLE IF NOT EXISTS admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    role VARCHAR(20) DEFAULT 'admin'
);

-- ── Table 2: BOOKS ──────────────────────────
CREATE TABLE IF NOT EXISTS books (
    book_id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    genre VARCHAR(50),
    total_copies INT DEFAULT 1,
    available_copies INT DEFAULT 1
);

-- ── Table 3: STUDENTS ───────────────────────
CREATE TABLE IF NOT EXISTS students (
    student_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(20),
    year INT,
    email VARCHAR(100),
    roll_number VARCHAR(20)
);

-- ── Table 4: BORROW_RECORDS ─────────────────
CREATE TABLE IF NOT EXISTS borrow_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(10),
    book_id VARCHAR(10),
    borrow_date DATE,
    return_date DATE,
    due_date DATE,
    status VARCHAR(20) DEFAULT 'Borrowed',
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- ── Table 5: REPORTS ────────────────────────
CREATE TABLE IF NOT EXISTS reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    generated_by INT,
    report_type VARCHAR(50),
    generated_date DATE DEFAULT (CURDATE()),
    description TEXT,
    FOREIGN KEY (generated_by) REFERENCES admin(admin_id)
);

-- ── Insert default admin ─────────────────────
INSERT IGNORE INTO admin (username, password, email, role)
VALUES ('admin', 'admin123', 'admin@library.com', 'admin');

-- ── Insert sample books ──────────────────────
INSERT IGNORE INTO books VALUES
('B001','Data Structures','Narasimha Karumanchi','Technical',5,3),
('B002','Python Programming','Mark Lutz','Technical',4,2),
('B003','Machine Learning','Tom Mitchell','Technical',3,1),
('B004','Engineering Maths','B.S. Grewal','Science',4,3),
('B005','DBMS Concepts','Ramez Elmasri','Technical',3,2),
('B006','Computer Networks','Forouzan','Technical',3,2),
('B007','Operating Systems','Silberschatz','Technical',2,1),
('B008','Discrete Maths','Kenneth Rosen','Science',3,2),
('B009','Atomic Habits','James Clear','Self Help',2,1),
('B010','Wings of Fire','A.P.J Abdul Kalam','Self Help',3,2),
('B011','Rich Dad Poor Dad','Robert Kiyosaki','Self Help',2,1),
('B012','History of India','Romila Thapar','History',2,2),
('B013','The Alchemist','Paulo Coelho','Fiction',3,2),
('B014','Ikigai','Hector Garcia','Self Help',2,1),
('B015','Deep Learning','Ian Goodfellow','Technical',2,1);

SELECT 'Database setup complete!' AS Message;

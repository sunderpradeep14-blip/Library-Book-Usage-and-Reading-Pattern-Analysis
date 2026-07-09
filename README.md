# 📚 Library Book Usage & Reading Pattern Analysis

A data analysis and visualization mini-project that studies how students borrow and use library books — identifying the most popular books, busiest departments, seasonal borrowing trends, and average reading duration. Built with **Python, Flask, MySQL, and HTML/CSS**.

---

## Project Purpose

College libraries generate borrowing data every day, but rarely analyze it. This project turns that raw data into actionable insight:

-  Which books are borrowed the most (and which are dead stock)
- Which departments read the most
- When library usage peaks (e.g., exam season)
- How long students typically keep a book

This helps a librarian decide what to restock, what to remove, and when to extend library hours.

---

##  System Architecture

```
Raw Library Data (CSV / Manual Entry)
        │
        ▼
Data Cleaning Module (Python + Pandas)
        │
        ▼
   MySQL Database
        │
        ▼
Analysis Module (Pandas + SQL Queries)
        │
        ▼
Visualization Module (Matplotlib / Seaborn)
        │
        ▼
     Flask Web App
        │
        ▼
HTML/CSS Dashboard (Charts + Insights)
```

---

##  Module Breakdown

| Module | Responsibility | Tech Used |
|---|---|---|
| **Data Collection** | Gather/generate borrowing records (book, student, dates) | CSV / MySQL |
| **Data Cleaning** | Handle missing values, duplicates, date formatting | Python, Pandas |
| **Database Layer** | Store cleaned data in structured tables | MySQL |
| **Analysis Engine** | Compute top books, department trends, monthly patterns, avg holding time | Pandas, SQL |
| **Visualization** | Generate bar, pie, line, and heatmap charts | Matplotlib, Seaborn |
| **Web Interface** | Display dashboard with results | Flask, HTML/CSS |

---

##  Database Schema

**Table: STUDENTS**
| Column | Type | Notes |
|---|---|---|
| student_id | INT | Primary Key |
| name | VARCHAR | |
| department | VARCHAR | |
| year | INT | |

**Table: BOOKS**
| Column | Type | Notes |
|---|---|---|
| book_id | INT | Primary Key |
| title | VARCHAR | |
| author | VARCHAR | |
| genre | VARCHAR | |

**Table: BORROW_RECORDS**
| Column | Type | Notes |
|---|---|---|
| record_id | INT | Primary Key |
| student_id | INT | Foreign Key → STUDENTS |
| book_id | INT | Foreign Key → BOOKS |
| date_borrowed | DATE | |
| date_returned | DATE | |

Relationship: One student can borrow many books, and one book can be borrowed by many students, connected through `BORROW_RECORDS`.

---

##  Data Pipeline (Step-by-Step)

**Step 1 — Data Collection**
Dataset fields:
- Book: `book_id`, `title`, `author`, `genre`
- Student: `student_id`, `department`, `year`
- Transaction: `date_borrowed`, `date_returned`, `borrow_count`

**Step 2 — Data Cleaning**
- Fill or drop missing values
- Remove duplicate borrow records
- Normalize inconsistent date formats

**Step 3 — Data Analysis**
- Most borrowed books (frequency count)
- Most active department (group by department)
- Peak borrowing months (group by month)
- Average book holding time (`date_returned - date_borrowed`)

**Step 4 — Visualization**
-  Bar chart — Top 10 most borrowed books
-  Pie chart — Genre-wise distribution
-  Line graph — Monthly borrowing trend
-  Heatmap — Department vs. reading frequency

---

##  Sample Expected Results

| Metric | Example Result |
|---|---|
| Most borrowed book | *Data Structures* by Narasimha |
| Most active department | CSE / AIDS |
| Peak reading month | November (exam season) |
| Least read genre | Fiction / Literature |
| Avg. book holding time | 7 days |

---

##  Suggested Project Structure

```
library-analysis/
│
├── data/
│   └── library_data.csv
├── app.py                  # Flask app entry point
├── db_config.py             # MySQL connection setup
├── cleaning.py               # Data cleaning scripts
├── analysis.py               # Analysis functions
├── visualization.py          # Chart generation
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/library-analysis.git
   cd library-analysis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**
   ```sql
   CREATE DATABASE library_db;
   ```
   Update your credentials in `db_config.py`.

5. **Run the Flask app**
   ```bash
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

---

##  Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn

---

##  Why This Project Stands Out

-  Directly relevant to everyday college life
-  Can use real data collected from your own college library
- Simple to explain in project reviews/vivas
-  Clean, modular structure with clear database design

---

##  Future Enhancements

- Add student login for self-service borrowing history
- Predictive model for book demand forecasting
- Real-time dashboard using Chart.js instead of static images
- Overdue book alert/notification system

---



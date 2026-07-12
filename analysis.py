
# ============================================
# Library Book Usage & Reading Pattern Analysis
# analysis.py - Data Analysis & Chart Generator
# ============================================

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os

# ── Setup ────────────────────────────────────
DATA_PATH   = 'data/library_data.csv'
CHARTS_PATH = 'static/charts/'
os.makedirs(CHARTS_PATH, exist_ok=True)

BG_COLOR    = '#0D2137'
CARD_COLOR  = '#1A3F6F'
ACCENT      = '#3B9EE8'
GREEN       = '#22C55E'
AMBER       = '#F59E0B'
PURPLE      = '#A855F7'
TEXT_COLOR  = '#E2E8F0'

plt.rcParams.update({
    'figure.facecolor': BG_COLOR,
    'axes.facecolor':   CARD_COLOR,
    'axes.edgecolor':   '#334155',
    'axes.labelcolor':  TEXT_COLOR,
    'xtick.color':      TEXT_COLOR,
    'ytick.color':      TEXT_COLOR,
    'text.color':       TEXT_COLOR,
    'grid.color':       '#1E3A5F',
    'grid.alpha':       0.5,
})

# ── Load & Clean Data ────────────────────────
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['borrow_date']  = pd.to_datetime(df['borrow_date'])
    df['return_date']  = pd.to_datetime(df['return_date'])
    df['hold_days']    = (df['return_date'] - df['borrow_date']).dt.days
    df['month']        = df['borrow_date'].dt.month
    df['month_name']   = df['borrow_date'].dt.strftime('%b')
    df.dropna(inplace=True)
    return df

# ── Chart 1: Top 10 Most Borrowed Books ─────
def chart_top_books(df):
    top = df['book_title'].value_counts().head(10).reset_index()
    top.columns = ['book_title', 'count']

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(BG_COLOR)
    bars = ax.barh(top['book_title'], top['count'],
                   color=ACCENT, edgecolor='none', height=0.6)
    for bar, val in zip(bars, top['count']):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                str(val), va='center', fontsize=11, color=TEXT_COLOR, fontweight='bold')
    ax.set_title('Top 10 Most Borrowed Books', fontsize=16,
                 fontweight='bold', color=TEXT_COLOR, pad=15)
    ax.set_xlabel('Number of Borrows', fontsize=12)
    ax.invert_yaxis()
    ax.grid(axis='x', alpha=0.3)
    ax.set_xlim(0, top['count'].max() + 3)
    plt.tight_layout()
    plt.savefig(f'{CHARTS_PATH}top_books.png', dpi=150, bbox_inches='tight')
    plt.close()

# ── Chart 2: Genre Distribution (Pie) ────────
def chart_genre(df):
    genre_counts = df['genre'].value_counts()
    colors = [ACCENT, GREEN, AMBER, PURPLE, '#EF4444', '#06B6D4']

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(BG_COLOR)
    wedges, texts, autotexts = ax.pie(
        genre_counts.values,
        labels=genre_counts.index,
        autopct='%1.1f%%',
        colors=colors[:len(genre_counts)],
        startangle=140,
        pctdistance=0.75,
        wedgeprops={'edgecolor': BG_COLOR, 'linewidth': 2}
    )
    for t in texts:    t.set_color(TEXT_COLOR); t.set_fontsize(12)
    for t in autotexts: t.set_color(BG_COLOR); t.set_fontsize(10); t.set_fontweight('bold')

    ax.set_title('Genre-wise Book Distribution', fontsize=16,
                 fontweight='bold', color=TEXT_COLOR, pad=15)
    plt.tight_layout()
    plt.savefig(f'{CHARTS_PATH}genre_pie.png', dpi=150, bbox_inches='tight')
    plt.close()

# ── Chart 3: Monthly Borrowing Trend ─────────
def chart_monthly(df):
    month_order = ['Jan','Feb','Mar','Apr','May','Jun',
                   'Jul','Aug','Sep','Oct','Nov','Dec']
    monthly = df.groupby('month_name').size().reindex(month_order).dropna()

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(BG_COLOR)
    ax.plot(monthly.index, monthly.values, color=PURPLE,
            linewidth=2.5, marker='o', markersize=7, markerfacecolor=PURPLE)
    ax.fill_between(monthly.index, monthly.values,
                    alpha=0.2, color=PURPLE)
    for x, y in zip(monthly.index, monthly.values):
        ax.text(x, y + 0.5, str(int(y)), ha='center',
                fontsize=10, color=TEXT_COLOR, fontweight='bold')
    ax.set_title('Monthly Borrowing Trend', fontsize=16,
                 fontweight='bold', color=TEXT_COLOR, pad=15)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Number of Borrows', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f'{CHARTS_PATH}monthly_trend.png', dpi=150, bbox_inches='tight')
    plt.close()

# ── Chart 4: Department-wise Activity ────────
def chart_department(df):
    dept = df['department'].value_counts().reset_index()
    dept.columns = ['department', 'count']
    colors = [ACCENT, GREEN, AMBER, PURPLE, '#EF4444', '#06B6D4']

    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor(BG_COLOR)
    bars = ax.bar(dept['department'], dept['count'],
                  color=colors[:len(dept)], edgecolor='none', width=0.55)
    for bar, val in zip(bars, dept['count']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                str(val), ha='center', fontsize=11,
                color=TEXT_COLOR, fontweight='bold')
    ax.set_title('Department-wise Borrowing Activity', fontsize=16,
                 fontweight='bold', color=TEXT_COLOR, pad=15)
    ax.set_xlabel('Department', fontsize=12)
    ax.set_ylabel('Number of Borrows', fontsize=12)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{CHARTS_PATH}department.png', dpi=150, bbox_inches='tight')
    plt.close()

# ── Chart 5: Heatmap (Month vs Department) ───
def chart_heatmap(df):
    pivot = df.pivot_table(index='department', columns='month_name',
                           values='record_id', aggfunc='count', fill_value=0)
    month_order = ['Jan','Feb','Mar','Apr','May','Jun',
                   'Jul','Aug','Sep','Oct','Nov','Dec']
    pivot = pivot.reindex(columns=[m for m in month_order if m in pivot.columns])

    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor(BG_COLOR)
    sns.heatmap(pivot, annot=True, fmt='d', cmap='Blues',
                ax=ax, linewidths=0.5, linecolor='#0D2137',
                annot_kws={'size': 11, 'color': TEXT_COLOR})
    ax.set_title('Borrowing Frequency: Department vs Month', fontsize=16,
                 fontweight='bold', color=TEXT_COLOR, pad=15)
    ax.set_xlabel('Month', fontsize=12, color=TEXT_COLOR)
    ax.set_ylabel('Department', fontsize=12, color=TEXT_COLOR)
    plt.tight_layout()
    plt.savefig(f'{CHARTS_PATH}heatmap.png', dpi=150, bbox_inches='tight')
    plt.close()

# ── Chart 6: Year-wise Reading Activity ──────
def chart_yearwise(df):
    year_data = df['year'].value_counts().sort_index()
    labels = [f'Year {y}' for y in year_data.index]
    colors = [ACCENT, GREEN, AMBER, PURPLE]

    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor(BG_COLOR)
    bars = ax.bar(labels, year_data.values,
                  color=colors[:len(year_data)], edgecolor='none', width=0.5)
    for bar, val in zip(bars, year_data.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                str(val), ha='center', fontsize=12,
                color=TEXT_COLOR, fontweight='bold')
    ax.set_title('Year-wise Student Reading Activity', fontsize=16,
                 fontweight='bold', color=TEXT_COLOR, pad=15)
    ax.set_xlabel('Student Year', fontsize=12)
    ax.set_ylabel('Number of Borrows', fontsize=12)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{CHARTS_PATH}yearwise.png', dpi=150, bbox_inches='tight')
    plt.close()

# ── Summary Stats ─────────────────────────────
def get_stats(df):
    return {
        'total_records':    len(df),
        'total_books':      df['book_id'].nunique(),
        'total_students':   df['student_id'].nunique(),
        'avg_hold_days':    round(df['hold_days'].mean(), 1),
        'most_borrowed':    df['book_title'].value_counts().idxmax(),
        'top_department':   df['department'].value_counts().idxmax(),
        'peak_month':       df['month_name'].value_counts().idxmax(),
        'top_genre':        df['genre'].value_counts().idxmax(),
    }

# ── Run All ───────────────────────────────────
def generate_all_charts():
    df = load_data()
    chart_top_books(df)
    chart_genre(df)
    chart_monthly(df)
    chart_department(df)
    chart_heatmap(df)
    chart_yearwise(df)
    print("✅ All 6 charts generated successfully!")
    return get_stats(df)

if __name__ == '__main__':
    stats = generate_all_charts()
    print("\n📊 Summary Stats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

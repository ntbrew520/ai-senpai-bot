from csv_loader import load_csv
from typing import Optional

def search_job_events(industry: Optional[str] = None, type_: Optional[str] = None, target_year: Optional[str] = None, format_: Optional[str] = None):
    df = load_csv("job_events.csv")
    
    if industry:
        df = df[df['industry'] == industry]
    if type_:
        df = df[df['type'] == type_]
    if target_year:
        df = df[df['target_year'].astype(str).str.contains(target_year)]
    if format_:
        df = df[df['format'] == format_]

    results = []
    for _, row in df.iterrows():
        results.append({
            "id": row['id'],
            "company_name": row['company_name'],
            "title": row['title'],
            "type": row['type'],
            "industry": row['industry'],
            "target_year": row['target_year'],
            "format": row['format'],
            "date": row['date'],
            "deadline": row['deadline'],
            "place": row['place'],
            "url": row['url'],
            "tags": row['tags']
        })
    return results

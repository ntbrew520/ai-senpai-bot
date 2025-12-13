from csv_loader import load_csv
from typing import Optional

def search_food(genre: Optional[str] = None, distance_tag: Optional[str] = None, keyword: Optional[str] = None):
    df = load_csv("food.csv")
    
    if genre:
        df = df[df['genre'] == genre]
    
    if distance_tag:
        df = df[df['distance_tag'] == distance_tag]
        
    if keyword:
        df = df[df.apply(lambda row: keyword in row['description'] or keyword in row['tags'], axis=1)]
        
    results = []
    for _, row in df.iterrows():
        results.append({
            "id": row['id'],
            "name": row['name'],
            "category_or_genre": row['genre'],
            "distance_tag": row['distance_tag'],
            "description": row['description'],
            "tags": row['tags']
        })
    return results

from csv_loader import load_csv
from gemini_client import generate_reply

def answer_job_tips(user_query: str):
    df = load_csv("job_tips.csv")
    
    keywords = user_query.split()
    matched_rows = []
    
    for _, row in df.iterrows():
        text_to_search = f"{row['category']} {row['tags']} {row['question_template']}"
        score = sum(1 for k in keywords if k in text_to_search)
        if score > 0:
            matched_rows.append((score, row))
            
    matched_rows.sort(key=lambda x: x[0], reverse=True)
    top_rows = [item[1] for item in matched_rows[:3]]
    
    tips_context = ""
    for row in top_rows:
        tips_context += f"カテゴリ: {row['category']}\n想定質問: {row['question_template']}\n先輩のアドバイス: {row['tip_memo']}\n---\n"
        
    if not tips_context:
        tips_context = "(特に関連するメモは見つかりませんでした)"

    prompt = f"""
あなたは大学の頼れる「就活強者の先輩(AI)」です。
後輩からの就活相談に乗ってください。

【先輩の就活メモ】
{tips_context}

【後輩の相談】
{user_query}

【回答ルール】
1. 先輩メモをベースにアドバイスすること。
2. 大学生にも分かる言葉で、具体的かつ「次に何をすべきか」を含めること。
3. 励ますこと。
"""
    return generate_reply(prompt)

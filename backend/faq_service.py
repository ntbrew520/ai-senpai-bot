from csv_loader import load_csv
from gemini_client import generate_reply

def search_faq_and_answer(user_query: str):
    df = load_csv("faq.csv")
    keywords = user_query.split()
    matched_rows = []
    
    for _, row in df.iterrows():
        text_to_search = f"{row['question']} {row['tags']}"
        score = sum(1 for k in keywords if k in text_to_search)
        if score > 0:
            matched_rows.append((score, row))
    
    matched_rows.sort(key=lambda x: x[0], reverse=True)
    top_rows = [item[1] for item in matched_rows[:5]]
    
    context_text = ""
    for row in top_rows:
        context_text += f"Q: {row['question']}\nA: {row['answer']}\n---\n"
    
    if not context_text:
        context_text = "(関連するFAQは見つかりませんでした)"

    prompt = f"""
あなたは大学の親切な「AI先輩」です。
以下の「公式FAQリスト」だけを根拠にして、学生の質問に答えてください。

【公式FAQリスト】
{context_text}

【学生の質問】
{user_query}

【ルール】
1. FAQリストにある情報に基づいて回答すること。
2. FAQに載っていない情報は勝手に創作せず、「ごめん、私のメモにはないな」「教務課で確認してみて」と正直に伝えること。
3. 口調は親しみやすい先輩風で。
"""
    return generate_reply(prompt)

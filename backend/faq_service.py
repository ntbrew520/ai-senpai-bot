from csv_loader import load_csv
from gemini_client import generate_reply

def search_faq_and_answer(user_query: str):
    # CSVを全件読み込む
    df = load_csv("faq.csv")
    
    # 検索ロジックを廃止し、CSVの中身をすべてテキスト化する
    # データ量が数千件を超えると遅くなるが、数百件ならこの方法が一番賢い
    context_text = ""
    for _, row in df.iterrows():
        context_text += f"Q: {row['question']}\nA: {row['answer']}\nTags: {row['tags']}\n---\n"
    
    if not context_text:
        context_text = "（FAQデータが空です）"

    # プロンプト作成
    prompt = f"""
あなたは大学の親切な「AI先輩」です。
以下の「公式FAQリスト」全体を読んで、学生の質問に最も適切な回答をしてください。

【公式FAQリスト】
{context_text}

【学生の質問】
{user_query}

【回答ルール】
1. 質問の意図を汲み取り、リストの中から最も近い情報を使って回答すること。
2. もしリストの中に全く関連する情報がなければ、「ごめん、その件については僕のメモ（FAQ）には載ってないんだ。教務課に聞いたほうがいいかも」と正直に答えること。
3. 口調は親しみやすい先輩風で。
"""
    return generate_reply(prompt)

"""
    return generate_reply(prompt)

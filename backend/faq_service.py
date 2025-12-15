from csv_loader import load_csv
from gemini_client import generate_reply

def search_faq_and_answer(user_query: str):
    # CSVを読み込む
    df = load_csv("faq.csv")
    
    # 【ここが重要】
    # キーワード検索を廃止し、CSVの中身を「すべて」Geminiに渡すように変更します。
    # これにより、ユーザーがどんな言葉で質問しても、Geminiが文脈を読んで探してくれるようになります。
    
    context_text = ""
    for _, row in df.iterrows():
        # 行ごとにテキスト化して連結
        context_text += f"Q: {row['question']}\nA: {row['answer']}\nTags: {row['tags']}\n---\n"
    
    # 万が一データが空の場合
    if not context_text:
        context_text = "（FAQデータが読み込めませんでした）"

    # Geminiへの命令文（プロンプト）
    prompt = f"""
あなたは大学の親切な「AI先輩」です。
以下の「公式FAQリスト」全体を読んで、学生の質問に最も適切な回答をしてください。

【公式FAQリスト】
{context_text}

【学生の質問】
{user_query}

【回答ルール】
1. 上記のリストにある情報「だけ」を根拠に回答すること。
2. もしリストの中に答えになりそうな情報が全くなければ、「ごめん、その件については僕のメモ（FAQ）には載ってないんだ。教務課に聞いたほうがいいかも」と正直に答えること。
3. 口調は親しみやすい先輩風で。
"""
    return generate_reply(prompt)

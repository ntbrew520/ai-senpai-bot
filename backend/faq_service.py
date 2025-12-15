import sys
from csv_loader import load_csv
from gemini_client import generate_reply

def search_faq_and_answer(user_query: str):
    # CSVを読み込む
    df = load_csv("faq.csv")
    
    # コンテキスト作成（全データ読み込み）
    context_text = ""
    for _, row in df.iterrows():
        context_text += f"Q: {row['question']}\nA: {row['answer']}\nTags: {row['tags']}\n---\n"
    
    if not context_text:
        context_text = "（FAQデータが読み込めませんでした）"

    # プロンプト作成
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
    
    # AIに回答させる
    answer_text = generate_reply(prompt)

    # ---------------------------------------------------------
    # 【追加機能】 Renderのログ画面に履歴を表示する
    # ---------------------------------------------------------
    print(f"--------------------------------------------------", file=sys.stderr)
    print(f"📝 [質問] {user_query}", file=sys.stderr)
    print(f"🤖 [回答] {answer_text}", file=sys.stderr)
    
    # もし「載ってない」「わからない」が含まれていたら、目立つように警告ログを出す
    if "載ってない" in answer_text or "わからない" in answer_text or "教務課" in answer_text:
        print(f"⚠️ [未解決] この質問はFAQ不足の可能性があります！", file=sys.stderr)
    
    print(f"--------------------------------------------------", file=sys.stderr)
    # ---------------------------------------------------------

    return answer_text



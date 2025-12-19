from csv_loader import load_csv
from gemini_client import generate_reply
import datetime
import sys

# ==========================================
# ログ保存機能（ログ画面への表示機能つき）
# ==========================================
def save_log_safely(question, answer):
    try:
        # 1. ファイルに保存（裏側の処理）
        with open("server.log", "a", encoding="utf-8") as f:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{now}] Q:{question} / A:{answer}\n")
            
        # 2. ログ画面に中身を表示（ここを追加しました！）
        print(f"--------------------------------------------------", file=sys.stderr)
        print(f"📝 [保存された質問] {question}", file=sys.stderr)
        print(f"🤖 [保存された回答] {answer}", file=sys.stderr)
        print(f"--------------------------------------------------", file=sys.stderr)
        
    except Exception as e:
        print(f"DEBUG: ログ保存失敗（無視します）: {e}", file=sys.stderr)

# ==========================================
# メイン処理
# ==========================================
def search_faq_and_answer(user_query: str):
    df = load_csv("faq.csv")
    
    context_text = ""
    for _, row in df.iterrows():
        context_text += f"Q: {row['question']}\nA: {row['answer']}\nTags: {row['tags']}\n---\n"
    
    if not context_text:
        context_text = "（FAQデータなし）"

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
    
    answer_text = generate_reply(prompt)

    # わからない時だけログに残す
    if "載ってない" in answer_text or "わからない" in answer_text or "教務課" in answer_text:
        save_log_safely(user_query, answer_text)

    return answer_text


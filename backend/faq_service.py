from csv_loader import load_csv
from gemini_client import generate_reply
import datetime
import sys

# ==========================================
# 【追加部分】絶対にアプリを落とさないログ保存機能
# ==========================================
def save_log_safely(question, answer):
    try:
        # "server.log" というファイルに追記する
        with open("server.log", "a", encoding="utf-8") as f:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 書き込む内容： [日時] 質問 / 回答
            f.write(f"[{now}] Q:{question} / A:{answer}\n")
            
        print("DEBUG: ログ保存成功", file=sys.stderr)
        
    except Exception as e:
        # 【重要】もし保存に失敗しても、エラーを表示するだけで何もしない（アプリを止めない）
        print(f"DEBUG: ログ保存失敗（でもドンマイ）: {e}", file=sys.stderr)

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
    
    # Geminiに回答させる
    answer_text = generate_reply(prompt)

    # ---------------------------------------------------------
    # 【追加】わからない時だけログに残す（安全装置付き）
    # ---------------------------------------------------------
    if "載ってない" in answer_text or "わからない" in answer_text or "教務課" in answer_text:
        # ここでさっきの安全な関数を呼ぶ
        save_log_safely(user_query, answer_text)

    return answer_text

"""
    return generate_reply(prompt)

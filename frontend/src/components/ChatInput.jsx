import React, { useState } from 'react';
const ChatInput = ({ onSend, placeholder }) => {
  const [text, setText] = useState("");
  const handleSend = () => { if (!text.trim()) return; onSend(text); setText(""); };
  const handleKeyDown = (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSend(); } };
  return (
    <div className="chat-input-area">
      <input className="chat-input" value={text} onChange={(e) => setText(e.target.value)} onKeyDown={handleKeyDown} placeholder={placeholder || "メッセージを入力"} />
      <button className="send-btn" onClick={handleSend}>送信</button>
    </div>
  );
};
export default ChatInput;

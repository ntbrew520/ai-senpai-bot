import React from 'react';
const MessageList = ({ messages }) => {
  return (
    <div className="message-list">
      {messages.map((msg, idx) => (
        <div key={idx} className={`message-row ${msg.role === 'user' ? 'user' : 'senpai'}`}>
          <div className="message-bubble">{msg.text}</div>
        </div>
      ))}
    </div>
  );
};
export default MessageList;

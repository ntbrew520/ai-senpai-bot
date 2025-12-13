import React from 'react';
const ChatHeader = ({ title }) => {
  return (
    <header className="chat-header">
      <div className="zju-icon">ZJU</div>
      <div className="title">{title}</div>
    </header>
  );
};
export default ChatHeader;

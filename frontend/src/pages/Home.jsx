import React, { useState, useEffect } from 'react';
import MessageList from '../components/MessageList';
import ChatInput from '../components/ChatInput';
import { postFaq, getFood, getPlay } from '../apiClient';

const Home = ({ category }) => {
  const [messages, setMessages] = useState([{ role: 'senpai', text: 'やあ!何か困ってることある?' }]);
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [genre, setGenre] = useState("");
  const [distance, setDistance] = useState("");
  const [keyword, setKeyword] = useState("");

  useEffect(() => {
    setMessages([{ role: 'senpai', text: 'やあ!何か困ってることある?' }]);
    setItems([]);
    setGenre(""); setDistance(""); setKeyword("");
  }, [category]);

  const handleFaqSend = async (text) => {
    setMessages(prev => [...prev, { role: 'user', text }]);
    setLoading(true);
    try {
      const res = await postFaq(text);
      setMessages(prev => [...prev, { role: 'senpai', text: res.answer }]);
    } catch (e) {
      setMessages(prev => [...prev, { role: 'senpai', text: "ごめん、通信エラーみたい。" }]);
    }
    setLoading(false);
  };

  const handleSearch = async () => {
    setLoading(true);
    try {
      let data = [];
      if (category === "美味しいお店") data = await getFood(genre, distance, keyword);
      else if (category === "遊ぶ場所") data = await getPlay(genre, distance, keyword);
      setItems(data);
    } catch (e) { console.error(e); }
    setLoading(false);
  };

  if (category === "学校生活") {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
        <div style={{ flex: 1, overflowY: 'auto' }}><MessageList messages={messages} /></div>
        <ChatInput onSend={handleFaqSend} placeholder="授業のこと、成績のこと..." />
      </div>
    );
  }

  return (
    <div>
      <div className="filter-bar">
        {category === "美味しいお店" && (
          <select onChange={(e) => setGenre(e.target.value)} value={genre}>
            <option value="">ジャンル:全て</option>
            <option value="日本食">日本食</option>
            <option value="洋食">洋食</option>
            <option value="中華">中華</option>
          </select>
        )}
        <select onChange={(e) => setDistance(e.target.value)} value={distance}>
          <option value="">距離:指定なし</option>
          <option value="near">近い</option>
          <option value="short">そこそこ</option>
          <option value="far">遠い</option>
        </select>
        <input className="filter-input" placeholder="キーワード" value={keyword} onChange={(e) => setKeyword(e.target.value)} />
        <button onClick={handleSearch} className="send-btn" style={{padding: '5px 15px'}}>検索</button>
      </div>
      <div className="card-list">
        {loading && <p>検索中...</p>}
        {items.map(item => (
          <div key={item.id} className="info-card">
            <h3>{item.name}</h3>
            <p style={{fontSize:'13px', margin:'5px 0'}}>{item.description}</p>
            <div className="tag-row"><span className="tag">{item.category_or_genre}</span></div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default Home;

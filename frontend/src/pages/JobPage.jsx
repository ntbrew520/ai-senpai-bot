import React, { useState } from 'react';
import MessageList from '../components/MessageList';
import ChatInput from '../components/ChatInput';
import { getJobEvents, postJobTips } from '../apiClient';

const JobPage = () => {
  const [tab, setTab] = useState("events");
  const [events, setEvents] = useState([]);
  const [industry, setIndustry] = useState("");
  const [type, setType] = useState("");
  const [messages, setMessages] = useState([{ role: 'senpai', text: '就活の悩み、なんでも聞いてくれ!' }]);

  const handleEventSearch = async () => {
    const data = await getJobEvents(industry, type, "", "");
    setEvents(data);
  };

  const handleTipsSend = async (text) => {
    setMessages(prev => [...prev, { role: 'user', text }]);
    try {
      const res = await postJobTips(text);
      setMessages(prev => [...prev, { role: 'senpai', text: res.answer }]);
    } catch (e) {
      setMessages(prev => [...prev, { role: 'senpai', text: "エラーが発生しました。" }]);
    }
  };

  return (
    <div>
      <div style={{ display:'flex', gap:'10px', marginBottom:'15px' }}>
        <button onClick={() => setTab("events")} style={{ flex:1, padding:'8px', background: tab==='events' ? 'var(--zju-blue)' : '#eee', color: tab==='events' ? '#fff' : '#333', border:'none', borderRadius:'5px' }}>イベント検索</button>
        <button onClick={() => setTab("tips")} style={{ flex:1, padding:'8px', background: tab==='tips' ? 'var(--zju-blue)' : '#eee', color: tab==='tips' ? '#fff' : '#333', border:'none', borderRadius:'5px' }}>就活相談</button>
      </div>

      {tab === "events" ? (
        <div>
          <div className="filter-bar">
            <select onChange={(e) => setIndustry(e.target.value)}><option value="">業界:全て</option><option value="IT">IT</option></select>
            <button onClick={handleEventSearch} className="send-btn" style={{padding:'5px 15px'}}>検索</button>
          </div>
          <div className="card-list">
            {events.map(ev => (
              <div key={ev.id} className="info-card">
                <h3>{ev.company_name} - {ev.title}</h3>
                <p style={{fontSize:'12px', color:'gray'}}>{ev.date}</p>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', height: 'calc(100vh - 180px)' }}>
          <div style={{ flex: 1, overflowY: 'auto' }}><MessageList messages={messages} /></div>
          <ChatInput onSend={handleTipsSend} placeholder="ガクチカの書き方..." />
        </div>
      )}
    </div>
  );
};
export default JobPage;

import { useState } from 'react';
import ChatHeader from './components/ChatHeader';
import CategorySelector from './components/CategorySelector';
import Home from './pages/Home';
import JobPage from './pages/JobPage';

function App() {
  const [currentCategory, setCurrentCategory] = useState("学校生活");

  const renderContent = () => {
    switch (currentCategory) {
      case "学校生活":
      case "美味しいお店":
      case "遊ぶ場所":
        return <Home category={currentCategory} />;
      case "就活":
        return <JobPage />;
      default:
        return <Home category="学校生活" />;
    }
  };

  return (
    <div className="app-container">
      <ChatHeader title="AI先輩 (ZJU)" />
      <div className="main-layout">
        <CategorySelector currentCategory={currentCategory} onSelect={setCurrentCategory} />
        <div className="content-area">
          {renderContent()}
        </div>
      </div>
    </div>
  );
}
export default App;

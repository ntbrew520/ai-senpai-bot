import React from 'react';
const categories = ["学校生活", "美味しいお店", "遊ぶ場所", "就活"];
const CategorySelector = ({ currentCategory, onSelect }) => {
  return (
    <div className="category-selector">
      {categories.map((cat) => (
        <button key={cat} className={`cat-btn ${currentCategory === cat ? 'active' : ''}`} onClick={() => onSelect(cat)}>
          {cat}
        </button>
      ))}
    </div>
  );
};
export default CategorySelector;

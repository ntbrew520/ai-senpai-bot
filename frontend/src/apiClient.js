const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function postFaq(query) {
  const res = await fetch(`${API_BASE_URL}/api/faq_answer`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });
  return res.json();
}

export async function getFood(genre, distance, keyword) {
  const params = new URLSearchParams();
  if (genre) params.append("genre", genre);
  if (distance) params.append("distance_tag", distance);
  if (keyword) params.append("keyword", keyword);
  const res = await fetch(`${API_BASE_URL}/api/food_search?${params.toString()}`);
  return res.json();
}

export async function getPlay(category, distance, keyword) {
  const params = new URLSearchParams();
  if (category) params.append("category", category);
  if (distance) params.append("distance_tag", distance);
  if (keyword) params.append("keyword", keyword);
  const res = await fetch(`${API_BASE_URL}/api/play_search?${params.toString()}`);
  return res.json();
}

export async function getJobEvents(industry, type, targetYear, format) {
  const params = new URLSearchParams();
  if (industry) params.append("industry", industry);
  if (type) params.append("type", type);
  if (targetYear) params.append("target_year", targetYear);
  if (format) params.append("format", format);
  const res = await fetch(`${API_BASE_URL}/api/jobs/events?${params.toString()}`);
  return res.json();
}

export async function postJobTips(query) {
  const res = await fetch(`${API_BASE_URL}/api/jobs/tips_answer`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });
  return res.json();
}

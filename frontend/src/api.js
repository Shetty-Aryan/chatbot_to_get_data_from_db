const BASE_URL = "https://chatbot-to-get-data-from-db.onrender.com";


export async function sendChatMessage(message) {
  const res = await fetch(`${BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  return res.json();
}
export async function getAddressByClientId(clientId) {
  const res = await fetch(
    `http://127.0.0.1:8000/clients/${clientId}/addresses`
  );
  return res.json();
}
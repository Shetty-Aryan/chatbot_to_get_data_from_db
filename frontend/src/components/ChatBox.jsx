import React, { useState } from "react";
import { sendChatMessage } from "../api";

export default function ChatBox({ onResponse }) {
  const [message, setMessage] = useState("");

  const sendMessage = async () => {
    if (!message.trim()) return;
    const response = await sendChatMessage(message);
    onResponse(response);
    setMessage("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  return (
    <>
      <input
        style={{
          width: "100%",
          padding: "10px",
          marginBottom: "10px",
          borderRadius: "4px",
          border: "none",
        }}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={handleKeyDown}   // 👈 THIS LINE
        placeholder="Type a query..."
      />

      <button
        style={{
          width: "100%",
          padding: "10px",
          backgroundColor: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: "4px",
          cursor: "pointer",
        }}
        onClick={sendMessage}
      >
        Send
      </button>
    </>
  );
}

import React, { useState } from "react";
import { sendChatMessage } from "../api";
import "./ChatBox.css";

function ChatBox({ onResponse }) {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    // Add user message
    const userMsg = { sender: "user", text: message };
    setChatHistory((prev) => [...prev, userMsg]);

    try {
      const res = await sendChatMessage(message);

      // Add bot reply
      let botText =
        res.type === "text"
          ? res.data
          : "Showing requested data below.";

      const botMsg = { sender: "bot", text: botText };
      setChatHistory((prev) => [...prev, botMsg]);

      // Send data to App (table)
      onResponse(res);
    } catch (err) {
      setChatHistory((prev) => [
        ...prev,
        { sender: "bot", text: "Something went wrong. Please try again." },
      ]);
    }

    setMessage("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="chatbox">
      {/* Chat history */}
      <div className="chat-history">
        {chatHistory.map((msg, idx) => (
          <div
            key={idx}
            className={`chat-message ${msg.sender}`}
          >
            <strong>{msg.sender === "user" ? "You" : "Bot"}:</strong>{" "}
            {msg.text}
          </div>
        ))}
      </div>

      {/* Input fixed at bottom */}
      <div className="chat-input">
        <input
          type="text"
          placeholder="Type a message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default ChatBox;

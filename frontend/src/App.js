import React, { useState } from "react";
import ChatBox from "./components/ChatBox";
import DataGrid from "./components/DataGrid";
import { getAddressByClientId } from "./api";
import "./App.css";

function App() {
  const [chatResponse, setChatResponse] = useState(null);
  const [details, setDetails] = useState(null);

  // 🔥 Clear client details whenever a new chat response arrives
  const handleChatResponse = (response) => {
    setChatResponse(response);
    setDetails(null); // CLEAR client details table
  };

  const handleRowClick = async (row) => {
    if (row.pty_id) {
      const addressData = await getAddressByClientId(row.pty_id);
      setDetails(addressData);
    }
  };

  return (
    <div className="app-container">
      {/* Left: Chat */}
      <div className="chat-panel">
        <h3>Chatbot</h3>
        <ChatBox onResponse={handleChatResponse} />
      </div>

      {/* Right: Results */}
      <div className="content-panel">
        <div className="card">
          <h3>Clients</h3>

          {chatResponse ? (
            chatResponse.type === "text" ? (
              <p className="bot-text">🤖 {chatResponse.data}</p>
            ) : (
              <DataGrid
                data={chatResponse.data}
                onRowClick={handleRowClick}
              />
            )
          ) : (
            <p className="empty">Ask the chatbot to load clients.</p>
          )}
        </div>

        <div className="card">
          <h3>Client Details</h3>

          {details ? (
            <DataGrid data={details} />
          ) : (
            <p className="empty">Click a client to view details.</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;

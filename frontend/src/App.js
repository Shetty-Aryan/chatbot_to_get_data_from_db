import React, { useState } from "react";
import ChatBox from "./components/ChatBox";
import DataGrid from "./components/DataGrid";
import { getAddressByClientId } from "./api";
import "./App.css";

function App() {
  const [chatResponse, setChatResponse] = useState(null);
  const [details, setDetails] = useState(null);

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
        <ChatBox onResponse={setChatResponse} />
      </div>

      {/* Right: Results */}
      <div className="content-panel">
        <div className="card">
          <h3>Clients</h3>
          {chatResponse ? (
            <DataGrid data={chatResponse.data} onRowClick={handleRowClick} />
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

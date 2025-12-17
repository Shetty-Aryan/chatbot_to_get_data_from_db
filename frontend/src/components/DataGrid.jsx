import React from "react";

function DataGrid({ data, onRowClick }) {
  // 🔒 SAFETY CHECKS (VERY IMPORTANT)
  if (!data || !Array.isArray(data) || data.length === 0) {
    return <p className="empty">No data found.</p>;
  }

  const columns = Object.keys(data[0]);

  return (
    <table border="1" width="100%" cellPadding="6">
      <thead>
        <tr>
          {columns.map((col) => (
            <th key={col}>{col}</th>
          ))}
        </tr>
      </thead>

      <tbody>
        {data.map((row, index) => (
          <tr
            key={index}
            onClick={() => onRowClick && onRowClick(row)}
            style={{ cursor: onRowClick ? "pointer" : "default" }}
          >
            {columns.map((col) => (
              <td key={col}>{String(row[col])}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default DataGrid;

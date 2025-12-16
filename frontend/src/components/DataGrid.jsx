export default function DataGrid({ data, onRowClick }) {
  if (!data || data.length === 0) return <p>No data</p>;

  const headers = Object.keys(data[0]);

  return (
    <table border="1" width="100%">
      <thead>
        <tr>
          {headers.map((h) => (
            <th key={h}>{h}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, idx) => (
          <tr
            key={idx}
            style={{ cursor: "pointer" }}
            onClick={() => onRowClick && onRowClick(row)}
          >
            {headers.map((h) => (
              <td key={h}>{row[h]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

import type { NetworkSample } from "../../types/network";

interface NetworkDataTableProps {
  data: NetworkSample[];
}

export default function NetworkDataTable({
  data,
}: NetworkDataTableProps) {
  return (
    <div className="data-table-card">
      <div className="section-header">
        <div>
          <h3>Network Data</h3>
          <p>Development and test network measurements</p>
        </div>
      </div>

      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Time</th>
              <th>Users</th>
              <th>Download</th>
              <th>Upload</th>
              <th>Latency</th>
              <th>Packet Loss</th>
              <th>CPU</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {data.map((sample) => (
              <tr key={sample.id}>
                <td>{sample.timestamp}</td>
                <td>{sample.activeUsers}</td>
                <td>{sample.downloadMbps} Mbps</td>
                <td>{sample.uploadMbps} Mbps</td>
                <td>{sample.latencyMs} ms</td>
                <td>{sample.packetLoss}%</td>
                <td>{sample.cpuUsage}%</td>
                <td>
                  <span className="table-status">{sample.deviceStatus}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}


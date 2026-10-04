import type { Anomaly } from "../../types/anomaly";

interface AnomalyTableProps {
  anomalies: Anomaly[];
}

export default function AnomalyTable({
  anomalies,
}: AnomalyTableProps) {
  return (
    <div className="data-table-card">
      <div className="section-header">
        <div>
          <h3>Detected Anomalies</h3>
          <p>Results from the selected detection methods</p>
        </div>
      </div>

      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Time</th>
              <th>Metric</th>
              <th>Value</th>
              <th>Method</th>
              <th>Severity</th>
              <th>Score</th>
              <th>Description</th>
            </tr>
          </thead>

          <tbody>
            {anomalies.map((anomaly) => (
              <tr key={anomaly.id}>
                <td>{anomaly.timestamp}</td>
                <td>{anomaly.metric}</td>
                <td>{anomaly.value}</td>
                <td>{anomaly.method}</td>
                <td>
                  <span
                    className={`severity ${anomaly.severity.toLowerCase()}`}
                  >
                    {anomaly.severity}
                  </span>
                </td>
                <td>{anomaly.score.toFixed(2)}</td>
                <td>{anomaly.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}


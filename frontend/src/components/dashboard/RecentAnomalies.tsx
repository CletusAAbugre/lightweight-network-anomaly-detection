import type { Anomaly } from "../../types/anomaly";

interface RecentAnomaliesProps {
  anomalies: Anomaly[];
}

export default function RecentAnomalies({
  anomalies,
}: RecentAnomaliesProps) {
  return (
    <div className="recent-anomalies">
      <div className="section-header">
        <h3>Recent Anomalies</h3>
        <span>{anomalies.length} detected</span>
      </div>

      {anomalies.map((anomaly) => (
        <div className="anomaly-item" key={anomaly.id}>
          <div>
            <strong>{anomaly.metric}</strong>
            <p>{anomaly.description}</p>
          </div>

          <div className="anomaly-item-right">
            <span className={`severity ${anomaly.severity.toLowerCase()}`}>
              {anomaly.severity}
            </span>
            <small>{anomaly.method}</small>
          </div>
        </div>
      ))}
    </div>
  );
}


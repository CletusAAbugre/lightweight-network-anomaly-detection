import { Bell, CheckCircle, AlertTriangle } from "lucide-react";
import { alertData } from "../data/developmentData";

export default function Alerts() {
  return (
    <div className="page-content">
      <div className="page-introduction">
        <h2>Alerts</h2>
        <p>
          Review alerts generated from detected network anomalies.
        </p>
      </div>

      <div className="alerts-list">
        {alertData.map((alert) => (
          <div className="alert-card" key={alert.id}>
            <div className="alert-icon">
              {alert.severity === "High" ? (
                <AlertTriangle size={22} />
              ) : (
                <Bell size={22} />
              )}
            </div>

            <div className="alert-content">
              <div className="alert-header">
                <h3>{alert.title}</h3>
                <span className={`severity ${alert.severity.toLowerCase()}`}>
                  {alert.severity}
                </span>
              </div>

              <p>{alert.message}</p>

              <small>{alert.timestamp}</small>
            </div>

            <div className="alert-status">
              {alert.status === "Resolved" ? (
                <>
                  <CheckCircle size={18} />
                  <span>Resolved</span>
                </>
              ) : (
                <span>Open</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

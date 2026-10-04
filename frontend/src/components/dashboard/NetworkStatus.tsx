interface NetworkStatusProps {
  status: string;
  lastUpdated: string;
}

export default function NetworkStatus({
  status,
  lastUpdated,
}: NetworkStatusProps) {
  const isOnline = status.toLowerCase() === "online";

  return (
    <div className="network-status">
      <div>
        <h3>Network Status</h3>
        <p>Awudua Hotspot Network</p>
      </div>

      <div className={`status-badge ${isOnline ? "online" : "offline"}`}>
        <span className="status-dot"></span>
        {status}
      </div>

      <small>Last updated: {lastUpdated}</small>
    </div>
  );
}

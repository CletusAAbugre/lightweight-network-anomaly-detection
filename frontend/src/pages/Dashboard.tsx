import {
  Users,
  Gauge,
  Clock3,
  PackageOpen,
} from "lucide-react";

import MetricCard from "../components/dashboard/MetricCard";
import NetworkStatus from "../components/dashboard/NetworkStatus";
import RecentAnomalies from "../components/dashboard/RecentAnomalies";
import TrafficChart from "../components/charts/TrafficChart";
import LatencyChart from "../components/charts/LatencyChart";
import {
  networkData,
  anomalyData,
} from "../data/developmentData";

export default function Dashboard() {
  const latestSample = networkData[networkData.length - 1];

  const averageLatency =
    networkData.reduce((total, sample) => total + sample.latencyMs, 0) /
    networkData.length;

  return (
    <div className="dashboard-page">
      <div className="development-banner">
        Development/Test Dataset — data shown here is simulated for MVP testing.
      </div>

      <NetworkStatus
        status={latestSample.deviceStatus}
        lastUpdated={latestSample.timestamp}
      />

      <div className="metrics-grid">
        <MetricCard
          title="Active Users"
          value={latestSample.activeUsers.toString()}
          subtitle="Current connected users"
          icon={<Users size={22} />}
        />

        <MetricCard
          title="Bandwidth"
          value={`${latestSample.bandwidthUtilization}%`}
          subtitle="Current utilization"
          icon={<Gauge size={22} />}
        />

        <MetricCard
          title="Average Latency"
          value={`${averageLatency.toFixed(0)} ms`}
          subtitle="Across test samples"
          icon={<Clock3 size={22} />}
        />

        <MetricCard
          title="Packet Loss"
          value={`${latestSample.packetLoss}%`}
          subtitle="Current packet loss"
          icon={<PackageOpen size={22} />}
        />
      </div>

      <div className="charts-grid">
        <TrafficChart data={networkData} />
        <LatencyChart data={networkData} />
      </div>

      <RecentAnomalies anomalies={anomalyData} />
    </div>
  );
}

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import type { NetworkSample } from "../../types/network";

interface LatencyChartProps {
  data: NetworkSample[];
}

export default function LatencyChart({ data }: LatencyChartProps) {
  const chartData = data.map((sample) => ({
    time: sample.timestamp.slice(11),
    latency: sample.latencyMs,
  }));

  return (
    <div className="chart-card">
      <div className="section-header">
        <div>
          <h3>Network Latency</h3>
          <p>Latency measurements over time</p>
        </div>
      </div>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="latency"
            name="Latency (ms)"
            strokeWidth={2}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}


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

interface TrafficChartProps {
  data: NetworkSample[];
}

export default function TrafficChart({ data }: TrafficChartProps) {
  const chartData = data.map((sample) => ({
    time: sample.timestamp.slice(11),
    download: sample.downloadMbps,
    upload: sample.uploadMbps,
  }));

  return (
    <div className="chart-card">
      <div className="section-header">
        <div>
          <h3>Network Traffic</h3>
          <p>Download and upload traffic over time</p>
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
            dataKey="download"
            name="Download (Mbps)"
            strokeWidth={2}
          />
          <Line
            type="monotone"
            dataKey="upload"
            name="Upload (Mbps)"
            strokeWidth={2}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}


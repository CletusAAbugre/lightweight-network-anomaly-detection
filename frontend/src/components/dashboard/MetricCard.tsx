import type { ReactNode } from "react";

interface MetricCardProps {
  title: string;
  value: string;
  subtitle: string;
  icon: ReactNode;
}

export default function MetricCard({
  title,
  value,
  subtitle,
  icon,
}: MetricCardProps) {
  return (
    <div className="metric-card">
      <div className="metric-card-header">
        <span>{title}</span>
        <span className="metric-card-icon">{icon}</span>
      </div>

      <div className="metric-card-value">{value}</div>

      <div className="metric-card-subtitle">{subtitle}</div>
    </div>
  );
}


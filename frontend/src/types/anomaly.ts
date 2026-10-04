export interface Anomaly {
  id: number;
  timestamp: string;
  metric: string;
  value: number;
  method: string;
  severity: string;
  score: number;
  description: string;
}

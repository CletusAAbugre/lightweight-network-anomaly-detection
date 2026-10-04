export interface NetworkSample {
  id: number;
  timestamp: string;
  activeUsers: number;
  downloadMbps: number;
  uploadMbps: number;
  bandwidthUtilization: number;
  latencyMs: number;
  packetLoss: number;
  cpuUsage: number;
  memoryUsage: number;
  deviceStatus: string;
}

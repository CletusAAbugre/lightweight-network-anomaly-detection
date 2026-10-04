const API_BASE_URL = "http://localhost:8000";

export async function getNetworkData() {
  const response = await fetch(`${API_BASE_URL}/api/network`);

  if (!response.ok) {
    throw new Error("Failed to fetch network data");
  }

  return response.json();
}

export async function getAnomalies() {
  const response = await fetch(`${API_BASE_URL}/api/anomalies`);

  if (!response.ok) {
    throw new Error("Failed to fetch anomalies");
  }

  return response.json();
}

export async function getAlerts() {
  const response = await fetch(`${API_BASE_URL}/api/alerts`);

  if (!response.ok) {
    throw new Error("Failed to fetch alerts");
  }

  return response.json();
}

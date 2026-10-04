import AnomalyTable from "../components/tables/AnomalyTable";
import { anomalyData } from "../data/developmentData";

export default function Anomalies() {
  return (
    <div className="page-content">
      <div className="page-introduction">
        <h2>Detected Anomalies</h2>
        <p>
          Review anomalies identified by the threshold, rolling statistical
          deviation, and Isolation Forest methods.
        </p>
      </div>

      <AnomalyTable anomalies={anomalyData} />
    </div>
  );
}

import NetworkDataTable from "../components/tables/NetworkDataTable";
import { networkData } from "../data/developmentData";

export default function NetworkData() {
  return (
    <div className="page-content">
      <div className="page-introduction">
        <h2>Network Data</h2>
        <p>
          Review network performance measurements collected for development
          and testing.
        </p>
      </div>

      <NetworkDataTable data={networkData} />
    </div>
  );
}

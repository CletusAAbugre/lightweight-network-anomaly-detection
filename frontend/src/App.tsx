import { useState } from "react";

import Sidebar from "./components/layout/Sidebar";
import Header from "./components/layout/Header";

import Dashboard from "./pages/Dashboard";
import NetworkData from "./pages/NetworkData";
import Anomalies from "./pages/Anomalies";
import Alerts from "./pages/Alerts";
import DetectionMethods from "./pages/DetectionMethods";
import Evaluation from "./pages/Evaluation";

function App() {
  const [activePage, setActivePage] = useState("Dashboard");

  const renderPage = () => {
    switch (activePage) {
      case "Network Data":
        return <NetworkData />;
      case "Anomalies":
        return <Anomalies />;
      case "Alerts":
        return <Alerts />;
      case "Detection Methods":
        return <DetectionMethods />;
      case "Evaluation":
        return <Evaluation />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <div className="app">
      <Sidebar
        activePage={activePage}
        onNavigate={setActivePage}
      />

      <div className="main-area">
        <Header activePage={activePage} />

        <main className="main-content">
          {renderPage()}
        </main>
      </div>
    </div>
  );
}

export default App;

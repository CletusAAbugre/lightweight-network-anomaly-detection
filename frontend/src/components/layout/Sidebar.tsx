import {
  LayoutDashboard,
  Activity,
  TriangleAlert,
  Bell,
  Brain,
  BarChart3,
} from "lucide-react";

interface SidebarProps {
  activePage: string;
  onNavigate: (page: string) => void;
}

const navigationItems = [
  { name: "Dashboard", icon: LayoutDashboard },
  { name: "Network Data", icon: Activity },
  { name: "Anomalies", icon: TriangleAlert },
  { name: "Alerts", icon: Bell },
  { name: "Detection Methods", icon: Brain },
  { name: "Evaluation", icon: BarChart3 },
];

export default function Sidebar({
  activePage,
  onNavigate,
}: SidebarProps) {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <h2>NetworkGuard</h2>
        <span>Anomaly Detection</span>
      </div>

      <nav className="sidebar-nav">
        {navigationItems.map((item) => {
          const Icon = item.icon;
          const isActive = activePage === item.name;

          return (
            <button
              key={item.name}
              className={`nav-item ${isActive ? "active" : ""}`}
              onClick={() => onNavigate(item.name)}
            >
              <Icon size={20} />
              <span>{item.name}</span>
            </button>
          );
        })}
      </nav>

      <div className="sidebar-footer">
        <span className="status-dot"></span>
        <span>Development Mode</span>
      </div>
    </aside>
  );
}

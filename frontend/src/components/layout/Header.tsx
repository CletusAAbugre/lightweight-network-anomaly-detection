import { Bell, Wifi } from "lucide-react";

interface HeaderProps {
  activePage: string;
}

export default function Header({ activePage }: HeaderProps) {
  return (
    <header className="header">
      <div>
        <h1>{activePage}</h1>
        <p>Awudua, Tarkwa, Ghana</p>
      </div>

      <div className="header-actions">
        <div className="connection-status">
          <Wifi size={18} />
          <span>Network Connected</span>
        </div>

        <button className="notification-button" type="button">
          <Bell size={20} />
        </button>
      </div>
    </header>
  );
}

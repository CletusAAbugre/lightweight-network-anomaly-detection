import { Activity, BarChart3, Brain } from "lucide-react";

const methods = [
  {
    name: "Threshold Baseline",
    icon: Activity,
    description:
      "Flags a network metric when its value exceeds a predefined threshold.",
    purpose: "Provides a simple baseline for comparison.",
  },
  {
    name: "Rolling Statistical Deviation",
    icon: BarChart3,
    description:
      "Compares current measurements with a rolling statistical baseline to identify unusual deviations.",
    purpose: "Detects changes relative to recent network behaviour.",
  },
  {
    name: "Isolation Forest",
    icon: Brain,
    description:
      "Uses an established unsupervised machine learning method to identify observations that differ from normal patterns.",
    purpose: "Provides a machine-learning-based comparison method.",
  },
];

export default function DetectionMethods() {
  return (
    <div className="page-content">
      <div className="page-introduction">
        <h2>Detection Methods</h2>
        <p>
          Compare the lightweight anomaly detection approaches used in the
          study.
        </p>
      </div>

      <div className="methods-grid">
        {methods.map((method) => {
          const Icon = method.icon;

          return (
            <div className="method-card" key={method.name}>
              <div className="method-icon">
                <Icon size={24} />
              </div>

              <h3>{method.name}</h3>

              <p>{method.description}</p>

              <div className="method-purpose">
                <strong>Purpose</strong>
                <span>{method.purpose}</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

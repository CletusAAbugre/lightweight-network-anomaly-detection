import { Target, Clock3, Cpu, ShieldCheck } from "lucide-react";

const evaluationMetrics = [
  {
    name: "Precision",
    value: "-",
    description: "Proportion of detected anomalies that are actual anomalies.",
    icon: Target,
  },
  {
    name: "Recall",
    value: "-",
    description: "Proportion of documented anomalies correctly detected.",
    icon: ShieldCheck,
  },
  {
    name: "F1 Score",
    value: "-",
    description: "Harmonic mean of precision and recall.",
    icon: Target,
  },
  {
    name: "MTTD",
    value: "-",
    description: "Mean time taken to detect a documented abnormal event.",
    icon: Clock3,
  },
  {
    name: "Computational Overhead",
    value: "-",
    description: "Resources required by each detection method.",
    icon: Cpu,
  },
];

export default function Evaluation() {
  return (
    <div className="page-content">
      <div className="page-introduction">
        <h2>Evaluation</h2>
        <p>
          Evaluation results will compare the three detection methods using
          common network data and documented abnormal events.
        </p>
      </div>

      <div className="evaluation-note">
        <strong>Evaluation status</strong>
        <span>
          Results are not available yet. The MVP currently provides the
          interface for the final evaluation.
        </span>
      </div>

      <div className="evaluation-grid">
        {evaluationMetrics.map((metric) => {
          const Icon = metric.icon;

          return (
            <div className="evaluation-card" key={metric.name}>
              <div className="evaluation-icon">
                <Icon size={22} />
              </div>

              <div>
                <h3>{metric.name}</h3>
                <div className="evaluation-value">{metric.value}</div>
                <p>{metric.description}</p>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

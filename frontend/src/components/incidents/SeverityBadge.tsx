interface SeverityBadgeProps {
  severity: string;
}

export default function SeverityBadge({
  severity,
}: SeverityBadgeProps) {

  const styles = {
    CRITICAL:
      "bg-red-100 text-red-700",

    HIGH:
      "bg-orange-100 text-orange-700",

    MEDIUM:
      "bg-yellow-100 text-yellow-700",

    LOW:
      "bg-green-100 text-green-700",
  };

  return (
    <span
      className={`rounded-full px-3 py-1 text-xs font-semibold ${
        styles[
          severity.toUpperCase() as keyof typeof styles
        ] ||
        "bg-slate-100 text-slate-700"
      }`}
    >
      {severity}
    </span>
  );
}
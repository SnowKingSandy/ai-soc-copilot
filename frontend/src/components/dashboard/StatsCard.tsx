import { ReactNode } from "react";

interface StatsCardProps {
  title: string;
  value: number;
  icon: ReactNode;
}

export default function StatsCard({
  title,
  value,
  icon,
}: StatsCardProps) {
  return (
    <div className="rounded-xl border bg-white p-6 shadow-md transition hover:shadow-lg">

      <div className="flex items-center justify-between">

        <h3 className="text-sm font-medium text-gray-500">
          {title}
        </h3>

        <div className="text-gray-700">
          {icon}
        </div>

      </div>

      <p className="mt-4 text-4xl font-bold">
        {value}
      </p>

    </div>
  );
} 
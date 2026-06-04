"use client";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

interface RiskScoreChartProps {
  data: {
    id: number;
    risk_score: number;
  }[];
}

export default function RiskScoreChart({
  data,
}: RiskScoreChartProps) {
  return (
    <div className="rounded-xl border bg-white p-6 shadow-sm">

      <h2 className="mb-4 text-xl font-semibold">
        Risk Score Trend
      </h2>

      <div className="h-80">

        <ResponsiveContainer
          width="100%"
          height="100%"
        >

          <LineChart data={data}>

            <XAxis dataKey="id" />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="risk_score"
              stroke="#ef4444"
              strokeWidth={3}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}
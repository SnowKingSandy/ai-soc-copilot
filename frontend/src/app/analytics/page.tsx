"use client";

import { useEffect, useState } from "react";

import { api } from "@/services/api";

import { Incident } from "@/types/incident";

import MetricsCard from "@/components/analytics/MetricsCard";
import SeverityChart from "@/components/analytics/SeverityChart";
import RiskScoreChart from "@/components/analytics/RiskScoreChart";

export default function AnalyticsPage() {

  const [incidents, setIncidents] =
    useState<Incident[]>([]);

  useEffect(() => {

    const fetchIncidents = async () => {

      try {

        const response =
          await api.get("/incidents");

        setIncidents(
          response.data
        );

      } catch (error) {

        console.error(error);
      }
    };

    fetchIncidents();

  }, []);

  const severityCounts = incidents.reduce(
    (acc, incident) => {

      const severity =
        incident.severity.toUpperCase();

      acc[severity] =
        (acc[severity] || 0) + 1;

      return acc;

    },
    {} as Record<string, number>
  );

  const severityData =
    Object.entries(severityCounts)
      .map(
        ([name, value]) => ({
          name,
          value,
        })
      );

  const riskData =
    incidents.map(
      (incident) => ({
        id: incident.id,
        risk_score:
          incident.risk_score,
      })
    );

  const averageRisk =
    incidents.length > 0
      ? (
          incidents.reduce(
            (sum, incident) =>
              sum +
              incident.risk_score,
            0
          ) /
          incidents.length
        ).toFixed(1)
      : "0";

  const highestThreat =
    Object.entries(
      incidents.reduce(
        (acc, incident) => {

          const threat =
            incident.detected_threat;

          acc[threat] =
            (acc[threat] || 0) + 1;

          return acc;

        },
        {} as Record<string, number>
      )
    )
      .sort(
        (a, b) =>
          b[1] - a[1]
      )[0]?.[0] || "N/A";

  return (
    <div className="space-y-8">

      <div>

        <h1 className="text-4xl font-bold">
          Analytics
        </h1>

        <p className="text-slate-500">
          Security analytics and threat trends
        </p>

      </div>

      <div className="grid gap-6 md:grid-cols-3">

        <MetricsCard
          title="Total Incidents"
          value={incidents.length}
        />

        <MetricsCard
          title="Average Risk Score"
          value={averageRisk}
        />

        <MetricsCard
          title="Top Threat"
          value={highestThreat}
        />

      </div>

      <div className="grid gap-6 lg:grid-cols-2">

        <SeverityChart
          data={severityData}
        />

        <RiskScoreChart
          data={riskData}
        />

      </div>

    </div>
  );
}
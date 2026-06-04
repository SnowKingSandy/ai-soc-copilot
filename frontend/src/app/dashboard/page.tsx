"use client";

import { useEffect, useState } from "react";

import { api } from "@/services/api";

import StatsCard from "@/components/dashboard/StatsCard";
import DashboardHeader from "@/components/dashboard/DashboardHeader";
import IncidentTable from "@/components/incidents/IncidentTable";
import ThreatChart from "@/components/analytics/ThreatChart";

import {
  Shield,
  AlertTriangle,
  Flame,
  BarChart3,
} from "lucide-react";

import {
  Stats,
  Incident,
} from "@/types/incident";

export default function Dashboard() {
  const [stats, setStats] = useState<Stats | null>(null);
  const [incidents, setIncidents] = useState<Incident[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const statsResponse = await api.get("/stats");
        setStats(statsResponse.data);

        const incidentsResponse =
          await api.get("/incidents");
        setIncidents(
          incidentsResponse.data
        );
      } catch (error) {
        console.error(
          "Dashboard Error:",
          error
        );
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="p-10">
        Loading...
      </div>
    );
  }

  if (!stats) {
    return (
      <div className="p-10">
        Failed to load dashboard
      </div>
    );
  }

  const threatCounts = incidents.reduce(
    (acc, incident) => {
      const threat =
        incident.detected_threat;

      acc[threat] =
        (acc[threat] || 0) + 1;

      return acc;
    },
    {} as Record<string, number>
  );

  const chartData =
    Object.entries(threatCounts).map(
      ([name, value]) => ({
        name,
        value,
      })
    );

  const topThreats = [...chartData]
    .sort((a, b) => b.value - a.value)
    .slice(0, 5);

  return (
    <div>
      <DashboardHeader />

      {/* Stats Cards */}
      <div className="grid grid-cols-1 gap-6 md:grid-cols-4">
        <StatsCard
          title="Total Incidents"
          value={stats.total_incidents}
          icon={<Shield size={20} />}
        />

        <StatsCard
          title="High Severity"
          value={stats.high}
          icon={<AlertTriangle size={20} />}
        />

        <StatsCard
          title="Critical"
          value={stats.critical}
          icon={<Flame size={20} />}
        />

        <StatsCard
          title="Medium"
          value={stats.medium}
          icon={<BarChart3 size={20} />}
        />
      </div>

      {/* Analytics Section */}
      <div className="mt-10 grid gap-6 lg:grid-cols-2">
        {/* Threat Chart */}
        <ThreatChart data={chartData} />

        {/* Top Threats Summary */}
        <div className="rounded-xl border bg-white p-6 shadow-sm">
          <div className="mb-5 flex items-center justify-between">
            <h3 className="text-lg font-semibold">
              Top Threats
            </h3>

            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs text-slate-600">
              Last 24h
            </span>
          </div>

          <div className="space-y-4">
            {topThreats.map(
              (threat, index) => (
                <div
                  key={threat.name}
                  className="flex items-center justify-between rounded-lg border p-3"
                >
                  <div className="flex items-center gap-3">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-slate-100 text-sm font-semibold">
                      #{index + 1}
                    </div>

                    <div>
                      <p className="font-medium">
                        {threat.name}
                      </p>

                      <p className="text-xs text-muted-foreground">
                        Threat Type
                      </p>
                    </div>
                  </div>

                  <div className="text-right">
                    <p className="text-lg font-bold">
                      {threat.value}
                    </p>

                    <p className="text-xs text-muted-foreground">
                      Incidents
                    </p>
                  </div>
                </div>
              )
            )}
          </div>
        </div>
      </div>

      {/* Incident Table */}
      <IncidentTable
        incidents={incidents}
      />
    </div>
  );
}
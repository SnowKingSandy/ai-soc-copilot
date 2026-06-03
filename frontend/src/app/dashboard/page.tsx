"use client";

import { useEffect, useState } from "react";

import { api } from "@/services/api";

import StatsCard from "@/components/dashboard/StatsCard";

import { Stats } from "@/types/incident";

export default function Dashboard() {

  const [stats, setStats] =
    useState<Stats | null>(null);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    const fetchStats = async () => {

      try {

        const response =
          await api.get("/stats");

        setStats(response.data);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);
      }
    };

    fetchStats();

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
        Failed to load stats
      </div>
    );
  }

  return (
    <div className="p-10">

      <h1 className="mb-8 text-4xl font-bold">
        AI SOC Dashboard
      </h1>

      <div className="grid grid-cols-1 gap-6 md:grid-cols-4">

        <StatsCard
          title="Total Incidents"
          value={stats.total_incidents}
        />

        <StatsCard
          title="High Severity"
          value={stats.high}
        />

        <StatsCard
          title="Critical"
          value={stats.critical}
        />

        <StatsCard
          title="Medium"
          value={stats.medium}
        />

      </div>

    </div>
  );
}
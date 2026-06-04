"use client";

import { useEffect, useState } from "react";
import { api } from "@/services/api";
import IncidentTable from "@/components/incidents/IncidentTable";
import { Incident } from "@/types/incident";

export default function IncidentsPage() {
  const [incidents, setIncidents] = useState<Incident[]>([]);

  useEffect(() => {
    api
      .get("/incidents")
      .then((res) => setIncidents(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Incidents</h1>

      <div className="mt-6">
        <IncidentTable incidents={incidents} />
      </div>
    </div>
  );
}

"use client";

import { useState } from "react";

import { Incident } from "@/types/incident";
import IncidentDetails from "./IncidentDetails";
import SeverityBadge from "./SeverityBadge";

interface IncidentTableProps {
  incidents: Incident[];
}

export default function IncidentTable({
  incidents,
}: IncidentTableProps) {
  const [selectedIncident, setSelectedIncident] =
    useState<Incident | null>(null);

  const [open, setOpen] = useState(false);

  const handleRowClick = (
    incident: Incident
  ) => {
    setSelectedIncident(incident);
    setOpen(true);
  };

  return (
    <>
      <div className="mt-10 overflow-hidden rounded-xl border bg-white shadow">
        <div className="border-b p-5">
          <h2 className="text-xl font-semibold">
            Recent Security Incidents
          </h2>
        </div>

        <table className="w-full">
          <thead className="bg-slate-100">
            <tr>
              <th className="p-4 text-left">
                Severity
              </th>

              <th className="p-4 text-left">
                Threat
              </th>

              <th className="p-4 text-left">
                MITRE
              </th>

              <th className="p-4 text-left">
                Risk
              </th>

              <th className="p-4 text-left">
                Source IP
              </th>
            </tr>
          </thead>

          <tbody>
            {incidents.map((incident) => (
              <tr
                key={incident.id}
                onClick={() =>
                  handleRowClick(incident)
                }
                className="cursor-pointer border-t transition hover:bg-slate-50"
              >
                <td className="p-4">
                  <SeverityBadge
                    severity={incident.severity}
                  />
                </td>

                <td className="p-4 font-medium">
                  {incident.detected_threat}
                </td>

                <td className="p-4 font-mono text-sm">
                  {incident.mitre_id}
                </td>

                <td className="p-4">
                  {incident.risk_score}
                </td>

                <td className="p-4 font-mono text-sm">
                  {incident.source_ip || "-"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <IncidentDetails
        incident={selectedIncident}
        open={open}
        onOpenChange={setOpen}
      />
    </>
  );
}
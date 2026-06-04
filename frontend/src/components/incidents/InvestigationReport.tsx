"use client";

import React from "react";
import { InvestigationReport as ReportType } from "@/types/incident";

interface Props {
  report: ReportType;
}

export default function InvestigationReport({ report }: Props) {
  if (!report) return null;

  return (
    <div className="mt-6 rounded-xl border p-4 bg-white">
      <h3 className="text-lg font-semibold">Investigation Report</h3>

      <div className="mt-3 space-y-3">
        <div>
          <h4 className="font-medium">Timeline</h4>
          <p className="text-sm text-muted-foreground">{report.timeline}</p>
        </div>

        <div>
          <h4 className="font-medium">Root Cause</h4>
          <p className="text-sm text-muted-foreground">{report.root_cause}</p>
        </div>

        <div>
          <h4 className="font-medium">Attack Chain</h4>
          <p className="text-sm text-muted-foreground">{report.attack_chain}</p>
        </div>

        <div>
          <h4 className="font-medium">Recommended Actions</h4>
          <ul className="list-disc list-inside text-sm text-muted-foreground">
            {report.recommended_actions.map((a, i) => (
              <li key={i}>{a}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

"use client";

import { useState } from "react";
import { api } from "@/services/api";
import { InvestigationReport } from "@/types/incident";

import { Incident } from "@/types/incident";

import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

import {
  ShieldAlert,
  Target,
  AlertTriangle,
  Activity,
  Globe,
  FileText,
} from "lucide-react";
import InvestigationReport from "./InvestigationReport";

interface IncidentDetailsProps {
  incident: Incident | null;
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export default function IncidentDetails({
  incident,
  open,
  onOpenChange,
}: IncidentDetailsProps) {
  if (!incident) return null;

  const [investigating, setInvestigating] = useState(false);
  const [report, setReport] = useState<InvestigationReport | null>(null);

  const severityColor = {
    Critical:
      "bg-red-100 text-red-700 border-red-200",
    High:
      "bg-orange-100 text-orange-700 border-orange-200",
    Medium:
      "bg-yellow-100 text-yellow-700 border-yellow-200",
    Low:
      "bg-green-100 text-green-700 border-green-200",
  };

  const severityClass =
    severityColor[
      incident.severity as keyof typeof severityColor
    ] ??
    "bg-slate-100 text-slate-700 border-slate-200";

  return (
    <Sheet
      open={open}
      onOpenChange={onOpenChange}
    >
      <SheetContent className="w-full sm:max-w-xl overflow-y-auto">
        <SheetHeader>
          <SheetTitle className="flex items-center gap-2 text-xl">
            <ShieldAlert className="h-5 w-5 text-red-500" />
            Incident Investigation
          </SheetTitle>
        </SheetHeader>

        <div className="mt-8 space-y-6">
          {/* Threat Header */}
          <div className="rounded-xl border bg-slate-50 p-5">
            <p className="text-xs uppercase tracking-wider text-muted-foreground">
              Detected Threat
            </p>

            <h2 className="mt-2 text-2xl font-bold">
              {incident.detected_threat}
            </h2>

            <div
              className={`mt-4 inline-flex rounded-full border px-3 py-1 text-sm font-medium ${severityClass}`}
            >
              {incident.severity} Severity
            </div>
          </div>

          {/* Metrics Grid */}
          <div className="grid grid-cols-2 gap-4">
            <div className="rounded-xl border p-4">
              <div className="flex items-center gap-2 text-muted-foreground">
                <Target className="h-4 w-4" />
                MITRE
              </div>

              <p className="mt-2 font-mono text-lg font-semibold">
                {incident.mitre_id}
              </p>
            </div>

            <div className="rounded-xl border p-4">
              <div className="flex items-center gap-2 text-muted-foreground">
                <AlertTriangle className="h-4 w-4" />
                Risk Score
              </div>

              <p className="mt-2 text-lg font-semibold">
                {incident.risk_score}
              </p>
            </div>
          </div>

          {/* Source Info */}
          <div className="rounded-xl border p-5">
            <div className="mb-4 flex items-center gap-2">
              <Globe className="h-4 w-4 text-blue-500" />
              <h3 className="font-semibold">
                Source Information
              </h3>
            </div>

            <div className="rounded-lg bg-slate-50 p-3">
              <p className="text-xs text-muted-foreground">
                Source IP
              </p>

              <p className="font-mono text-sm">
                {incident.source_ip || "Unknown"}
              </p>
            </div>
          </div>

          {/* Analysis Summary */}
          <div className="rounded-xl border p-5">
            <div className="mb-4 flex items-center gap-2">
              <FileText className="h-4 w-4 text-indigo-500" />
              <h3 className="font-semibold">
                AI Analysis Summary
              </h3>
            </div>

            <div className="rounded-lg bg-slate-50 p-4">
              <p className="leading-relaxed text-muted-foreground">
                {incident.summary ||
                  "No summary available."}
              </p>
            </div>
          </div>

          {/* Status Footer */}
          <div className="rounded-xl border border-green-200 bg-green-50 p-4">
            <div className="flex items-center gap-2">
              <Activity className="h-4 w-4 text-green-600" />

              <span className="font-medium text-green-700">
                Incident Logged and Available for Review
              </span>
            </div>

            <div className="mt-4">
              <button
                className="inline-flex items-center rounded-md bg-blue-600 px-4 py-2 text-sm text-white hover:bg-blue-700"
                onClick={async () => {
                  setInvestigating(true);
                  setReport(null);

                  try {
                    const res = await api.post("/investigate", {
                      incident_id: incident.id,
                    });

                    setReport(res.data);
                  } catch (e) {
                    setReport({
                      timeline: "",
                      root_cause: "Investigation failed",
                      attack_chain: "",
                      recommended_actions: [],
                    });
                  } finally {
                    setInvestigating(false);
                  }
                }}
              >
                {investigating ? "Investigating..." : "Investigate Incident"}
              </button>
            </div>
          </div>
        </div>

        {report && (
          <InvestigationReport report={report} />
        )}
      </SheetContent>
    </Sheet>
  );
}
import { ReactNode } from "react";

interface DashboardShellProps {
  children: ReactNode;
}

export default function DashboardShell({
  children,
}: DashboardShellProps) {
  return (
    <div className="flex min-h-screen bg-slate-100">

      <aside className="w-64 border-r bg-slate-900 text-white">

        <div className="border-b p-6">
          <h1 className="text-xl font-bold">
            AI SOC Copilot
          </h1>

          <p className="text-sm text-slate-400">
            Security Operations Center
          </p>
        </div>

        <nav className="p-4">

          <ul className="space-y-3">

            <li className="rounded-lg bg-slate-800 p-3">
              Dashboard
            </li>

            <li className="rounded-lg p-3 hover:bg-slate-800">
              Incidents
            </li>

            <li className="rounded-lg p-3 hover:bg-slate-800">
              Analytics
            </li>

            <li className="rounded-lg p-3 hover:bg-slate-800">
              Threat Intel
            </li>

          </ul>

        </nav>

      </aside>

      <main className="flex-1 p-8">
        {children}
      </main>

    </div>
  );
}
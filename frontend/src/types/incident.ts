export interface Incident {
  id: number;
  severity: string;
  attack_type: string;
  detected_threat: string;
  mitre_id: string;
  confidence: number;
  risk_score: number;
  source_ip: string | null;
  failed_attempts: number;
  summary: string;
}

export interface Stats {
  total_incidents: number;
  critical: number;
  high: number;
  medium: number;
  low: number;
}
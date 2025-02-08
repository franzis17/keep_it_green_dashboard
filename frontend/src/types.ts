export interface Emission {
  id: number,
  date: string,
  kwh_used: number,
  co2_emissions: number;
}

export interface EmissionsResponse {
  emissions: Emission[];
  total_emissions: number;
}

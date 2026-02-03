"""
Strava API Client with auto-refresh token support
"""
import os
import time
import requests
from datetime import datetime
from typing import Optional, Dict, List, Any

class StravaClient:
    BASE_URL = "https://www.strava.com/api/v3"
    AUTH_URL = "https://www.strava.com/oauth/token"
    
    def __init__(self):
        self.client_id = os.environ.get("STRAVA_CLIENT_ID")
        self.client_secret = os.environ.get("STRAVA_CLIENT_SECRET")
        self.access_token = os.environ.get("STRAVA_ACCESS_TOKEN")
        self.refresh_token = os.environ.get("STRAVA_REFRESH_TOKEN")
        self.token_expires_at = 0
        
        if not all([self.client_id, self.client_secret, self.access_token, self.refresh_token]):
            raise ValueError("Missing Strava credentials. Source /root/.secrets first.")
    
    def _refresh_token_if_needed(self) -> None:
        """Refresh access token if expired or about to expire (within 5 min)"""
        current_time = time.time()
        
        # Always try to refresh if token_expires_at is 0 (first call)
        if self.token_expires_at == 0 or current_time >= (self.token_expires_at - 300):
            try:
                response = requests.post(self.AUTH_URL, data={
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "grant_type": "refresh_token",
                    "refresh_token": self.refresh_token
                })
                
                if response.status_code == 200:
                    data = response.json()
                    self.access_token = data["access_token"]
                    self.refresh_token = data["refresh_token"]
                    self.token_expires_at = data["expires_at"]
                    print(f"[Strava] Token refreshed, expires at {datetime.fromtimestamp(self.token_expires_at)}")
                else:
                    print(f"[Strava] Token refresh failed: {response.text}")
            except Exception as e:
                print(f"[Strava] Token refresh error: {e}")
    
    def _get_headers(self) -> Dict[str, str]:
        """Get authorization headers, refreshing token if needed"""
        self._refresh_token_if_needed()
        return {"Authorization": f"Bearer {self.access_token}"}
    
    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make GET request to Strava API"""
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    
    def get_athlete(self) -> Dict[str, Any]:
        """Get authenticated athlete info"""
        return self._get("/athlete")
    
    def get_athlete_stats(self, athlete_id: int = 52431948) -> Dict[str, Any]:
        """Get athlete stats (totals)"""
        return self._get(f"/athletes/{athlete_id}/stats")
    
    def get_activities(
        self, 
        after: Optional[int] = None, 
        before: Optional[int] = None,
        per_page: int = 100,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Get activities with optional date filters
        
        Args:
            after: Epoch timestamp - only activities after this time
            before: Epoch timestamp - only activities before this time
            per_page: Number of activities per page (max 200)
            page: Page number
        """
        params = {"per_page": per_page, "page": page}
        if after:
            params["after"] = after
        if before:
            params["before"] = before
        
        return self._get("/athlete/activities", params)
    
    def get_activities_for_month(self, year: int, month: int) -> List[Dict[str, Any]]:
        """Get all activities for a specific month"""
        # Calculate epoch timestamps for start and end of month
        from calendar import monthrange
        
        start_date = datetime(year, month, 1)
        _, last_day = monthrange(year, month)
        end_date = datetime(year, month, last_day, 23, 59, 59)
        
        after = int(start_date.timestamp())
        before = int(end_date.timestamp())
        
        all_activities = []
        page = 1
        
        while True:
            activities = self.get_activities(after=after, before=before, page=page)
            if not activities:
                break
            all_activities.extend(activities)
            if len(activities) < 100:
                break
            page += 1
        
        return all_activities
    
    def get_recent_activities(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most recent activities"""
        return self.get_activities(per_page=limit)
    
    @staticmethod
    def categorize_activity(activity_type: str) -> str:
        """Categorize activity into swim/bike/run/other"""
        activity_type = activity_type.lower()
        
        if activity_type in ["swim", "openwater swim", "openwatersswim"]:
            return "swim"
        elif activity_type in ["ride", "virtualride", "virtual ride", "ebikeride"]:
            return "bike"
        elif activity_type in ["run", "virtualrun", "virtual run", "trailrun", "trail run"]:
            return "run"
        else:
            return "other"
    
    @staticmethod
    def calculate_month_totals(activities: List[Dict[str, Any]]) -> Dict[str, Dict[str, float]]:
        """
        Calculate totals for a list of activities, grouped by sport
        
        Returns dict with swim/bike/run keys, each containing:
        - distance_km: total distance in km
        - elevation_m: total elevation gain in meters
        - duration_hours: total moving time in hours
        - count: number of activities
        """
        totals = {
            "swim": {"distance_km": 0, "elevation_m": 0, "duration_hours": 0, "count": 0},
            "bike": {"distance_km": 0, "elevation_m": 0, "duration_hours": 0, "count": 0},
            "run": {"distance_km": 0, "elevation_m": 0, "duration_hours": 0, "count": 0},
            "other": {"distance_km": 0, "elevation_m": 0, "duration_hours": 0, "count": 0}
        }
        
        for activity in activities:
            category = StravaClient.categorize_activity(activity.get("type", ""))
            
            totals[category]["distance_km"] += activity.get("distance", 0) / 1000
            totals[category]["elevation_m"] += activity.get("total_elevation_gain", 0)
            totals[category]["duration_hours"] += activity.get("moving_time", 0) / 3600
            totals[category]["count"] += 1
        
        # Round values
        for cat in totals:
            totals[cat]["distance_km"] = round(totals[cat]["distance_km"], 2)
            totals[cat]["elevation_m"] = round(totals[cat]["elevation_m"], 0)
            totals[cat]["duration_hours"] = round(totals[cat]["duration_hours"], 2)
        
        return totals


# Singleton instance
_client = None

def get_client() -> StravaClient:
    """Get or create Strava client singleton"""
    global _client
    if _client is None:
        _client = StravaClient()
    return _client


if __name__ == "__main__":
    # Quick test
    client = get_client()
    
    print("Testing Strava Client...")
    
    # Get athlete
    athlete = client.get_athlete()
    print(f"\nAthlete: {athlete.get('firstname')} {athlete.get('lastname')}")
    
    # Get stats
    stats = client.get_athlete_stats()
    print(f"\nAll-time runs: {stats['all_run_totals']['distance'] / 1000:.0f} km")
    print(f"All-time rides: {stats['all_ride_totals']['distance'] / 1000:.0f} km")
    print(f"All-time swims: {stats['all_swim_totals']['distance'] / 1000:.0f} km")
    
    # Get January 2026 activities
    jan_2026 = client.get_activities_for_month(2026, 1)
    print(f"\nJaneiro 2026: {len(jan_2026)} atividades")
    
    totals = client.calculate_month_totals(jan_2026)
    print(f"  Run: {totals['run']['distance_km']} km ({totals['run']['count']} atividades)")
    print(f"  Bike: {totals['bike']['distance_km']} km ({totals['bike']['count']} atividades)")
    print(f"  Swim: {totals['swim']['distance_km']} km ({totals['swim']['count']} atividades)")

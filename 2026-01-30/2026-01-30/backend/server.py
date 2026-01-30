"""
Flask API Server for Triathlon Dashboard
"""
import os
import json
from datetime import datetime
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from strava_client import get_client, StravaClient

app = Flask(__name__, static_folder="..")
CORS(app)

GOALS_FILE = os.path.join(os.path.dirname(__file__), "goals.json")


def load_goals():
    """Load goals from JSON file"""
    try:
        with open(GOALS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"monthly": {"run_km": 200, "bike_km": 150, "swim_km": 20}}


def save_goals(goals):
    """Save goals to JSON file"""
    with open(GOALS_FILE, "w") as f:
        json.dump(goals, f, indent=2)


@app.route("/")
def index():
    """Serve the dashboard HTML"""
    return send_from_directory("..", "triathlon-dashboard.html")


@app.route("/api/activities")
def get_activities():
    """
    Get recent activities
    Query params:
    - limit: number of activities (default 10)
    - month: specific month (1-12)
    - year: specific year
    """
    try:
        client = get_client()
        
        limit = request.args.get("limit", 10, type=int)
        month = request.args.get("month", type=int)
        year = request.args.get("year", type=int)
        
        if month and year:
            activities = client.get_activities_for_month(year, month)
        else:
            activities = client.get_recent_activities(limit)
        
        # Format activities for frontend
        formatted = []
        for act in activities:
            formatted.append({
                "id": act.get("id"),
                "name": act.get("name"),
                "type": act.get("type"),
                "category": StravaClient.categorize_activity(act.get("type", "")),
                "distance_km": round(act.get("distance", 0) / 1000, 2),
                "distance_m": act.get("distance", 0),
                "moving_time_seconds": act.get("moving_time", 0),
                "moving_time_formatted": format_duration(act.get("moving_time", 0)),
                "elevation_gain": act.get("total_elevation_gain", 0),
                "average_heartrate": act.get("average_heartrate"),
                "average_speed": act.get("average_speed"),
                "average_watts": act.get("average_watts"),
                "start_date": act.get("start_date_local"),
                "pace": calculate_pace(act)
            })
        
        return jsonify({
            "success": True,
            "count": len(formatted),
            "activities": formatted
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/stats")
def get_stats():
    """Get athlete all-time stats"""
    try:
        client = get_client()
        stats = client.get_athlete_stats()
        
        return jsonify({
            "success": True,
            "stats": {
                "all_time": {
                    "run": {
                        "distance_km": round(stats["all_run_totals"]["distance"] / 1000, 0),
                        "count": stats["all_run_totals"]["count"],
                        "elevation_m": round(stats["all_run_totals"]["elevation_gain"], 0),
                        "moving_time_hours": round(stats["all_run_totals"]["moving_time"] / 3600, 0)
                    },
                    "bike": {
                        "distance_km": round(stats["all_ride_totals"]["distance"] / 1000, 0),
                        "count": stats["all_ride_totals"]["count"],
                        "elevation_m": round(stats["all_ride_totals"]["elevation_gain"], 0),
                        "moving_time_hours": round(stats["all_ride_totals"]["moving_time"] / 3600, 0)
                    },
                    "swim": {
                        "distance_km": round(stats["all_swim_totals"]["distance"] / 1000, 0),
                        "count": stats["all_swim_totals"]["count"],
                        "moving_time_hours": round(stats["all_swim_totals"]["moving_time"] / 3600, 0)
                    }
                },
                "ytd": {
                    "run": {
                        "distance_km": round(stats["ytd_run_totals"]["distance"] / 1000, 2),
                        "count": stats["ytd_run_totals"]["count"],
                        "elevation_m": round(stats["ytd_run_totals"]["elevation_gain"], 0),
                        "moving_time_hours": round(stats["ytd_run_totals"]["moving_time"] / 3600, 2)
                    },
                    "bike": {
                        "distance_km": round(stats["ytd_ride_totals"]["distance"] / 1000, 2),
                        "count": stats["ytd_ride_totals"]["count"],
                        "elevation_m": round(stats["ytd_ride_totals"]["elevation_gain"], 0),
                        "moving_time_hours": round(stats["ytd_ride_totals"]["moving_time"] / 3600, 2)
                    },
                    "swim": {
                        "distance_km": round(stats["ytd_swim_totals"]["distance"] / 1000, 2),
                        "count": stats["ytd_swim_totals"]["count"],
                        "moving_time_hours": round(stats["ytd_swim_totals"]["moving_time"] / 3600, 2)
                    }
                }
            }
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/yoy")
def get_yoy_comparison():
    """
    Get Year-over-Year comparison for January
    Compares Janeiro 2026 vs Janeiro 2025
    """
    try:
        client = get_client()
        
        # Get activities for both months
        jan_2026 = client.get_activities_for_month(2026, 1)
        jan_2025 = client.get_activities_for_month(2025, 1)
        
        # Calculate totals
        totals_2026 = client.calculate_month_totals(jan_2026)
        totals_2025 = client.calculate_month_totals(jan_2025)
        
        # Calculate evolution percentages
        def calc_evolution(current, previous):
            if previous == 0:
                return 100 if current > 0 else 0
            return round(((current - previous) / previous) * 100, 1)
        
        comparison = {
            "2025": totals_2025,
            "2026": totals_2026,
            "evolution": {
                "swim": {
                    "distance_pct": calc_evolution(totals_2026["swim"]["distance_km"], totals_2025["swim"]["distance_km"]),
                    "count_pct": calc_evolution(totals_2026["swim"]["count"], totals_2025["swim"]["count"])
                },
                "bike": {
                    "distance_pct": calc_evolution(totals_2026["bike"]["distance_km"], totals_2025["bike"]["distance_km"]),
                    "count_pct": calc_evolution(totals_2026["bike"]["count"], totals_2025["bike"]["count"])
                },
                "run": {
                    "distance_pct": calc_evolution(totals_2026["run"]["distance_km"], totals_2025["run"]["distance_km"]),
                    "count_pct": calc_evolution(totals_2026["run"]["count"], totals_2025["run"]["count"])
                }
            }
        }
        
        return jsonify({
            "success": True,
            "period": "Janeiro",
            "comparison": comparison
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/goals", methods=["GET"])
def get_goals():
    """
    Get goals with current progress
    """
    try:
        client = get_client()
        goals = load_goals()
        
        # Get current month activities
        now = datetime.now()
        current_month_activities = client.get_activities_for_month(now.year, now.month)
        current_totals = client.calculate_month_totals(current_month_activities)
        
        # Calculate progress
        monthly_goals = goals.get("monthly", {})
        progress = {
            "run": {
                "goal": monthly_goals.get("run_km", 200),
                "current": current_totals["run"]["distance_km"],
                "percent": min(100, round((current_totals["run"]["distance_km"] / monthly_goals.get("run_km", 200)) * 100, 1))
            },
            "bike": {
                "goal": monthly_goals.get("bike_km", 150),
                "current": current_totals["bike"]["distance_km"],
                "percent": min(100, round((current_totals["bike"]["distance_km"] / monthly_goals.get("bike_km", 150)) * 100, 1))
            },
            "swim": {
                "goal": monthly_goals.get("swim_km", 20),
                "current": current_totals["swim"]["distance_km"],
                "percent": min(100, round((current_totals["swim"]["distance_km"] / monthly_goals.get("swim_km", 20)) * 100, 1))
            }
        }
        
        return jsonify({
            "success": True,
            "goals": goals,
            "progress": progress,
            "month": now.strftime("%B %Y")
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/goals", methods=["POST"])
def update_goals():
    """Update goals"""
    try:
        data = request.get_json()
        goals = load_goals()
        
        if "monthly" in data:
            goals["monthly"].update(data["monthly"])
        if "yearly" in data:
            goals["yearly"] = goals.get("yearly", {})
            goals["yearly"].update(data["yearly"])
        
        save_goals(goals)
        
        return jsonify({"success": True, "goals": goals})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/month/<int:year>/<int:month>")
def get_month_summary(year: int, month: int):
    """Get summary for a specific month"""
    try:
        client = get_client()
        activities = client.get_activities_for_month(year, month)
        totals = client.calculate_month_totals(activities)
        
        return jsonify({
            "success": True,
            "year": year,
            "month": month,
            "totals": totals,
            "activity_count": len(activities)
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


def format_duration(seconds: int) -> str:
    """Format seconds as HH:MM:SS or MM:SS"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def calculate_pace(activity: dict) -> str:
    """Calculate pace based on activity type"""
    distance = activity.get("distance", 0)
    moving_time = activity.get("moving_time", 0)
    activity_type = activity.get("type", "").lower()
    
    if distance == 0 or moving_time == 0:
        return "-"
    
    category = StravaClient.categorize_activity(activity_type)
    
    if category == "run":
        # min/km
        pace_seconds = moving_time / (distance / 1000)
        mins = int(pace_seconds // 60)
        secs = int(pace_seconds % 60)
        return f"{mins}:{secs:02d}/km"
    
    elif category == "swim":
        # min/100m
        pace_seconds = moving_time / (distance / 100)
        mins = int(pace_seconds // 60)
        secs = int(pace_seconds % 60)
        return f"{mins}:{secs:02d}/100m"
    
    elif category == "bike":
        # km/h
        speed_kmh = (distance / 1000) / (moving_time / 3600)
        return f"{speed_kmh:.1f} km/h"
    
    return "-"


if __name__ == "__main__":
    import sys
    debug_mode = "--debug" in sys.argv
    
    print("🚴 Starting Triathlon Dashboard API...")
    print("📍 Dashboard: http://localhost:5000/")
    print("📊 API endpoints:")
    print("   GET /api/activities - Recent activities")
    print("   GET /api/stats - Athlete stats")
    print("   GET /api/yoy - Year-over-year comparison")
    print("   GET /api/goals - Goals and progress")
    print()
    
    app.run(host="0.0.0.0", port=5000, debug=debug_mode, threaded=True)

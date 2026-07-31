from typing import Literal

from fastmcp import FastMCP

mcp = FastMCP("Travel Tools")


@mcp.tool
def calculate_trip_budget(
    flight_cost: float,
    hotel_cost: float,
    food_cost: float,
    activities_cost: float,
    local_transport_cost: float = 0,
    other_cost: float = 0,
) -> dict:
    """Calculate a trip's total cost from supplied cost components."""

    values = {
        "flight_cost": flight_cost,
        "hotel_cost": hotel_cost,
        "food_cost": food_cost,
        "activities_cost": activities_cost,
        "local_transport_cost": local_transport_cost,
        "other_cost": other_cost,
    }

    if any(value < 0 for value in values.values()):
        raise ValueError("Costs cannot be negative.")

    return {**values, "total_cost": round(sum(values.values()), 2)}


@mcp.tool
def recommend_destination(
    preference: str,
    budget: float,
    trip_length_days: int = 5,
    travel_region: Literal["India", "Asia", "Europe", "Anywhere"] = "Anywhere",
) -> dict:
    """Recommend sample destinations using preference, budget, duration, and region."""

    if budget <= 0:
        raise ValueError("Budget must be greater than zero.")
    if trip_length_days <= 0:
        raise ValueError("Trip length must be greater than zero.")

    text = preference.lower()
    catalogue = {
        "beach": {
            "India": ["Goa", "Varkala", "Pondicherry"],
            "Asia": ["Phuket", "Bali", "Da Nang"],
            "Europe": ["Algarve", "Crete", "Split"],
            "Anywhere": ["Goa", "Bali", "Phuket"],
        },
        "mountain": {
            "India": ["Manali", "Dharamshala", "Sikkim"],
            "Asia": ["Pokhara", "Da Lat", "Chiang Mai"],
            "Europe": ["Innsbruck", "Zakopane", "Bled"],
            "Anywhere": ["Manali", "Pokhara", "Bled"],
        },
        "history": {
            "India": ["Jaipur", "Hampi", "Varanasi"],
            "Asia": ["Kyoto", "Siem Reap", "Ayutthaya"],
            "Europe": ["Rome", "Athens", "Prague"],
            "Anywhere": ["Jaipur", "Kyoto", "Rome"],
        },
        "food": {
            "India": ["Delhi", "Lucknow", "Amritsar"],
            "Asia": ["Bangkok", "Osaka", "Penang"],
            "Europe": ["Bologna", "Lisbon", "Lyon"],
            "Anywhere": ["Delhi", "Bangkok", "Bologna"],
        },
        "nature": {
            "India": ["Munnar", "Meghalaya", "Coorg"],
            "Asia": ["Sri Lanka", "Sabah", "Ninh Binh"],
            "Europe": ["Slovenia", "Madeira", "Scotland"],
            "Anywhere": ["Munnar", "Sri Lanka", "Slovenia"],
        },
    }

    category = next((key for key in catalogue if key in text), "nature")
    destinations = catalogue[category][travel_region]

    return {
        "preference_category": category,
        "region": travel_region,
        "trip_length_days": trip_length_days,
        "total_budget": budget,
        "approximate_daily_budget": round(budget / trip_length_days, 2),
        "recommendations": destinations,
        "note": "Illustrative recommendations; verify live prices and entry requirements.",
    }


@mcp.tool
def estimate_daily_cost(
    accommodation_per_night: float,
    meals_per_day: float,
    transport_per_day: float,
    activities_per_day: float,
    number_of_days: int,
) -> dict:
    """Estimate daily and total on-ground trip costs, excluding flights."""

    if number_of_days <= 0:
        raise ValueError("Number of days must be greater than zero.")

    costs = [
        accommodation_per_night,
        meals_per_day,
        transport_per_day,
        activities_per_day,
    ]
    if any(cost < 0 for cost in costs):
        raise ValueError("Costs cannot be negative.")

    daily_total = round(sum(costs), 2)
    return {
        "daily_total": daily_total,
        "number_of_days": number_of_days,
        "estimated_on_ground_total": round(daily_total * number_of_days, 2),
        "excludes": ["flights", "visa fees", "insurance", "shopping"],
    }


@mcp.tool
def build_itinerary(
    destination: str,
    number_of_days: int,
    travel_style: Literal["budget", "balanced", "comfort", "adventure", "relaxed"] = "balanced",
    interests: str = "local culture, food, and major attractions",
) -> dict:
    """Build a simple day-by-day itinerary template."""

    if number_of_days < 1 or number_of_days > 30:
        raise ValueError("number_of_days must be between 1 and 30.")

    days = []
    for day in range(1, number_of_days + 1):
        if day == 1:
            plan = (
                f"Arrive in {destination}, check in, explore the nearby area, "
                "and have a local dinner."
            )
        elif day == number_of_days:
            plan = (
                f"Enjoy a relaxed morning in {destination}, buy souvenirs, "
                "check out, and depart."
            )
        else:
            plan = (
                f"Explore {destination} with a {travel_style} pace, focusing on "
                f"{interests}. Include rest and meal breaks."
            )
        days.append({"day": day, "plan": plan})

    return {
        "destination": destination,
        "travel_style": travel_style,
        "interests": interests,
        "itinerary": days,
        "note": "Check live opening hours, transport schedules, and reservations.",
    }


if __name__ == "__main__":
    mcp.run()

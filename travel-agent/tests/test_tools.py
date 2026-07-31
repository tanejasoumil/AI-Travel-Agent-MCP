import pytest

from mcp_server.server import (
    build_itinerary,
    calculate_trip_budget,
    estimate_daily_cost,
    recommend_destination,
)


def test_calculate_trip_budget() -> None:
    result = calculate_trip_budget(300, 500, 200, 150)
    assert result["total_cost"] == 1150


def test_negative_cost_is_rejected() -> None:
    with pytest.raises(ValueError):
        calculate_trip_budget(-1, 500, 200, 150)


def test_recommend_destination() -> None:
    result = recommend_destination("beach", 1000, 5, "India")
    assert "Goa" in result["recommendations"]


def test_estimate_daily_cost() -> None:
    result = estimate_daily_cost(100, 40, 20, 30, 5)
    assert result["estimated_on_ground_total"] == 950


def test_itinerary_length() -> None:
    result = build_itinerary("Kyoto", 4, "balanced")
    assert len(result["itinerary"]) == 4

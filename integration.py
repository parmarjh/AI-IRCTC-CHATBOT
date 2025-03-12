"""
This module simulates integration with the Indian Railways' APIs.  
In real implementations, this module would perform secure REST API calls to fetch live data.
"""

def fetch_train_schedule(train_id: str) -> dict:
    """
    Simulates fetching a train schedule based on a train ID.

    Args:
        train_id (str): The train number or ID.

    Returns:
        dict: A dummy schedule containing departure time, arrival time,
              duration, and a list of stops.
    """
    schedule = {
        "departure": "10:00 AM",
        "arrival": "04:00 PM",
        "duration": "6 hours",
        "stops": ["Station A", "Station B", "Station C"]
    }
    return schedule

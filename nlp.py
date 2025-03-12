"""
This module simulates basic natural language understanding.
For production, consider integrating with a pre-trained model from Hugging Face Transformers.
"""

def analyze_intent(text: str) -> str:
    """
    Analyzes the input text to determine the user intent.
    For this PoC, the function uses simple keyword-based detection.

    Args:
        text (str): User input message.

    Returns:
        str: Detected intent, e.g., "train_schedule", "ticket_booking",
             "refund_cancellation", or "general_query".
    """
    text_lower = text.lower()
    if "schedule" in text_lower or "train" in text_lower:
        return "train_schedule"
    elif "booking" in text_lower or "ticket" in text_lower:
        return "ticket_booking"
    elif "refund" in text_lower or "cancel" in text_lower:
        return "refund_cancellation"
    else:
        return "general_query"

"""
This module maps the recognized intent to a conversational response.
In a production system, this would be extended to handle dialog context more robustly.
"""

def get_response(intent: str, message: str = "") -> str:
    """
    Returns a chatbot response based on the detected intent.

    Args:
        intent (str): The intent extracted by the NLP module.
        message (str): The original user message (if further context is needed).

    Returns:
        str: A response message tailored to the detected intent.
    """
    if intent == "train_schedule":
        return ("It looks like you're inquiring about a train schedule. "
                "Please provide the train number for exact details.")
    elif intent == "ticket_booking":
        return ("For ticket booking information, please specify the travel date and train number.")
    elif intent == "refund_cancellation":
        return ("I can help with refunds and cancellations. Kindly provide your booking reference.")
    else:
        return ("I'm here to assist with your Indian Railways queries. Could you please provide more details?")

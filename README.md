# AI Agent-Based Chatbot for the Indian Railways Support System

This repository contains a Proof of Concept (PoC) for an AI agent-based chatbot designed to support the Indian Railways system. The solution demonstrates how Python and Flask can be used to develop an API-based chatbot backend that integrates a simple NLP pipeline, dialogue management, and simulated data integration for handling queries related to train schedules, ticket bookings, and refunds/cancellations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-locally)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Docker Usage](#docker-usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The AI Agent-Based Chatbot is designed to enhance the customer support experience for Indian Railways users by quickly addressing a wide range of queries, including:

- **Ticket bookings:** Information on ticket availability and booking procedures
- **Train schedules:** Real-time updates on departure, arrival, and delays
- **Refunds & cancellations:** Guidance on policies and steps for processing refunds or cancellations

This project serves as the starting point to build a scalable, production-ready chatbot by demonstrating basic NLP-based intent recognition and modular architecture.

## Features

- **Modular Architecture:** Separation of concerns using individual modules for NLP, dialogue management, and data integration.
- **Simple NLP Intent Recognition:** Uses basic keyword-based matching to determine user intent.
- **Simulated Data Integration:** Provides a dummy train schedule endpoint for demonstration purposes.
- **RESTful API Endpoints:** Two main endpoints (`/chat` and `/train-schedule`) for interfacing with the chatbot.
- **Containerization:** Dockerfile provided for consistent deployment across environments.
- **Testing:** Unit tests implemented using pytest to validate API endpoints and functionality.

## Project Structure



## Getting Started

### Prerequisites

- Python 3.9 or later
- pip (Python package manager)
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>

Install the required Python packages:

If a requirements.txt exists, run:

pip install -r requirements.txt

Otherwise, manually install:
pip install flask pytest

Running Locally
To start the application locally, run:

python main.py

The Flask server will start on http://localhost:5000.

API Endpoints
Chat Endpoint: URL: POST http://localhost:5000/chat Request Body Example:

Chat Endpoint: URL: POST http://localhost:5000/chat Request Body Example:

json
{
  "message": "What is the train schedule for train 12345?"
}
Response Example:

json
{
  "response": "It looks like you're inquiring about a train schedule. Please provide the train number for exact details.",
  "intent": "train_schedule"
}
Train Schedule Endpoint: URL: GET http://localhost:5000/train-schedule?train_id=12345 Response Example:

json
{
  "train_id": "12345",
  "schedule": {
    "departure": "10:00 AM",
    "arrival": "04:00 PM",
    "duration": "6 hours",
    "stops": ["Station A", "Station B", "Station C"]
  }
}
Testing
The project includes unit tests using pytest. To run the tests, execute:

bash
pytest --maxfail=1 --disable-warnings -q
Docker Usage
Build the Docker image:

bash
docker build -t indian-railways-chatbot .
Run the Docker container:

bash
docker run -p 5000:5000 indian-railways-chatbot
The application will now be accessible on http://localhost:5000.

Contributing
Contributions are welcome! If you have any improvements, bug fixes, or additional features you'd like to propose, please open an issue or submit a pull request. We appreciate your efforts to help enhance this project.

License
This project is licensed under the MIT License.


---

This `README.md` file offers a comprehensive overview of the project, outlines clear instructions for setup, usage, and testing, and helps guide potential contributors through the structure and objectives of this PoC. 

If you're interested in exploring how to add advanced features like voice integration, multilingual support, or an upgraded NLP pipeline with transformer models, let's discuss further enhancements in subsequent updates!


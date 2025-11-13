# Notification System

This directory contains the implementation for a notification system.

## Notification System Design

A notification system is a crucial component of modern applications, responsible for delivering timely and relevant information to users across various channels. This system is designed to be scalable, reliable, and extensible, ensuring that users receive notifications promptly and accurately.

### Key Features

*   **Scalability**: The system is designed to handle a high volume of notifications, scaling horizontally to accommodate a growing number of users and notification types.
*   **Reliability**: Notifications are delivered with high reliability, with mechanisms for retries and error handling to ensure that messages are not lost.
*   **Extensibility**: The system is designed to be easily extensible, allowing for the addition of new notification channels (e.g., email, SMS, push notifications) and notification types with minimal effort.
*   **Real-time Delivery**: The system supports real-time notification delivery, ensuring that users receive time-sensitive information without delay.
*   **User Preferences**: Users can customize their notification preferences, choosing which types of notifications they want to receive and on which channels.

### Architecture

The notification system is built on a microservices architecture, with separate services for handling different aspects of the notification process, such as:

*   **Notification Service**: The core service responsible for receiving notification requests, processing them, and sending them to the appropriate channels.
*   **User Service**: Manages user information, including their notification preferences and contact details.
*   **Template Service**: Manages notification templates, allowing for easy customization of notification content.
*   **Channel Services**: Separate services for each notification channel (e.g., email service, SMS service, push notification service), responsible for sending notifications to the respective channels.

This modular architecture allows for independent scaling and development of each component, ensuring that the system remains robust and maintainable as it evolves.

## Project Structure and Components

This implementation uses a microservices architecture with a Redis-based event bus for communication between services.

*   `docker-compose.yml`: Defines the services for the system, including the API, notification worker, analytics worker, and a Redis instance.
*   `main.py`: A FastAPI application that exposes a `/register` endpoint. When a user registers, it publishes a `REGISTERED_USER` event to the `USER_CHANNEL` on the Redis event bus.
*   `event_bus.py`: A Python class that encapsulates the logic for publishing and subscribing to events using Redis.
*   `notification_worker.py`: A worker that subscribes to the `USER_CHANNEL`. When it receives a `REGISTERED_USER` event, it calls the `sent_email` function to simulate sending a welcome email.
*   `analytics_worker.py`: A worker that also subscribes to the `USER_CHANNEL`. When it receives a `REGISTERED_USER` event, it calls the `update_analytics` function to simulate updating a dashboard.
*   `notification_system.py`: An alternative implementation that uses an in-memory event bus. The main system uses the Redis-based one.

## How to Run

1.  **Prerequisites**: Make sure you have Docker and Docker Compose installed on your system.
2.  **Build and Run**: Open a terminal in the project's root directory and run the following command:
    ```bash
    docker-compose up --build
    ```
3.  **Register a User**: Once the services are running, you can register a new user by sending a POST request to the `/register` endpoint. You can use `curl` for this:
    ```bash
    curl -X POST "http://localhost:8000/register?email=test@example.com"
    ```
4.  **Observe the Logs**: You will see logs from the notification and analytics workers in the terminal, showing that they have received the event and performed their respective actions.
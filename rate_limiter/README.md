# FastAPI Rate Limiter Example

This project is a simple demonstration of a rate limiter implemented in a FastAPI application using Redis as a backend.

## Description

The application has two endpoints:

- `/publico`: A public endpoint with no rate limiting.
- `/protegido`: A protected endpoint that is limited to 5 requests per minute per IP address.

The rate limiting is implemented using the `slowapi` library, which provides a simple way to add rate limiting to FastAPI applications. The token bucket algorithm is used to limit the number of requests.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Redis](https://redis.io/)
- [Docker](https://www.docker.com/)
- [slowapi](https://slowapi.readthedocs.io/en/latest/)

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation and Running

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository/rate_limiter
    ```

2.  **Build and run the application using Docker Compose:**

    ```bash
    docker-compose up --build
    ```

    This will start the FastAPI application on `http://localhost:8000` and a Redis container.

## Testing

To test the rate limiter, you can use the provided `test_limiter.sh` script:

```bash
./test_limiter.sh
```

This script will send 7 requests to the `/protegido` endpoint. The first 5 requests should be successful, and the last 2 should be blocked by the rate limiter, returning a `429 Too Many Requests` error.

## Project Structure

```
rate_limiter/
├── docker-compose.yml  # Docker Compose configuration
├── Dockerfile          # Dockerfile for the FastAPI application
├── main.py             # FastAPI application code
├── requirements.txt    # Python dependencies
└── test_limiter.sh     # Script to test the rate limiter
```

# Script Directory

This directory contains utility scripts for the rate limiter project.

## `token_bucket_limiter.py`

This script implements the Token Bucket algorithm for rate limiting. It provides a mechanism to control the rate at which requests or operations are processed, preventing resource exhaustion and abuse.

### How it works

The `token_bucket_limiter.py` script implements a Token Bucket rate limiting algorithm.

**`TockenBucketLimiter` Class:**
*   **`__init__(self, capacity, fill_rate)`**: Initializes the bucket with a `capacity` (max tokens), `_tokens` (current tokens, starts at capacity), `fill_rate` (tokens per second), and `last_filled` timestamp.
*   **`_refill(self)`**: Calculates elapsed time since `last_filled`, adds `new_tokens` based on `fill_rate`, and caps `_tokens` at `capacity`. Updates `last_filled`.
*   **`allow_request(self) -> bool`**: First, it calls `_refill()` to update tokens. If `_tokens` is 1 or more, it consumes one token and returns `True` (request allowed). Otherwise, it returns `False` (request rejected).

**Example Usage:**
The script creates a limiter with 5 tokens capacity and a refill rate of 1 token/second. It then simulates two batches of 7 requests, demonstrating how requests are allowed until tokens are exhausted and then rejected until the bucket refills. A `time.sleep(1)` between batches shows the refill in action.

This script provides a fundamental example of how the Token Bucket algorithm controls request rates to prevent system overload.
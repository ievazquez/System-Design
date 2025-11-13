import time

class TockenBucketLimiter:
    def __init__(self, capacity:int, fill_rate:float):
        self.capacity    = float(capacity)
        self._tokens     = float(capacity)
        self.fill_rate   = fill_rate
        self.last_filled = time.monotonic()

    def _refill(self):
        now =time.monotonic()
        time_passed = now - self.last_filled
        #print(f"Time passed {time_passed}")
        new_tokens = time_passed * self.fill_rate
        #print(f"New tokens {new_tokens}")

        if new_tokens > 0:
            self._tokens = min(self.capacity, self._tokens + new_tokens)
            #print(f"Tokens {self._tokens}")
            self.last_filled = now


    def allow_request(self) ->bool:
        self._refill()

        if self._tokens >= 1:
            self._tokens -= 1
            return True

        return False



limiter = TockenBucketLimiter(capacity = 5, fill_rate = 1)

for i in range(7):
    if limiter.allow_request():
        print(f"Request {i+1}: Allowed ✅")
    else:
        print(f"Request { i + 1}: Rejected ❌ (Rate Limit) ")

time.sleep(1)

for i in range(7):
    if limiter.allow_request():
        print(f"Request {i+1}: Allowed ✅")
    else:
        print(f"Request { i + 1}: Rejected ❌ (Rate Limit) ")

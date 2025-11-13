from collections import defaultdict
import time

class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)
        print("Event (in-memory) Bus initialized...")

    def subscribe(self, event_type:str, callback_func : callable):
        self.listeners[event_type].append(callback_func)
        print(f"New subscriber {callback_func.__name__} for event '{event_type}'" )

    def publish(self, event_type:str, data:dict):
        #print(f"\n--- PUBLISHING EVENT: {event_type} ---")
        if not self.listeners[event_type]:
            print(f"No subscribers for {event_type}")
            return

        # Call each function registered for this event
        for func in self.listeners[event_type]:
            try:
                func(data)
            except:
                print(f"Error executing {func.__name__}: {e}")


def send_email(data:dict):
    email = data.get("email")
    print(f"[Worker Emal] Simulating email dispatch to {email}...")
    time.sleep(1)
    print(f"[Worker Emal] Email sent.")

def update_analytics(data:dict):
    email = data.get("email")
    print(f"[Worker Analytics] Updating Dashboard with {email}...")
    time.sleep(0.5)
    print(f"[Worker Analytics] Dashboard updated.")

def payment_notification(data:dict):
    print(f"[Worker Notification] Payment received for {data.get('amount')}.")

if __name__ == "__main__":
    event_bus = EventBus()

    # Register the subscribers
    event_bus.subscribe("REGISTERED_USER", send_email)
    event_bus.subscribe("REGISTERED_USER", update_analytics)
    event_bus.subscribe("RECEIVED_PAYMENT", payment_notification)

    # API Simulation (Publishing events)

    event_bus.publish("REGISTERED_USER", {"email": "juan@ejemplo.com", "id": 123})
    event_bus.publish("REGISTERED_USER", {"email": "ana@ejemplo.com", "id": 456})
    event_bus.publish("RECEIVED_PAYMENT", {"amount": 99.9, "txd_id": "xyz"})

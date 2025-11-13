import time
from event_bus import event_bus
import json

def sent_email(email:str):
    print(f"[Worker Emal] Simulating email dispatch to {email}...")
    time.sleep(1)
    print(f"[Worker Emal] Email sent.")



def main():
    event_bus.subscribe("USER_CHANNEL")

    for data in event_bus.listen():
        print(f"\n[Notificación] ¡Evento recibido! ")
        if data["event_type"] == "REGISTERED_USER":
            sent_email(data["email"])


if __name__ == "__main__":
    main()

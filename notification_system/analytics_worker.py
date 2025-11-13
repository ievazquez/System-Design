import time
from event_bus import event_bus
import json

def update_analytics(email:str):
    print(f"[Worker Analytics] Updating Dashboard with {email}...")
    time.sleep(0.5)
    print(f"[Worker Analytics] Dashboard updated.")

def main():
    # 1. Suscribirse al canal
    event_bus.subscribe("USER_CHANNEL")
    
    # 2. Escuchar usando el generador
    #    ¡Mucho más limpio!
    for data in event_bus.listen():
        print(f"\n[Analytics] ¡Evento recibido! ")
        if data["event_type"] == "REGISTERED_USER":
            update_analytics(data['email'])

if __name__ == "__main__":
    main()

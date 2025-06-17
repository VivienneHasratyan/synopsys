class SecurityCheck: # Handler
    def __init__(self, next_check=None):
        self.next_check = next_check

    def handle(self, passenger):
        if self.next_check:
            return self.next_check.handle(passenger)
        return "Passenger cleared all checks."

class IDCheck(SecurityCheck): # Concrete Handler 1
    def handle(self, passenger):
        if not passenger.get("has_valid_id", False):
            return "Denied: Invalid or missing ID."
        print("ID verified.")
        return super().handle(passenger)

class XRayScan(SecurityCheck): # Concrete Handler 2
    def handle(self, passenger):
        if passenger.get("suspicious_item", False):
            return "Alert: Suspicious item detected in X-ray."
        print("X-ray scan passed.")
        return super().handle(passenger)

class ManualBagCheck(SecurityCheck): # Concrete Handler 3
    def handle(self, passenger):
        if passenger.get("manual_bag_check", True):
            if passenger.get("hidden_item", False):
                return "Alert: Hidden item found in manual check!"
            print("Manual bag check passed.")
        else:
            print("Manual bag check skipped.")
        return super().handle(passenger)

class ExplosivesDetector(SecurityCheck): # Concrete Handler 4
    def handle(self, passenger):
        if passenger.get("explosive_trace", False):
            return "Alert: Explosive material detected!"
        print("No explosive traces found.")
        return super().handle(passenger)

security_chain = IDCheck( # Chain
    XRayScan(
        ManualBagCheck(
            ExplosivesDetector()
        )
    )
)

passenger_1 = {
    "has_valid_id": True,
    "suspicious_item": False,
    "manual_bag_check": False,
    "explosive_trace": False
}

passenger_2 = {
    "has_valid_id": False,
    "suspicious_item": True,
    "manual_bag_check": True,
    "hidden_item": True,
    "explosive_trace": True,
}

print("\nPassenger 1:")
print(security_chain.handle(passenger_1))

print("\nPassenger 2:")
print(security_chain.handle(passenger_2))

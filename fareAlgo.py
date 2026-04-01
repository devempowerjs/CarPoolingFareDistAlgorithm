from typing import List

class Passenger:
    def __init__(self, name: str, board: float, drop: float, waiting: float):
        self.name = name
        self.board = board
        self.drop = drop
        self.waiting = waiting
        self.fare = 0.0

passengers = [
    Passenger('A', 0, 10, 3),   # A: 0-10km, 3min waiting
    Passenger('B', 3, 8, 2),    # B: 3-8km, 2min waiting
    Passenger('C', 6, 8, 1)     # C: 6-8km, 1min waiting
]

FarePerKm = 25
WaitingChargePerMin = 1

events = set()
for p in passengers:
    events.add(p.board)
    events.add(p.drop)
events = sorted(events)

def calculate_fares(passengers: List[Passenger]):
    for i in range(len(events)-1):
        segStart = events[i]
        segEnd = events[i+1]
        segLength = segEnd - segStart
        present = [p for p in passengers if p.board <= segStart < p.drop]
        if not present:
            continue
        segFare = segLength * FarePerKm
        splitFare = segFare / len(present)
        for p in present:
            p.fare += splitFare
    for p in passengers:
        p.fare += p.waiting * WaitingChargePerMin

calculate_fares(passengers)
print("\n- Shared Fare Distribution")
for p in passengers:
    tripDistance = p.drop - p.board
    print(f"Passenger {p.name}: Total Fare = Rs {p.fare:.2f} | Trip Distance = {tripDistance} km | Waiting Time = {p.waiting} min")

def calculate_actual_fares(passengers, FarePerKm, WaitingChargePerMin):
    actualFares = {}
    for p in passengers:
        travelFare = (p.drop - p.board) * FarePerKm
        waitingFare = p.waiting * WaitingChargePerMin
        actualFares[p.name] = travelFare + waitingFare
    return actualFares

actualFares = calculate_actual_fares(passengers, FarePerKm, WaitingChargePerMin)

print("\n- Actual Fare Without Sharing")
for name in actualFares:
    p = next(x for x in passengers if x.name == name)
    tripDistance = p.drop - p.board
    print(f"Passenger {name}: Total Fare = Rs {actualFares[name]:.2f} | Trip Distance = {tripDistance} km | Waiting Time = {p.waiting} min")

passengers.clear()
del events
import gc
gc.collect()

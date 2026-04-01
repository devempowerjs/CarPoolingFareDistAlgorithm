# Car Pooling Fare Distribution Algorithm

## Overview
This project implements a robust and fair algorithm for distributing cab fares among multiple passengers sharing a ride (pooling), considering their individual boarding and dropping points, as well as waiting times. The algorithm ensures that each passenger pays only for the distance and waiting time they are actually involved in, making it ideal for ride-sharing applications and cab pooling services.

## Features
- **Dynamic Fare Splitting:** Calculates the fare for each segment of the journey and splits it among all passengers present in that segment.
- **Individual Waiting Charges:** Accurately assigns waiting charges to only those passengers who are present during waiting events (e.g., traffic, pickup/drop delays).
- **Detailed Trip Breakdown:** For each passenger, the output includes their total fare, trip distance, and waiting time, providing full transparency.
- **Comparison with Solo Fare:** Outputs both the shared fare and the fare each passenger would pay if they traveled alone, highlighting the savings from pooling.
- **Memory Efficiency:** Clears trip data after each calculation to ensure efficient memory usage, suitable for integration into real-time ride-sharing apps.

## How It Works
1. **Input:**
   - List of passengers, each with:
     - Name
     - Boarding point (in km)
     - Dropping point (in km)
     - Waiting time (in minutes)
   - Fare per kilometer
   - Waiting charge per minute
2. **Event Segmentation:**
   - The route is divided into segments based on all unique boarding and dropping points of all passengers.
3. **Fare Calculation:**
   - For each segment, the fare is split equally among all passengers present in that segment.
   - Each passenger's total fare is the sum of their segment fares plus their individual waiting charges.
   - The output for each passenger includes:
     - Total fare (shared)
     - Trip distance (drop - board)
     - Waiting time
4. **Solo Fare Calculation:**
   - For comparison, the fare each passenger would pay if they traveled alone is also calculated and shown with trip distance and waiting time.
   ```
      SoloFare = (drop − board) × FarePerKm + waitingTime × WaitingChargePerMin
   ```
5. **Memory Management:**
   - After fare calculation, all trip data is cleared and memory is released to ensure efficiency for repeated use.

## Example Output
```
- Shared Fare Distribution
Passenger A: Total Fare = Rs 182.17 | Trip Distance = 10 km | Waiting Time = 3 min
Passenger B: Total Fare = Rs 56.17 | Trip Distance = 5 km | Waiting Time = 2 min
Passenger C: Total Fare = Rs 17.67 | Trip Distance = 2 km | Waiting Time = 1 min

- Actual Fare Without Sharing
Passenger A: Total Fare = Rs 253.00 | Trip Distance = 10 km | Waiting Time = 3 min
Passenger B: Total Fare = Rs 127.00 | Trip Distance = 5 km | Waiting Time = 2 min
Passenger C: Total Fare = Rs 51.00 | Trip Distance = 2 km | Waiting Time = 1 min
```

## Calculation Steps & Example

The fare distribution algorithm uses a **segment-based equal split** for distance fare and **individual waiting charges**.

### Core Formulas

1. **Distance fare (per segment):**
   - Route is divided by all unique boarding/dropping points.
   - For each segment [start, end]:
     - SegmentLength = end − start (km)
     - SegmentFare = segmentLength × FarePerKm
     - PassengersPresent: board ≤ start < drop
     - Share/passenger = segment fare ÷ n_passengers_in_segment
   - Passenger's total distance fare = sum of shares across segments.

2. **Waiting charge:**
   - WaitingFare = waitingTime × WaitingChargePerMin (per passenger)

3. **Total shared fare:**
   - TotalFare = distance fare + waiting fare

### Example 

```bash
FarePerKm=25
WaitingChargePerMin=1
segments=(0-3 | 3-6 | 6-8 | 8-10)

# Segment breakdown
 | Segment | Length | Passengers | Segment fare | Share per pax |
 |---------|--------|------------|--------------|---------------|
 | 0-3     | 3      | A          | 75           | 75            |
 | 3-6     | 3      | A,B        | 75           | 37.5          |
 | 6-8     | 2      | A,B,C      | 50           | 16.67         |
 | 8-10    | 2      | A          | 50           | 50            |

# Fare calculation
A_distFare=(75+37.5+16.67+50)   # ≈179.17
A_waitFare=(3*1)                # 3
A_totalFare=(179.17+3)          # ≈182.17

B_distFare=(37.5+16.67)         # ≈54.17
B_waitFare=(2*1)                # 2
B_totalFare=(54.17+2)           # ≈56.17

C_distFare=16.67                # 16.67
C_waitFare=(1*1)                # 1
C_totalFare=(16.67+1)           # ≈17.67

# Solo fare 
A_solo=(10*25+3*1)              # 253
B_solo=(5*25+2*1)               # 127
C_solo=(2*25+1*1)               # 51
```

This ensures each passenger pays for the distance they actually shared and their own waiting time.

## Usage
1. Edit the `passengers` list in `fareAlgo.py` to match your scenario. Each passenger should have their name, boarding point, dropping point, and waiting time specified.
2. Set the `FarePerKm` and `WaitingChargePerMin` variables as needed for your fare structure.
3. Run the script:
   ```sh
   python fareAlgo.py
   ```
4. View the output for both shared and solo fares, including trip distance and waiting time for each passenger.

## Applications
- Ride-sharing and cab pooling apps
- Corporate or group travel cost splitting
- Any scenario requiring fair, transparent fare distribution among multiple travelers

## License
This project is licensed under the MIT License. Feel free to use, modify and distribute with attribution.
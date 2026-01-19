# Booking Confirmation Prediction Approach

## Objective

The objective of this feature is to predict the probability (in percentage) of a booking being successfully confirmed.
This prediction is based on historical and simulated booking data.
Since this is a design-focused assignment, a mock prediction logic is implemented instead of a real-time trained ML model.

---

## Prediction Approach

The prediction is based on the following factors:
- Seat occupancy percentage of the bus
- Day of travel (weekday or weekend)
- Meal selection during booking

The assumption is that:
- Higher seat occupancy increases confirmation probability
- Meal selection increases booking seriousness
- Weekend bookings have higher confirmation rates

---

## Mock Dataset

| Day        | Seat Occupancy (%) | Meal Selected | Confirmed |
|-----------|--------------------|---------------|-----------|
| Monday    | 65                 | Yes           | Yes       |
| Tuesday   | 40                 | No            | No        |
| Friday    | 85                 | Yes           | Yes       |
| Saturday  | 95                 | Yes           | Yes       |
| Wednesday | 50                 | No            | No        |

This dataset is used only to simulate booking behavior patterns.

---

## Model Used (Mock)

A simple rule-based scoring logic is used to simulate prediction:

- Seat occupancy > 80% → +40%
- Meal selected → +20%
- Weekend travel → +20%
- Base probability → 20%

Final probability is capped at 100%.

This approach represents how a logistic regression or classification model could be implemented in a real system.

---

## Sample Prediction Output

```json
{
  "booking_id": "BK1023",
  "confirmation_probability": "82%"
}

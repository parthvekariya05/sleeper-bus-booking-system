from flask import Flask, request, jsonify
from data import seats, stations, bookings
import uuid

app = Flask(__name__)

# -------------------- List Seats --------------------
@app.route("/api/seats", methods=["GET"])
def list_seats():
    return jsonify(seats)

# -------------------- Book Seat --------------------
@app.route("/api/book-seat", methods=["POST"])
def book_seat():
    data = request.json
    seat = data.get("seat_number")
    name = data.get("passenger_name")

    if seat not in seats:
        return jsonify({"error": "Invalid seat number"}), 400

    if seats[seat] == "booked":
        return jsonify({"error": "Seat already booked"}), 400

    booking_id = str(uuid.uuid4())[:8]
    seats[seat] = "booked"

    bookings[booking_id] = {
        "passenger_name": name,
        "seat_number": seat,
        "meal": None,
        "status": "confirmed"
    }

    return jsonify({
        "message": "Seat booked successfully",
        "booking_id": booking_id
    })

# -------------------- Book Meal --------------------
@app.route("/api/book-meal", methods=["POST"])
def book_meal():
    data = request.json
    booking_id = data.get("booking_id")
    meal = data.get("meal_type")

    if booking_id not in bookings:
        return jsonify({"error": "Booking not found"}), 404

    bookings[booking_id]["meal"] = meal
    return jsonify({"message": "Meal added successfully"})

# -------------------- Cancel Booking --------------------
@app.route("/api/cancel-booking", methods=["POST"])
def cancel_booking():
    data = request.json
    booking_id = data.get("booking_id")

    if booking_id not in bookings:
        return jsonify({"error": "Booking not found"}), 404

    seat = bookings[booking_id]["seat_number"]
    seats[seat] = "available"
    bookings[booking_id]["status"] = "cancelled"

    return jsonify({"message": "Booking cancelled successfully"})

# -------------------- Booking History --------------------
@app.route("/api/booking-history", methods=["GET"])
def booking_history():
    return jsonify(bookings)

# -------------------- Stations --------------------
@app.route("/api/stations", methods=["GET"])
def get_stations():
    return jsonify(stations)

if __name__ == "__main__":
    app.run(debug=True)

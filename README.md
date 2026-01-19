# Sleeper Bus Ticket Booking System  
Ahmedabad → Mumbai

## Project Overview

This is a web-based Sleeper Bus Ticket Booking System for the Ahmedabad to Mumbai route.  
Users can view available sleeper seats, select seats, book meals during checkout, and confirm or cancel bookings.  
The system assumes a single bus with possible intermediate stations between Ahmedabad and Mumbai.  
Payment gateway integration is not included.

---

## Core Features

1. Sleeper seat availability and selection  
2. Seat booking for Ahmedabad to Mumbai route  
3. Meal booking during checkout (Veg / Non-Veg / No Meal)  
4. Booking confirmation with unique booking ID  
5. Booking cancellation  
6. Booking history view  
7. Booking confirmation probability prediction (mock)

---

## Test Cases

### Functional Test Cases
- View available seats  
- Book a sleeper seat  
- Select meal during booking  
- Cancel a booking  

### Edge Cases
- Booking last available seat  
- Booking without meal selection  
- Cancelling non-existing booking  
- Invalid seat selection  

### UI/UX Validation
- Clear seat availability display  
- Simple meal selection  
- Proper error messages  

---

## API Endpoints

- **GET /api/seats** – List seat availability  
- **POST /api/book-seat** – Book a seat  
- **POST /api/book-meal** – Add meal to booking  
- **POST /api/cancel-booking** – Cancel booking  
- **GET /api/booking-history** – View booking history  
- **GET /api/stations** – List intermediate stations  

---

## UI/UX Prototype

UI screens are implemented using Flask HTML templates instead of Figma.  
The booking flow includes seat selection, meal selection, booking summary, and confirmation pages.

---

## Prediction Approach

A mock AI-based booking confirmation prediction feature is implemented.  
The prediction logic, mock dataset, and final probability output are documented in:

**PREDICTION_APPROACH.md**

---

## Technology Stack

- Backend: Python (Flask)  
- Database: In-memory mock data  
- UI/UX: Flask HTML templates  
- AI/ML: Mock rule-based logic  

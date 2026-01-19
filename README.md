# Sleeper Bus Ticket Booking System  
Ahmedabad → Mumbai


## Project Overview

I have designed a web-based Sleeper Bus Ticket Booking System for the Ahmedabad to Mumbai route.  
In this system, users can view available sleeper seats, select seats, book meals during the checkout process, and confirm or cancel their bookings.  
The system assumes only one bus operating on this route, with the possibility of multiple intermediate stations between Ahmedabad and Mumbai.  
Payment gateway integration is intentionally excluded, as the focus of this project is on system design, backend APIs, and analytical thinking.


## Core Features

1. I allow users to view sleeper seat availability in real time  
2. Users can book sleeper seats for the Ahmedabad to Mumbai route  
3. Meal booking (Veg / Non-Veg / No Meal) is integrated into the booking flow  
4. Each successful booking generates a unique booking ID  
5. Users can cancel an existing booking and release the seat  
6. Booking history can be viewed for reference  
7. A mock AI-based booking confirmation probability is generated


## Test Cases

### Functional Test Cases
- I verify that users can view available sleeper seats  
- I ensure users can successfully book a seat  
- I check that meal selection works correctly during booking  
- I confirm that bookings can be cancelled properly  

### Edge Cases
- Booking the last available seat  
- Booking without selecting any meal option  
- Cancelling a booking that does not exist  
- Selecting an invalid or already booked seat  

### UI/UX Validation
- Seat availability is clearly displayed to users  
- Meal options are simple and easy to understand  
- Appropriate error messages are shown for invalid actions  


## API Endpoints

### GET /api/seats  
Returns the list of sleeper seats along with their availability status.

### POST /api/book-seat  
Allows users to book a sleeper seat for the selected route.

### POST /api/book-meal  
Adds the selected meal preference to an existing booking.

### POST /api/cancel-booking  
Cancels a confirmed booking and makes the seat available again.

### GET /api/booking-history  
Returns the booking history details.

### GET /api/stations  
Returns the list of intermediate stations between Ahmedabad and Mumbai.


## UI/UX Prototype

Figma Design Link:  
(Will be added here – Public link)



## Prediction Approach

I have implemented a mock AI-based booking confirmation prediction feature.  
This feature estimates the probability (in percentage) of booking confirmation based on historical and simulated data.  
The detailed prediction logic, mock dataset, model approach, and final output are documented in:

**PREDICTION_APPROACH.md**

---

## Technology Stack

- Backend: Python (Flask) / Node.js (Express)  
- Database: In-memory data structures (mock data)  
- UI/UX Design: Figma  
- AI/ML: Mock rule-based or simple logistic regression approach  

---

## Notes

- The system considers only one bus for the entire route  
- Payment gateway integration is not part of this project  
- The main focus is on backend design, system flow, and analytical reasoning  

---

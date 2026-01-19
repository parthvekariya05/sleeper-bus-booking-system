# Sleeper Bus Ticket Booking System  
Ahmedabad → Mumbai

---

## Project Overview

This project is a web-based Sleeper Bus Ticket Booking System for the route Ahmedabad to Mumbai.  
The system allows users to select sleeper seats, book meals during checkout, and confirm or cancel bookings.  
The bus may have multiple intermediate stations between Ahmedabad and Mumbai, and only one bus is considered in the system.  
Payment gateway integration is not included as part of this project.

---

## Core Features

1. Sleeper seat selection and availability check  
2. Booking seats for Ahmedabad to Mumbai route  
3. Meal booking integration during checkout  
4. Booking confirmation with unique booking ID  
5. Booking cancellation functionality  
6. Viewing booking history  
7. Booking confirmation probability prediction (AI-based mock logic)

---

## Test Cases

### Functional Test Cases
- User can view available sleeper seats  
- User can book a seat successfully  
- User can select a meal during booking  
- User can cancel a booking  

### Edge Cases
- Booking the last available seat  
- Booking without selecting a meal  
- Cancelling a booking that does not exist  
- Selecting an invalid seat number  

### UI/UX Validation
- Seat availability is clearly visible  
- Meal options are easy to understand  
- Proper error messages are shown  

---

## API Endpoints

### GET /api/seats  
Returns the list of sleeper seats with their availability status.

### POST /api/book-seat  
Books a sleeper seat for the selected route.

### POST /api/book-meal  
Adds meal preference (Veg / Non-Veg / No Meal) to an existing booking.

### POST /api/cancel-booking  
Cancels a confirmed booking and frees the seat.

### GET /api/booking-history  
Returns booking history details.

### GET /api/stations  
Returns intermediate stations between Ahmedabad and Mumbai.

---

## UI/UX Prototype

Figma Design Link:  
(Will be added here – Public link)

---

## Prediction Approach

This system includes a mock AI-based booking confirmation prediction feature.  
The prediction logic, mock dataset, model approach, and final probability output are documented in the file:

**PREDICTION_APPROACH.md**

---

## Technology Stack

- Backend: Python (Flask) / Node.js (Express)  
- Database: In-memory / Mock data  
- UI Design: Figma  
- AI/ML: Mock rule-based or logistic regression approach  

---

## Notes

- Only one bus is considered in the system  
- Payment gateway integration is not included  
- This project focuses on system design, backend APIs, and analytical thinking  

---

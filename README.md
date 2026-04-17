# Full Stack Graphical Calculator

A modern full-stack calculator web application built using React and FastAPI. Supports scientific operations, nested expressions, and operator precedence using the Shunting Yard Algorithm.

## Features

* Basic arithmetic (+, -, *, /, %)
* Power operations (^)
* Parentheses support
* Nested expression solving
* Trigonometric functions:
  * sin()
  * cos()
  * tan()
* sqrt()
* log()
* Fast backend API using FastAPI
* Clean graphical interface using React
* Stack-based expression parser

## Tech Stack

* Frontend: React
* Backend: FastAPI
* Language: Python, JavaScript
* Algorithm: Stack + Shunting Yard

## Project Structure

frontend/ → React UI
backend/ → FastAPI backend + parser

## Run Locally

### Backend

cd backend
pip install fastapi uvicorn
uvicorn main:app --reload

### Frontend

cd frontend
npm install
npm start

## Future Improvements

* Calculation history
* Graph plotting
* Dark/light theme
* User login
* Cloud deployment

## Author

Arjun Hirani

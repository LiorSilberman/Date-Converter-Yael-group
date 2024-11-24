# Date-Converter-Yael-group

## Date Converter Web App

This project is a web application that converts Gregorian dates to Hebrew dates. It utilizes a Flask backend to interact with the Hebcal API and a React frontend for user interactions.

## Features

- Convert individual Gregorian dates to Hebrew dates.
- Responsive and user-friendly interface.

## Installation

To install Date Converter Web App, follow these steps:

### Backend Setup

**1. Clone the repository:**
```bash
git clone https://github.com/LiorSilberman/Date-Converter-Yael-group.git
cd Date-Converter-Yael-group/backend
```

**2. Create a virtual environment and activate it:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**3. Install the required packages:**
```bash
pip install -r requirements.txt
```

**4. Start the Flask server:**
```bash
python3 app.py
```

### Frontend Setup

**1. Navigate to the frontend directory:**
```bash
cd ../date-converter-frontend
```

**2. Install the necessary npm packages:**
```bash
npm install
```

**3. Start the React application:**
```bash
npm start
```

## Usage

Once both the backend and frontend are running, open your web browser and go to [http://localhost:3000](http://localhost:3000). Use the interface to select a date, then click the "Convert" button to see the Hebrew date.

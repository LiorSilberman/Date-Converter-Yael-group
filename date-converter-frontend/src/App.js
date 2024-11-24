import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import "react-datepicker/dist/react-datepicker.css";
import './App.css';


/**
 * App component that provides a form for converting Gregorian dates to Hebrew dates.
 */  
function App() {
  const [startDate, setStartDate] = useState(new Date());
  const [hebrewDate, setHebrewDate] = useState('');

  /**
   * Handles the change of the date picker.
   * @param {Date} date - The new date selected in the date picker.
   */
  const handleChange = date => {
    setStartDate(date);
  };

  /**
   * Handles the submission of the conversion form.
   * Asynchronously fetches the Hebrew date corresponding to the selected Gregorian date.
   * @param {Event} e - The form submission event.
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
      if (!startDate) {
        console.error('No date selected');
        return;
      }
    const year = startDate.getFullYear();
    const month = startDate.getMonth() + 1;
    const day = startDate.getDate();
  
    try {
      const response = await fetch(`http://localhost:5000/convert?year=${year}&month=${month}&day=${day}`);
      const data = await response.json();
      setHebrewDate(data.hebrew);
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
  return (
    <div className="App">
      <header className="App-header">
        <h1>Date Converter</h1>
        <form onSubmit={handleSubmit}>
          <DatePicker
            selected={startDate}
            onChange={handleChange}
            dateFormat="dd/MM/yyyy"
            showYearDropdown
            dropdownMode="select"
          />
          <button type="submit">Convert</button>
        </form>
        {hebrewDate && <p>{hebrewDate}</p>}
      </header>
    </div>
  );
}

export default App;

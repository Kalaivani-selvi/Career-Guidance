 // Get the current date and time
        const currentDate = new Date();
        const currentDateString = currentDate.toISOString().slice(0, 10); 
        const currentTimeString = currentDate.toTimeString().slice(0, 5);
      
        // Set the default values to the input fields
        document.getElementById("date").value = currentDateString;
        document.getElementById("time").value = currentTimeString;
      
fetch("http://127.0.0.1:5000/api/demand_forecast")
  .then(res => res.json())
  .then(data => {
    const ctx = document.getElementById("forecastChart").getContext("2d");
    new Chart(ctx, {
      type: "line",
      data: {
        labels: data.hours_ahead.map(h => `+${h}h`),
        datasets: [{
          label: "Predicted Demand",
          data: data.predicted_demand,
          borderWidth: 3,
          fill: true,
          tension: 0.3
        }]
      },
      options: {
        plugins: { legend: { labels: { color: "#fff" } } },
        scales: {
          x: { ticks: { color: "#fff" } },
          y: { ticks: { color: "#fff" } }
        }
      }
    });
  })
  .catch(err => console.error("Error loading forecast:", err));

async function getETA(busId, source, destination) {
  try {
    const res = await fetch("http://127.0.0.1:5000/api/eta", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ bus_id: busId, source, destination })
    });
    const data = await res.json();
    alert(`Estimated Arrival Time: ${data.eta_minutes} minutes`);
  } catch (error) {
    console.error("Error fetching ETA:", error);
  }
}

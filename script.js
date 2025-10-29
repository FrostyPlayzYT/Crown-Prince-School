const form = document.getElementById("greetForm");
const greeting = document.getElementById("greeting");

form.addEventListener("submit", async (event) => {
  event.preventDefault(); // Stop form from reloading the page

  const name = document.getElementById("nameInput").value;

  // Send data to Flask
  const response = await fetch("/greet", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ name: name })
  });

  const data = await response.json();
  greeting.innerText = data.message;
});

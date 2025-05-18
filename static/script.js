document.getElementById("pizzaForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const type = document.getElementById("pizzaType").value;
  const size = document.getElementById("pizzaSize").value;
  const toppings = Array.from(document.querySelectorAll("input[type='checkbox']:checked"))
    .map(el => el.value);

  let basePrice = { margherita: 200, pepperoni: 250, hawaiian: 230 }[type];
  let sizeAdd = { small: 0, medium: 50, large: 100 }[size];
  let toppingAdd = toppings.length * 30;

  const total = basePrice + sizeAdd + toppingAdd;

  fetch("/api/order", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      pizzaType: type,
      pizzaSize: size,
      toppings: toppings,
      total: total
    })
  })
  .then(res => res.json())
  .then(data => alert(data.message));
});
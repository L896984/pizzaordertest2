PizzaOrder/
document.getElementById("pizzaForm").addEventListener("change", calculateTotal);
document.getElementById("pizzaForm").addEventListener("submit", function(e) {
  e.preventDefault();
  alert("感謝您的訂購！");
});

function calculateTotal() {
  const pizzaPrices = {
    margherita: 200,
    pepperoni: 250,
    hawaiian: 230
  };

  const sizePrices = {
    small: 0,
    medium: 50,
    large: 100
  };

  const pizzaType = document.getElementById("pizzaType").value;
  const pizzaSize = document.getElementById("pizzaSize").value;
  const toppings = document.querySelectorAll('input[name="topping"]:checked');

  let total = pizzaPrices[pizzaType] + sizePrices[pizzaSize];
  total += toppings.length * 30;

  document.getElementById("total").textContent = "總金額：$" + total;
}
document.getElementById("pizzaForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const pizzaType = document.getElementById("pizzaType").value;
  const pizzaSize = document.getElementById("pizzaSize").value;
  const toppings = Array.from(document.querySelectorAll('input[name="topping"]:checked'))
                        .map(t => t.value);
  const total = calculateTotal();  // 修改成 return 數字

  fetch("/order", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      pizzaType,
      pizzaSize,
      toppings,
      total
    })
  })
  .then(res => res.json())
  .then(data => {
    alert(data.message || "訂單送出失敗！");
  })
  .catch(err => {
    console.error("Error:", err);
    alert("送出錯誤！");
  });
});

function calculateTotal() {
  const pizzaPrices = {
    margherita: 200,
    pepperoni: 250,
    hawaiian: 230
  };

  const sizePrices = {
    small: 0,
    medium: 50,
    large: 100
  };

  const pizzaType = document.getElementById("pizzaType").value;
  const pizzaSize = document.getElementById("pizzaSize").value;
  const toppings = document.querySelectorAll('input[name="topping"]:checked');

  let total = pizzaPrices[pizzaType] + sizePrices[pizzaSize];
  total += toppings.length * 30;

  document.getElementById("total").textContent = "總金額：$" + total;
  return total;
}

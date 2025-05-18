
 document.getElementById("pizzaForm").addEventListener("change", calculateTotal);
 document.getElementById("pizzaForm").addEventListener("submit", function(e) {
   calculateTotal();
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

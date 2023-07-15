document.getElementById("subscription-form").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Retrieve input values
  var email = document.getElementById("email").value;
  var cardNumber = document.getElementById("card-number").value;
  var expiryMonth = document.getElementById("expiry-month").value;
  var expiryYear = document.getElementById("expiry-year").value;
  var cvv = document.getElementById("cvv").value;
  var amount = document.getElementById("amount").value;

  // Create subscription object
  var subscription = {
    email: email,
    cardNumber: cardNumber,
    expiryMonth: expiryMonth,
    expiryYear: expiryYear,
    cvv: cvv,
    amount: amount
  };

  // Make API call to create subscription
  var seerbit = require("seerbit");

  seerbit.create_subscription(subscription)
    .then(function(response) {
      if (response.status === "SUCCESS") {
        console.log("Subscription created successfully");
        // Handle success response
        alert("Subscription created successfully!");
      } else {
        console.log("Error creating subscription:", response.message);
        // Handle error response
      }
    })
    .catch(function(error) {
      console.log("Error creating subscription:", error);
      // Handle error case
    });
});

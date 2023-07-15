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

  // Make AJAX request to server-side API endpoint
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/create-subscription", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        if (response.status === "SUCCESS") {
          console.log("Subscription created successfully");
          alert("Subscription created successfully!");
        } else {
          console.log("Error creating subscription:", response.message);
          // Handle error response
        }
      } else {
        console.log("Error creating subscription:", xhr.status);
        // Handle error status
      }
    }
  };
  xhr.send(JSON.stringify(subscription));
});

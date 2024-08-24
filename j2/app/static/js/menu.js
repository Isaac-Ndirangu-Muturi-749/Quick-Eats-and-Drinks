
/* Initialize order total. */
document.getElementById("orderTotal").innerHTML = "0.00";
var itemTotals = new Array({{ products|length }});

for (var i = 0; i < itemTotals.length; i++) {
    itemTotals[i] = 0.00;
}

/* Function to calculate order total */
function calculateOrderTotal() {
    var orderTotal = 0.00;
    for (var i = 0; i < itemTotals.length; i++) {
        orderTotal += itemTotals[i];
    }
    return orderTotal.toFixed(2);
}

/* Function to reset form */
function resetForm() {
    document.getElementById("orderForm").reset();
    document.getElementById("orderTotal").innerHTML = "0.00";
    for (var i = 0; i < itemTotals.length; i++) {
        itemTotals[i] = 0.00;
    }
}

/* Function to update order total when quantities change */
function updateTotal(itemNo, quantity, price) {
    var amount = quantity * price;
    itemTotals[itemNo] = amount;
    document.getElementById("orderTotal").innerHTML = calculateOrderTotal();
}

/* Function to validate the order amount */
function validateOrder() {
    if (calculateOrderTotal() <= 0.00) {
        alert('Please select at least one item to buy.');
        return false;
    }
}

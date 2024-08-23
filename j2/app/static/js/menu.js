document.getElementById("orderTotal").innerHTML = "0.00";

var itemTotals = [];

function calculateOrderTotal() {
    var orderTotal = 0.00;
    for (var i = 0; i < itemTotals.length; i++) {
        orderTotal += itemTotals[i];
    }
    return orderTotal;
}

function resetForm() {
    document.getElementById("orderForm").reset();
    document.getElementById("orderTotal").innerHTML = "0.00";
    itemTotals = [];
}

function updateTotal(itemNo, quantity, price) {
    var amount = quantity * price;
    itemTotals[itemNo] = amount;
    var totalAmount = calculateOrderTotal().toFixed(2);
    document.getElementById("orderTotal").innerHTML = totalAmount;
}

function validateOrder() {
    if (calculateOrderTotal() <= 0.0) {
        alert('Please select at least one item to buy.');
        return false;
    }
}

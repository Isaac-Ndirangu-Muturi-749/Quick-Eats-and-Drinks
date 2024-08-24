
// Ensure all initial values are 0.00
for (var i = 0; i < itemTotals.length; i++) {
    itemTotals[i] = 0.00;
}

// Function to calculate the order total
function calculateOrderTotal() {
    var orderTotal = 0.00;
    for (var i = 0; i < itemTotals.length; i++) {
        orderTotal += parseFloat(itemTotals[i]);
    }
    return orderTotal.toFixed(2);
}

// Function to update the total for a specific item
function updateTotal(itemNo, quantity, price) {
    var quantityNum = parseFloat(quantity) || 0;
    var priceNum = parseFloat(price) || 0;
    var amount = quantityNum * priceNum;

    itemTotals[itemNo] = amount;  // Update specific item total

    // Update individual item total on the page
    var itemTotalElement = document.getElementById("itemTotal" + itemNo);
    if (itemTotalElement) {
        itemTotalElement.innerHTML = amount.toFixed(2);
    }

    // Update the order total
    document.getElementById("orderTotal").innerHTML = calculateOrderTotal();
}

// Function to reset the form and item totals
function resetForm() {
    document.getElementById("orderForm").reset();
    document.getElementById("orderTotal").innerHTML = "0.00";
    for (var i = 0; i < itemTotals.length; i++) {
        itemTotals[i] = 0.00;
        var itemTotalElement = document.getElementById("itemTotal" + i);
        if (itemTotalElement) {
            itemTotalElement.innerHTML = "0.00";  // Reset item total display
        }
    }
}

// Function to validate the order before submission
function validateOrder() {
    if (calculateOrderTotal() <= 0.00) {
        alert('Please select at least one item to buy.');
        return false;
    }
    return true;
}

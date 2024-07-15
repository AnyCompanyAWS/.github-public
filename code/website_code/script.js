// Define an array to store the products in the cart
let cart = [];

// Function to add a product to the cart
function addToCart(productId, productName, productPrice) {
    // Check if the product is already in the cart
    let existingItem = cart.find(item => item.id === productId);

    if (existingItem) {
        // If the product is already in the cart, increase its quantity
        existingItem.quantity++;
    } else {
        // Otherwise, add the product to the cart with quantity 1
        cart.push({
            id: productId,
            name: productName,
            price: productPrice,
            quantity: 1
        });
    }

    // Update the cart display
    displayCart();
}

// Function to display the cart
function displayCart() {
    // Select the element where cart items will be displayed
    let cartDisplay = document.getElementById('cart-display');
    // Clear previous content
    cartDisplay.innerHTML = '';

    // Loop through each item in the cart and display it
    cart.forEach(item => {
        let itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');
        itemElement.innerHTML = `
            <span>${item.name}</span>
            <span>Quantity: ${item.quantity}</span>
            <span>Price: $${(item.price * item.quantity).toFixed(2)}</span>
        `;
        cartDisplay.appendChild(itemElement);
    });
}

// Example: Event listener for "Add to Cart" button
document.addEventListener('DOMContentLoaded', function() {
    // Example button element (replace with your actual HTML structure)
    let addToCartButtons = document.querySelectorAll('.btn-add-to-cart');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();

            // Example: Fetch product details from HTML attributes or data attributes
            let productId = this.getAttribute('data-id');
            let productName = this.getAttribute('data-name');
            let productPrice = parseFloat(this.getAttribute('data-price'));

            // Add the product to the cart
            addToCart(productId, productName, productPrice);
        });
    });
});

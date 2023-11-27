document.addEventListener('DOMContentLoaded', function () {
    const cartBtns = document.querySelectorAll('.cart-btn');
    const closeCartBtn = document.getElementById('close-cart-btn');
    const checkoutBtn = document.getElementById('checkout-btn');
    const clearCartBtn = document.getElementById('clear-cart-btn');
    const cartOverlay = document.getElementById('cart');
    const cartItemsList = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');

    let cart = [];

    function updateCart() {
        cartItemsList.innerHTML = '';
        let total = 0;

        cart.forEach((item, index) => {
            const listItem = document.createElement('li');
            listItem.textContent = `${item.name} - Rs. ${item.price}`;
            
            // Create a remove button for each item
            const removeBtn = document.createElement('button');
            removeBtn.textContent = 'Remove';
            removeBtn.classList.add('remove-btn');
            removeBtn.addEventListener('click', function () {
                removeFromCart(index);
            });

            listItem.appendChild(removeBtn);
            cartItemsList.appendChild(listItem);
            total += item.price;
        });

        cartTotal.textContent = `Total: Rs. ${total}`;
    }

    function addToCart(name, price) {
        cart.push({ name, price });
        updateCart();
    }

    function removeFromCart(index) {
        cart.splice(index, 1);
        updateCart();
    }

    cartBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            const productName = this.parentElement.querySelector('strong').textContent;
            const productPrice = parseInt(this.parentElement.querySelector('.price').textContent.replace('Rs. ', ''));
            addToCart(productName, productPrice);
            cartOverlay.style.display = 'block'; // Show the cart overlay after adding to the cart
        });
    });

    closeCartBtn.addEventListener('click', function () {
        cartOverlay.style.display = 'none';
    });


    checkoutBtn.addEventListener('click', function () {
        if (cart.length === 0) {
            alert('Your cart is empty. Add items before checkout.');
        } else {
            window.location.href = "cheackout";
            const confirmation = confirm('Proceed to checkout?');
            if (confirmation) {
                alert('Thank you for your purchase!');
                // Reset the cart and update the display
                cart = [];
                updateCart();
                cartOverlay.style.display = 'none';
            }
        }
    });
});
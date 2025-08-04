// Global variables
let menuData = null;
let cart = [];
let cartTotal = 0;

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    loadMenu();
    updateCartDisplay();
});

// Load menu data from API
async function loadMenu() {
    try {
        const response = await fetch('/api/menu');
        menuData = await response.json();
        renderPizzas();
        renderToppings();
    } catch (error) {
        console.error('Error loading menu:', error);
        showError('Failed to load menu. Please refresh the page.');
    }
}

// Render pizza cards
function renderPizzas() {
    const pizzaGrid = document.getElementById('pizzaGrid');
    pizzaGrid.innerHTML = '';
    
    menuData.pizzas.forEach(pizza => {
        const pizzaCard = document.createElement('div');
        pizzaCard.className = 'pizza-card';
        pizzaCard.innerHTML = `
            <div class="pizza-header">
                <div>
                    <h4 class="pizza-name">${pizza.name}</h4>
                    <p class="pizza-description">${pizza.description}</p>
                </div>
                <div class="pizza-price">$${pizza.base_price}</div>
            </div>
            <div class="pizza-options">
                <div class="size-options">
                    <button class="size-btn active" data-size="small" onclick="selectSize(${pizza.id}, 'small', this)">
                        Small ($${pizza.base_price})
                    </button>
                    <button class="size-btn" data-size="big" onclick="selectSize(${pizza.id}, 'big', this)">
                        Big ($${pizza.base_price + 10})
                    </button>
                </div>
                <div class="quantity-controls">
                    <button class="quantity-btn" onclick="changeQuantity(${pizza.id}, -1)">-</button>
                    <span class="quantity-display" id="qty-${pizza.id}">1</span>
                    <button class="quantity-btn" onclick="changeQuantity(${pizza.id}, 1)">+</button>
                </div>
                <button class="add-to-cart" onclick="addPizzaToCart(${pizza.id})">
                    <i class="fas fa-plus"></i> Add to Cart
                </button>
            </div>
        `;
        pizzaGrid.appendChild(pizzaCard);
    });
}

// Render topping cards
function renderToppings() {
    const toppingsGrid = document.getElementById('toppingsGrid');
    toppingsGrid.innerHTML = '';
    
    menuData.toppings.forEach(topping => {
        const toppingCard = document.createElement('div');
        toppingCard.className = 'topping-card';
        toppingCard.innerHTML = `
            <div class="topping-header">
                <span class="topping-name">${topping.name}</span>
                <span class="topping-price">$${topping.price}</span>
            </div>
            <div class="quantity-controls">
                <button class="quantity-btn" onclick="changeToppingQuantity(${topping.id}, -1)">-</button>
                <span class="quantity-display" id="topping-qty-${topping.id}">0</span>
                <button class="quantity-btn" onclick="changeToppingQuantity(${topping.id}, 1)">+</button>
            </div>
            <button class="add-to-cart" onclick="addToppingToCart(${topping.id})">
                <i class="fas fa-plus"></i> Add to Cart
            </button>
        `;
        toppingsGrid.appendChild(toppingCard);
    });
}

// Select pizza size
function selectSize(pizzaId, size, button) {
    // Remove active class from all size buttons in this pizza card
    const pizzaCard = button.closest('.pizza-card');
    const sizeButtons = pizzaCard.querySelectorAll('.size-btn');
    sizeButtons.forEach(btn => btn.classList.remove('active'));
    
    // Add active class to selected button
    button.classList.add('active');
    
    // Store selected size
    button.closest('.pizza-card').setAttribute('data-selected-size', size);
}

// Change pizza quantity
function changeQuantity(pizzaId, change) {
    const qtyElement = document.getElementById(`qty-${pizzaId}`);
    let currentQty = parseInt(qtyElement.textContent);
    const newQty = Math.max(1, currentQty + change);
    qtyElement.textContent = newQty;
}

// Change topping quantity
function changeToppingQuantity(toppingId, change) {
    const qtyElement = document.getElementById(`topping-qty-${toppingId}`);
    let currentQty = parseInt(qtyElement.textContent);
    const newQty = Math.max(0, currentQty + change);
    qtyElement.textContent = newQty;
}

// Add pizza to cart
function addPizzaToCart(pizzaId) {
    const pizza = menuData.pizzas.find(p => p.id === pizzaId);
    const qtyElement = document.getElementById(`qty-${pizzaId}`);
    const quantity = parseInt(qtyElement.textContent);
    
    // Get selected size
    const pizzaCard = qtyElement.closest('.pizza-card');
    const selectedSize = pizzaCard.getAttribute('data-selected-size') || 'small';
    
    // Calculate price
    const sizeExtra = selectedSize === 'big' ? 10 : 0;
    const totalPrice = (pizza.base_price + sizeExtra) * quantity;
    
    // Add to cart
    const cartItem = {
        type: 'pizza',
        pizza_id: pizzaId,
        name: pizza.name,
        size: selectedSize,
        quantity: quantity,
        unit_price: pizza.base_price + sizeExtra,
        total_price: totalPrice
    };
    
    cart.push(cartItem);
    updateCartDisplay();
    showSuccess(`${quantity}x ${pizza.name} (${selectedSize}) added to cart!`);
    
    // Reset quantity to 1
    qtyElement.textContent = '1';
}

// Add topping to cart
function addToppingToCart(toppingId) {
    const topping = menuData.toppings.find(t => t.id === toppingId);
    const qtyElement = document.getElementById(`topping-qty-${toppingId}`);
    const quantity = parseInt(qtyElement.textContent);
    
    if (quantity === 0) {
        showError('Please select a quantity greater than 0');
        return;
    }
    
    // Calculate price
    const totalPrice = topping.price * quantity;
    
    // Add to cart
    const cartItem = {
        type: 'topping',
        topping_id: toppingId,
        name: topping.name,
        quantity: quantity,
        unit_price: topping.price,
        total_price: totalPrice
    };
    
    cart.push(cartItem);
    updateCartDisplay();
    showSuccess(`${quantity}x ${topping.name} added to cart!`);
    
    // Reset quantity to 0
    qtyElement.textContent = '0';
}

// Update cart display
function updateCartDisplay() {
    const cartCount = document.getElementById('cartCount');
    const cartItems = document.getElementById('cartItems');
    const cartTotal = document.getElementById('cartTotal');
    
    // Calculate totals
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    const totalPrice = cart.reduce((sum, item) => sum + item.total_price, 0);
    
    // Update cart count
    cartCount.textContent = totalItems;
    
    // Update cart items
    if (cart.length === 0) {
        cartItems.innerHTML = '<p class="empty-cart">Your cart is empty</p>';
    } else {
        cartItems.innerHTML = cart.map((item, index) => `
            <div class="cart-item">
                <div class="cart-item-info">
                    <h4>${item.name}</h4>
                    <div class="cart-item-details">
                        ${item.type === 'pizza' ? `Size: ${item.size}, ` : ''}Qty: ${item.quantity}
                    </div>
                </div>
                <div class="cart-item-price">
                    $${item.total_price}
                    <button onclick="removeFromCart(${index})" style="margin-left: 10px; background: #e74c3c; color: white; border: none; border-radius: 3px; padding: 2px 6px; cursor: pointer;">×</button>
                </div>
            </div>
        `).join('');
    }
    
    // Update total
    cartTotal.textContent = totalPrice;
}

// Remove item from cart
function removeFromCart(index) {
    cart.splice(index, 1);
    updateCartDisplay();
}

// Toggle cart sidebar
function toggleCart() {
    const cartSidebar = document.getElementById('cartSidebar');
    const cartOverlay = document.getElementById('cartOverlay');
    
    cartSidebar.classList.toggle('open');
    cartOverlay.classList.toggle('active');
}

// Place order
async function placeOrder() {
    const customerName = document.getElementById('customerName').value.trim();
    
    if (!customerName) {
        showError('Please enter your name');
        return;
    }
    
    if (cart.length === 0) {
        showError('Your cart is empty');
        return;
    }
    
    try {
        const orderData = {
            customer_name: customerName,
            items: cart
        };
        
        const response = await fetch('/api/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(orderData)
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Clear cart
            cart = [];
            updateCartDisplay();
            
            // Close cart if open
            const cartSidebar = document.getElementById('cartSidebar');
            const cartOverlay = document.getElementById('cartOverlay');
            cartSidebar.classList.remove('open');
            cartOverlay.classList.remove('active');
            
            // Show success message
            showOrderSuccess(`Order #${result.order_id} placed successfully! Total: $${result.total}`);
            
            // Clear customer name
            document.getElementById('customerName').value = '';
        } else {
            showError(result.error || 'Failed to place order');
        }
    } catch (error) {
        console.error('Error placing order:', error);
        showError('Failed to place order. Please try again.');
    }
}

// View all orders
async function viewOrders() {
    try {
        const response = await fetch('/api/orders');
        const orders = await response.json();
        
        const ordersTable = document.getElementById('ordersTable');
        
        if (orders.length === 0) {
            ordersTable.innerHTML = '<p>No orders found.</p>';
        } else {
            ordersTable.innerHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>Customer</th>
                            <th>Total Qty</th>
                            <th>Marinara</th>
                            <th>Margherita</th>
                            <th>Salami</th>
                            <th>Toppings</th>
                            <th>Total $</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${orders.map(order => `
                            <tr>
                                <td>${order[0]}</td>
                                <td>${order[1]}</td>
                                <td>${order[2]} ${order[3]}</td>
                                <td>${order[4]} ${order[5]}</td>
                                <td>${order[6]} ${order[7]}</td>
                                <td>${order[8]}</td>
                                <td>$${order[9]}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            `;
        }
        
        // Show modal
        document.getElementById('ordersModal').classList.add('active');
    } catch (error) {
        console.error('Error loading orders:', error);
        showError('Failed to load orders');
    }
}

// Close orders modal
function closeOrdersModal() {
    document.getElementById('ordersModal').classList.remove('active');
}

// Show success message
function showSuccess(message) {
    // Create a temporary success notification
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: #00b894;
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        z-index: 2000;
        animation: slideIn 0.3s ease;
    `;
    notification.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Show order success modal
function showOrderSuccess(message) {
    document.getElementById('successMessage').textContent = message;
    document.getElementById('successModal').classList.add('active');
}

// Close success modal
function closeSuccessModal() {
    document.getElementById('successModal').classList.remove('active');
}

// Show error message
function showError(message) {
    // Create a temporary error notification
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: #e74c3c;
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        z-index: 2000;
        animation: slideIn 0.3s ease;
    `;
    notification.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

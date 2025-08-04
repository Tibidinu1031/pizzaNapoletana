from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Pizza data structure
PIZZAS = [
    {"id": 1, "name": "Marinara", "base_price": 10, "description": "Classic tomato sauce, garlic, oregano, and olive oil"},
    {"id": 2, "name": "Margherita", "base_price": 12, "description": "Tomato sauce, mozzarella, fresh basil, and olive oil"},
    {"id": 3, "name": "Salami", "base_price": 14, "description": "Tomato sauce, mozzarella, and premium salami"}
]

TOPPINGS = [
    {"id": 1, "name": "Extra Mozzarella", "price": 5},
    {"id": 2, "name": "Extra Salami", "price": 6},
    {"id": 3, "name": "Extra Prosciutto", "price": 7}
]

SIZE_MULTIPLIER = {"small": 0, "big": 10}

def load_orders():
    """Load orders from file"""
    try:
        with open("pizza.orders", "r") as f:
            return eval(f.read())
    except:
        return []

def save_orders(orders):
    """Save orders to file with backup"""
    # Create backup if file exists
    if os.path.exists("pizza.orders"):
        try:
            os.makedirs("bah", exist_ok=True)
            backup_file = f"bah/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            os.system(f"copy pizza.orders {backup_file}")
        except:
            pass
    
    # Save orders
    with open("pizza.orders", "w") as f:
        f.write(str(orders))

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/menu')
def get_menu():
    """Get menu data"""
    return jsonify({
        'pizzas': PIZZAS,
        'toppings': TOPPINGS,
        'sizes': [
            {'name': 'small', 'label': 'Small', 'extra_cost': 0},
            {'name': 'big', 'label': 'Big', 'extra_cost': 10}
        ]
    })

@app.route('/api/orders', methods=['GET'])
def get_orders():
    """Get all orders"""
    orders = load_orders()
    return jsonify(orders)

@app.route('/api/orders', methods=['POST'])
def place_order():
    """Place a new order"""
    try:
        data = request.json
        
        # Calculate order totals
        total_quantity = 0
        total_price = 0
        pizza_details = {"marinara": {"qty": 0, "size": ""}, 
                        "margherita": {"qty": 0, "size": ""}, 
                        "salami": {"qty": 0, "size": ""}}
        toppings_qty = 0
        
        # Process pizzas
        for item in data.get('items', []):
            if item['type'] == 'pizza':
                pizza = next(p for p in PIZZAS if p['id'] == item['pizza_id'])
                quantity = item['quantity']
                size = item['size']
                
                item_price = (pizza['base_price'] + SIZE_MULTIPLIER[size]) * quantity
                total_price += item_price
                total_quantity += quantity
                
                # Update pizza details for legacy format
                pizza_name = pizza['name'].lower()
                pizza_details[pizza_name]['qty'] = quantity
                pizza_details[pizza_name]['size'] = size
            
            elif item['type'] == 'topping':
                topping = next(t for t in TOPPINGS if t['id'] == item['topping_id'])
                quantity = item['quantity']
                
                item_price = topping['price'] * quantity
                total_price += item_price
                toppings_qty += quantity
        
        # Create order in legacy format for compatibility
        order_data = [
            data['customer_name'],
            total_quantity,
            pizza_details['marinara']['qty'],
            pizza_details['marinara']['size'],
            pizza_details['margherita']['qty'],
            pizza_details['margherita']['size'],
            pizza_details['salami']['qty'],
            pizza_details['salami']['size'],
            toppings_qty,
            total_price
        ]
        
        # Load existing orders and add new one
        orders = load_orders()
        orders.append(order_data)
        
        # Save orders
        save_orders(orders)
        
        return jsonify({
            'success': True,
            'order_id': len(orders),
            'total': total_price,
            'message': 'Order placed successfully!'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

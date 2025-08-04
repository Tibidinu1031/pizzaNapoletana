# Pizzeria Napoletana Da Tiberius - Web Frontend

A modern, responsive web frontend for the pizza ordering system with Italian restaurant theming.

## Features

### 🍕 **Pizza Menu**
- Interactive pizza cards with beautiful design
- 3 authentic Neapolitan pizzas: Marinara, Margherita, Salami
- Size selection (Small/Big) with dynamic pricing
- Quantity controls with intuitive +/- buttons

### 🛒 **Shopping Cart**
- Sliding cart sidebar with smooth animations
- Real-time cart updates and item count
- Remove items functionality
- Live total calculation

### 🎨 **Modern UI/UX**
- Responsive design that works on all devices
- Italian restaurant color scheme (warm oranges, elegant typography)
- Smooth hover effects and transitions
- Mobile-first responsive design
- Beautiful hero section with gradient background

### 📱 **Interactive Features**
- Real-time notifications for actions
- Modal dialogs for order confirmation
- Order history viewer with table format
- Form validation and error handling

### 💾 **Data Persistence**
- Same file-based storage as original console app
- Automatic backups with timestamps
- Compatible with existing `pizza.orders` format

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Access the Web Interface
Open your browser and navigate to:
```
http://localhost:5000
```

## File Structure

```
pizzaWindsurf/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Modern CSS styling
│   └── js/
│       └── app.js        # Frontend JavaScript
└── pizza.orders          # Data storage file (created automatically)
```

## API Endpoints

- `GET /` - Main web interface
- `GET /api/menu` - Get menu data (pizzas, toppings, sizes)
- `GET /api/orders` - Get all orders
- `POST /api/orders` - Place a new order

## Usage

1. **Enter Your Name**: Fill in the customer name field
2. **Select Pizzas**: Choose pizza type, size, and quantity
3. **Add Toppings**: Select extra toppings if desired
4. **Review Cart**: Click the cart icon to review your order
5. **Place Order**: Click "Place Order" to submit
6. **View Orders**: Click "View All Orders" to see order history

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with Italian restaurant theming
- **Icons**: Font Awesome
- **Fonts**: Playfair Display (headings), Inter (body text)
- **Data Storage**: File-based (compatible with original system)

## Browser Support

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Development

The application maintains full compatibility with your existing console-based system while providing a modern web interface. All order data is stored in the same format, so you can switch between the web interface and console application seamlessly.

## Features Comparison

| Feature | Console App | Web Frontend |
|---------|-------------|--------------|
| Pizza Selection | ✅ | ✅ |
| Size Options | ✅ | ✅ |
| Toppings | ✅ | ✅ |
| Order History | ✅ | ✅ |
| Data Persistence | ✅ | ✅ |
| Mobile Friendly | ❌ | ✅ |
| Shopping Cart | ❌ | ✅ |
| Visual Design | ❌ | ✅ |
| Real-time Updates | ❌ | ✅ |

Enjoy your new modern pizza ordering system! 🍕

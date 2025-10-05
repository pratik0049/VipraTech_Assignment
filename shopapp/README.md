# ShopApp - Django E-commerce with Stripe Integration

## Implementation Choices & Assumptions

### Assumptions Made
1. Single currency (USD) operation
2. Simple product catalog without categories/tags
3. No inventory management required
4. Single shipping address per order
5. Users must be registered to place orders

### Technical Decisions

#### Stripe Checkout vs Payment Intents
- Chose **Stripe Checkout** over Payment Intents for:
  - Faster implementation with built-in UI
  - Pre-built security and compliance
  - Mobile-responsive design out of the box
  - Simpler integration with fewer edge cases to handle

#### Preventing Double Charges & Race Conditions
1. Order status tracking:
   - Orders created as 'pending'
   - Status updated to 'paid' only after successful Stripe webhook
   - Double-check in success handler prevents duplicate processing

2. Session handling:
   - Stripe session ID tied to order via metadata
   - Order status verified before processing payment success

## Setup & Installation

1. Clone the repository
2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Unix/macOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file (see `.env.example` below)
5. Run migrations:
```bash
python manage.py migrate
```

6. Load sample products:
```bash
python manage.py seed_products
```

7. Run the development server:
```bash
python manage.py runserver
```

### `.env.example`
```
DB_NAME=shop_db
DB_USER=postgres
DB_PASSWORD=your_password
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
```

## Code Quality & Architecture Notes

### Strengths
1. Clear separation of concerns:
   - Models for data structure
   - Views for business logic
   - Utils for third-party integration

2. Security considerations:
   - Login required for sensitive operations
   - CSRF protection enabled
   - Stripe keys in environment variables

3. User experience:
   - Informative error messages
   - Order history pagination
   - Recent orders display

### Areas for Improvement
1. Add unit tests
2. Implement proper logging
3. Add inventory management
4. Consider async processing for webhooks
5. Add order email notifications
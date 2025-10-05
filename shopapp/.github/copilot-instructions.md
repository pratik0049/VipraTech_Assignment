# AI Agent Instructions for ShopApp

## Project Overview
This is a Django e-commerce application that integrates with Stripe for payments. The project follows a standard Django structure with the following key components:

- Product catalog with randomized display
- Shopping cart functionality
- Stripe checkout integration
- Order management system
- User authentication and registration

## Architecture & Data Flow

### Core Components
- `shop/models.py`: Contains `Product` and `Order` models
  - Products have: name, price, description, image_url
  - Orders store: user, payment info, line items as JSON, status
- `shop/views.py`: Handles business logic and Stripe integration
  - Uses Django's function-based views with `@login_required` decorator
  - Implements Stripe checkout session creation and webhook handling

### Key Integration Points
1. **Stripe Integration**:
   - Environment variables required: `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`
   - Checkout flow in `views.py:stripe_success`
   - Custom session creation in `utils.py:create_stripe_checkout_session`

2. **Database**:
   - PostgreSQL database (configured in settings.py)
   - Required env vars: `DB_NAME`, `DB_USER`, `DB_PASSWORD`

## Development Workflow

### Environment Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Required environment variables (in `.env`):
```
DB_NAME=shop_db
DB_USER=postgres
DB_PASSWORD=your_password
STRIPE_SECRET_KEY=your_stripe_secret
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable
```

### Project Patterns

1. **Order Processing**:
   - Orders start as 'pending'
   - After successful Stripe payment, status updates to 'paid'
   - Line items stored as JSON array in Order model

2. **User Experience**:
   - Products display in random order on index page
   - Order history shows 10 orders per page
   - Recent orders (last 3) shown on index page
   - Quantity limited to 10 items per product

### Testing & Debug Tips
- Run Django development server: `python manage.py runserver`
- Create test products: `python manage.py seed_products`
- Database migrations: `python manage.py migrate`

## Common Gotchas
- Always handle Stripe webhook responses asynchronously
- Check for existing paid orders in `stripe_success` view to prevent double-processing
- Ensure proper CSRF handling for POST requests
- Remember to validate quantities (1-10) in cart submission

## Template Locations
- Base template: `templates/base.html`
- Main pages: `templates/*.html`
- Login override: `templates/registration/login.html`
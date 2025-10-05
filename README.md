# 🛍️ ShopApp — Django E-commerce with Stripe Integration

A full-stack **Django + Stripe Checkout** application that allows users to browse products, add them to the cart, make secure payments, and view their order history.

---

## 🖼️ Screenshots

| Register | Home | Checkout | Stripe | Payment | View Order | Order History |
|-----------|------|-----------|---------|-----------|-------------|----------------|
| ![Register](images/Register.png) | ![Main](images/main.png) | ![Checkout](images/checkout.png) | ![Stripe](images/stripe.png) | ![Payment](images/payment.png) | ![View Order](images/vieworder.png) | ![View Order History](images/vieworderhistory.png) |


---

## 🚀 Repository

**GitHub URL:** [https://github.com/pratik0049/VipraTech_Assignment](https://github.com/pratik0049/VipraTech_Assignment)

---

## 🧠 Implementation Choices & Assumptions

### 🔹 Assumptions Made
1. Single currency — **USD**
2. Simple product catalog (no categories or tags)
3. No inventory tracking
4. Each order has a single shipping address
5. Only registered users can place orders

---

## ⚙️ Technical Decisions

### 🆚 Stripe Checkout vs Payment Intents
**Chosen:** `Stripe Checkout`  
**Reasons:**
- Faster integration with pre-built UI
- Strong built-in security and PCI compliance
- Mobile-responsive out of the box
- Fewer edge cases vs. manually managing Payment Intents

### 🔒 Preventing Double Charges & Race Conditions
1. **Order Status Flow**
   - Orders start as `pending`
   - Updated to `paid` only after verified Stripe webhook  
   - Double-check in success handler prevents duplicate confirmation

2. **Session Handling**
   - Stripe session ID stored in order metadata  
   - Order status re-verified before marking payment success

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/pratik0049/VipraTech_Assignment.git
cd VipraTech_Assignment
2️⃣ Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
.\venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Create the .env File
Copy values from .env.example and update credentials.

5️⃣ Run Migrations
bash
Copy code
python manage.py migrate
6️⃣ Load Sample Products
bash
Copy code
python manage.py seed_products
7️⃣ Start the Development Server
bash
Copy code
python manage.py runserver
🧾 Example .env File
env
Copy code
DB_NAME=shop_db
DB_USER=postgres
DB_PASSWORD=your_password
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
🧩 Code Quality & Architecture Notes
✅ Strengths
Separation of concerns

Models → Data structure

Views → Business logic

Utils → Third-party integrations

Security

Authentication required for order placement

CSRF protection enabled

Stripe keys stored in environment variables

User Experience

Simple, intuitive UI

Clear error messages

“My Orders” section shows recent payments

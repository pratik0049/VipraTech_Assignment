# 🛍️ ShopApp — Django E-commerce with Stripe Integration

A full-stack **Django + Stripe Checkout** application that allows users to browse products, add them to the cart, make secure payments, and view their order history.

🔄 Project Flow

1️⃣ Home Page – Shows 3 fixed products where users enter quantity and click Buy.
2️⃣ Checkout – Sends data to Django backend to create a Stripe Checkout Session.
3️⃣ Payment – User is redirected to Stripe’s test payment page for secure payment.
4️⃣ Order Creation – After successful payment, an Order is saved in the database with payment details.
5️⃣ My Orders – Users can view all past orders, total amount, and payment status.
6️⃣ Admin – Manage products, orders, and transactions.
---

## 🖼️ Screenshots

| Register | Main | Checkout | Stripe | Payment | View Order | Order History |
|-----------|------|-----------|---------|-----------|-------------|----------------|
| <img src="images/Register.png" width="200"/> | <img src="images/main.png" width="200"/> | <img src="images/checkout.png" width="200"/> | <img src="images/stripe.png" width="200"/> | <img src="images/payment.png" width="200"/> | <img src="images/vieworder.png" width="200"/> | <img src="images/vieworderhistory.png" width="200"/> |


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

Here’s your **README Setup & Installation** section rewritten in clean and properly formatted Markdown syntax 👇

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/pratik0049/VipraTech_Assignment.git
cd VipraTech_Assignment
```

---

### 2️⃣ Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create the `.env` File

Copy the values from `.env.example` and update your credentials accordingly.

Example:

```env
DB_NAME=shop_db
DB_USER=postgres
DB_PASSWORD=your_password

STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
```

---

### 5️⃣ Run Migrations

```bash
python manage.py migrate
```

---

### 6️⃣ Load Sample Products

```bash
python manage.py seed_products
```

---

### 7️⃣ Start the Development Server

```bash
python manage.py runserver
```

Then open your browser and visit 👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧩 Code Quality & Architecture Notes

### ✅ Strengths

**Separation of Concerns**

* **Models** → Define data structure
* **Views** → Contain business logic
* **Utils** → Handle third-party integrations

**Security**

* Authentication required for order placement
* CSRF protection enabled
* Stripe keys stored securely in environment variables

**User Experience**

* Simple, intuitive UI
* Clear error messages
* “My Orders” section shows recent payments

---


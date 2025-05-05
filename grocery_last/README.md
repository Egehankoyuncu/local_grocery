# Grocery Price Comparison – Multi-Store Grocery Price Checker

Grocery Price Comparison is a full-stack web application that allows users to search for grocery items and compare prices across multiple major stores like Kroger, Walmart, and Target.  
Users can register, log in, set their location, view the cheapest price for an item, and save favorite products to their account.

> 🛒 Built with Django (backend), HTML + CSS + Bootstrap (frontend).  
> 📦 Uses local JSON data (no external APIs) and static product images.  
> 🔐 Secure user authentication, filtering, and cheapest price highlighting.

---

## Features

- **Clean Homepage + Search Bar**  
  Simple and modern interface with a large search bar and informational banner.

- **Price Comparison by Store**  
  View the same product across Kroger, Walmart, and Target with unique prices and images.

- **Cheapest Price Highlighting**  
  Automatically highlights the store with the lowest price for each product.

- **User Registration and Login**  
  Built-in authentication for saving favorites and personalizing the experience.

- **Favorites System**  
  Logged-in users can add and view favorite store-product combinations.

- **Filtering & Sorting**  
  Search results can be filtered by store and sorted by ascending/descending price.

- **Location Prompting**  
  After login, users are prompted to enter their location to personalize results.

---

## Tech Stack

| Layer        | Technology       |
|--------------|------------------|
| Frontend     | HTML, CSS, Bootstrap |
| Backend      | Django (Python)  |
| Database     | Django ORM + SQLite |
| Auth         | Django Authentication |
| Data Source  | Local JSON (`data.json`) |
| Deployment   | (Self-hosted / optional) |

---

### 🔧 Backend Setup

```bash
git clone https://github.com/yourusername/grocery-comparison.git
cd grocery-comparison
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py load_data  
python manage.py runserver
```


---

## User Guide

### Registering an Account
- Click **Register** in the top navigation bar.
- Fill out username, email, and password.
- Submit to create your account.

### Logging In & Location Entry
- After login, you'll be prompted to enter your location.
- This is stored for personalized filtering.

### Searching for Products
- Use the large search bar on the homepage to find grocery items.
- The system will show all stores that sell the product.

### Comparing Prices
- Results show item name, store, price, and image.
- The cheapest store is automatically **highlighted**.

### Filtering & Sorting
- Use the dropdown menus to filter by store or sort by price.

### Saving Favorites
- Click the "Add to Favorites" button next to any store-item.
- View your saved items anytime from the Favorites page.


## Live Demo

https://yourdeploymenturl.com/

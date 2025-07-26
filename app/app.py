from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'supersecretkey'

products = {
    1: {'name': 'Laptop', 'price': 800},
    2: {'name': 'Headphones', 'price': 150},
    3: {'name': 'Mouse', 'price': 30}
}

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    cart_items = {pid: {'product': products[pid], 'quantity': qty} for pid, qty in cart.items()}
    return render_template('cart.html', cart=cart_items)

@app.route('/remove/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    cart.pop(product_id, None)
    session['cart'] = cart
    return redirect(url_for('view_cart'))

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return "Checkout complete!"

if __name__ == '__main__':
    app.run(debug=True)

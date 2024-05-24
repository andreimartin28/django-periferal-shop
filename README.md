# Periferal -> Django eCommerce Project

## Website: https://periferal.onrender.com/

## Description

This Django eCommerce project is a fully functional web application designed for online shopping. 

It allows users to create accounts, browse products and features/characteristics, add them to the cart, manage their cart and complete orders. 

The project is built using Python Django framework for fullstack and SQLite for the database. 

Docker is used to create images for deployment.

Written according to PEP 8 coding standard.

## Features
- User authentication: Users can sign up, log in, and log out.
- Product browsing: Users can browse through a list of available products and click on them for more information about features/characteristics.
- Reviews: Once the users are connected and browsing a product, they can leave a review.
- Cart management: Users can add products to their cart, remove items, and update quantities.
- Checkout process: Authenticated users can complete orders by providing shipping information and payment details.
- Admin panel: Administrators can manage products, categories, orders, and user accounts through the Django admin interface.
- Responsive design: The application is designed to be mobile-friendly.


## Installation for local usage
1. Create a folder for the project:
mkdir project_folder

2. Navigate to the project directory:
cd project_folder

3. Clone the repository:
git clone https://github.com/andreimartin28/django-periferal-shop.git

4. Build and run the Docker containers:
docker-compose up --build

4. Access the application at `http://localhost:10000`. You can change the port from docker with any port you prefer(ex: the classic port 8000).

## Usage

- Register for creating an account.

- Log in with the data provided.

- Go to my account page for completing data(first name, last name, phone number and updating the profile photo).

- Visit the home page to browse products, see details about the items and add them to the cart.

- On the cart page choose the quantity of the products and click on checkout.

- Checkout with a dummy billing address. 

- When redirected to the Stripe Test Mode API, use the following test card data and click on pay:  <br />
    -> Email: test@test.com <br />
    -> Card information: 4242 4242 4242 4242 <br />
    -> MM/YY: 12/34 and CVC: 567 <br />
    -> Cardholder name: any name you prefer, it really doesn't matter. <br />
    -> Country or region: any country or region you prefer.  <br />

- Succes! You have made a dummy order. For order history details, you can check by getting back to my account page while logged in.

- Administrators can access the admin panel at `http://localhost:10000/admin`, or the port you wrote on the 'docker-compose.yml' file, to manage the site.

- To see the administration panel, you have to create a superuser, so write on terminal 'python manage.py createsuperuser' and create one.

## Technologies Used

- Python
- Django
- HTML
- CSS
- HTMX
- Javascript
- SQLite
- Docker

## Credits
This project was developed by Martin Andrei-Alexandru.

## License
Copyright 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

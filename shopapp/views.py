import json
import stripe
from datetime import datetime, timedelta
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import JsonResponse


from .models import Product, Category, Order, OrderItem, Review
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .cart import Cart
# Create your views here.


def startingpage(request):
    # we display all the products from the database
    products = Product.objects.all()

    #
    brands = Product.objects.all().values_list(
        'brand', flat=True).distinct().order_by()

    categories = Category.objects.all()

    # we display the context dictionary here
    context = {
                "brands": brands,
                "products": products,
                "categories": categories,
    }

    return render(request, 'shopapp/starting_page.html', context)


def render_products_list(request):
    products = Product.objects.all()

    brands = Product.objects.all().values_list(
        'brand', flat=True).distinct().order_by()

    category = request.GET.get("category", None)

    if category:
        products = products.filter(category_id=category)

    brand = request.GET.get("brand", None)

    if brand:
        products = products.filter(brand=brand)

    search = request.GET.get("search", None)

    if search:
        if brand:
            products = products.filter(
                Q(name__icontains=search) & Q(brand=brand))
        else:
            products = products.filter(
                Q(name__icontains=search) | Q(brand=search))

    context = {
        'brands': brands,
        'products': products,
        "categories": Category.objects.all()
    }

    return render(request, 'shopapp/partials/products_list.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')

        if content:
            review = Review.objects.create(product=product,
                                           rating=rating,
                                           title=title,
                                           content=content,
                                           created_by=request.user,)

        return redirect('product', slug=slug)

    return render(request,
                  'shopapp/product.html',
                  {'product': product})


class Login(LoginView):
    template_name = 'shopapp/registration/login.html'


@login_required
def myaccount(request):
    return render(request,
                  'shopapp/myaccount.html')


@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(
                                request.POST,
                                instance=request.user
                                )

        profile_form = ProfileUpdateForm(
                                   request.POST,
                                   request.FILES,
                                   instance=request.user.profile
                                   )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()

            profile_form.save()

            messages.success(request,
                             "Your account has been updated!")

            return redirect('myaccount')

    else:
        user_form = UserUpdateForm(instance=request.user)

        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request,
                  'shopapp/edit_myaccount.html',
                  context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request,
                  'shopapp/registration/register.html',
                  {'form': form})


def check_email(request):
    email = request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse('''<div style='color: red;'>
                            This email already exists</div>''')
    else:
        return HttpResponse('''<div style='color: green;'>
                            This email is available</div>''')


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('''<div style='color: red;'>
                            This username already exists</div>''')
    else:
        return HttpResponse('''<div style='color: green;'>
                            This username is available</div>''')


def add_to_cart(request, product_id):
    cart = Cart(request)

    cart.add(product_id)

    return render(request,
                  'shopapp/cart/menu_cart.html')


def cart(request):
    return render(request,
                  'shopapp/cart/cart.html')


def success_page(request):

    today_date = datetime.now().date()

    first_date_range = today_date + timedelta(days=3)
    last_date_range = today_date + timedelta(days=9)

    date_range = {
        'first_estimated_arrival': first_date_range,
        'last_estimated_arrival': last_date_range
    }

    return render(request,
                  'shopapp/cart/success.html',
                  date_range)


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    elif action == 'decrement':
        cart.add(product_id, -1, True)
    else:
        cart.remove(product_id)

    product = Product.objects.get(pk=product_id)

    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'brand': product.brand,
                'name': product.name,
                'image': product.image,
                'price': product.price,
                'currency': product.currency,
            },
            'total_price': quantity * product.price,
            'quantity': quantity,
        }

    else:
        item = None

    response = render(request,
                      'shopapp/partials/cart_item.html',
                      {'item': item})

    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required
def checkout(request):
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE

    return render(request,
                  'shopapp/cart/checkout.html',
                  {'pub_key': pub_key})


def hx_menu_cart(request):
    return render(request,
                  'shopapp/cart/menu_cart.html')


def hx_cart_total(request):
    return render(request,
                  'shopapp/partials/cart_total.html')


def start_order(request):
    cart = Cart(request)

    data = json.loads(request.body)

    total_price = 0

    items = []

    for item in cart:
        product = item['product']

        total_price += product.price * item['quantity']

        obj = {
            'price_data': {
                'currency': 'eur',
                'product_data': {'name': product.name, },
                'unit_amount': product.price * 100,
            },
            'quantity': item['quantity']
        }

        items.append(obj)

    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/cart/checkout/success/',
        cancel_url='http://127.0.0.1:8000/cart/checkout/'
    )

    payment_intent = session.payment_intent

    first_name = data['first_name']

    last_name = data['last_name']

    email = data['email']

    address = data['address']

    optional_address = data['optional_address']

    phone = data['phone']

    country = data['country']

    city = data['city']

    zip_code = data['zip_code']

    order = Order.objects.create(user=request.user,
                                 first_name=first_name,
                                 last_name=last_name,
                                 email=email,
                                 address=address,
                                 optional_address=optional_address,
                                 phone=phone,
                                 country=country,
                                 city=city,
                                 zip_code=zip_code)

    order.payment_intent = payment_intent

    order.paid_amount = total_price

    order.paid = True

    order.save()

    for item in cart:
        product = item['product']

        quantity = item['quantity']

        final_price = product.price * quantity

        item = OrderItem.objects.create(order=order,
                                        product=product,
                                        price=final_price,
                                        quantity=quantity)

    cart.clear()

    return JsonResponse(
        {
            'session': session,
            'order': payment_intent
        }
    )

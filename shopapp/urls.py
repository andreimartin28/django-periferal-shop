from django.contrib import admin
from django.urls import path
from shopapp import views
from shopapp.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

     path('admin/',
          admin.site.urls),

     path('',
          views.startingpage,
          name="starting_page"),


     path('login/',
          views.Login.as_view(template_name="shopapp/registration/login.html"),
          name='login'),

     path('logout/',
          LogoutView.as_view(),
          name='logout'),

     path('register/',
          views.register,
          name="register"),

     path('myaccount/',
          views.myaccount,
          name='myaccount'),

     path('myaccount/edit',
          views.edit_myaccount,
          name='edit_myaccount'),

     path('product/<slug:slug>/',
          views.product,
          name='product'),

     path('render_products_list/',
          views.render_products_list,
          name='render_products_list'),

     path('add_to_cart/<int:product_id>/',
          views.add_to_cart,
          name='add_to_cart'),

     path('cart/',
          views.cart,
          name='cart'),

     path('cart/checkout/',
          views.checkout,
          name='checkout'),

     path('cart/checkout/success/',
          views.success_page,
          name='success'),

     path('update_cart/<int:product_id>/<str:action>/',
          views.update_cart,
          name='update_cart'),

     path('hx_menu_cart/',
          views.hx_menu_cart,
          name='hx_menu_cart'),

     path('hx_cart_total/',
          views.hx_cart_total,
          name='hx_cart_total'),

     path('order/start_order/',
          views.start_order,
          name='start_order'),

]

htmx_views = [
    path("check-username/",
         views.check_username,
         name='check-username'),

    path("check-email/",
         views.check_email,
         name='check-email'),
]

urlpatterns += htmx_views
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import *
from django.contrib.auth import views as auth

urlpatterns = [
    path('',homeView,name='home'),
    path('store/',storeView,name='store'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart_view/', cart_view, name='cart_view'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:item_id>/<str:action>/', update_quantity, name='update_quantity'),
    path('checkout/', checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/',order_confirmation, name='order_confirmation'),
    path('my_orders/', my_orders, name='my_orders'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('login/',auth.LoginView.as_view(template_name='app/login.html'),name='login'),
    path('signup/',signupView,name='signup'),
    path('logout/',auth.LogoutView.as_view(template_name='app/logout.html'),name='logout'),

    path('male/tshirts-shirts/', product_category_view, {'subcategory': 'T-shirts & Shirts'}, name='male_tshirts_shirts'),
    path('male/pants-trousers/', product_category_view, {'subcategory': 'Pants & Trousers'}, name='male_pants_trousers'),
    path('male/watches/', product_category_view, {'subcategory': 'Watches'}, name='male_watches'),
    path('male/sneakers-shoes/', product_category_view, {'subcategory': 'Sneakers & Shoes'}, name='male_sneakers_shoes'),

    path('female/tshirts-onepieces/', product_category_view, {'subcategory': 'T-shirts & One-Pieces'}, name='female_tshirts_onepieces'),
    path('female/lowers/', product_category_view, {'subcategory': 'Lowers'}, name='female_lowers'),
    path('female/makeup-products/', product_category_view, {'subcategory': 'MakeUp Products'}, name='female_makeup_products'),
    path('female/hair-skincare/', product_category_view, {'subcategory': 'Hair & Skin Care'}, name='female_hair_skincare'),

    path('home-appliance/pressure-cooker/', product_category_view, {'subcategory': 'Pressure Cooker'}, name='home_appliance_pressure_cooker'),
    path('home-appliance/cleaning/', product_category_view, {'subcategory': 'Cleaning'}, name='home_appliance_cleaning'),
    path('home-appliance/juicers-mixers-choppers/', product_category_view, {'subcategory': 'Juicers,Mixers & Choppers'}, name='home_appliance_juicers_mixers_choppers'),
    path('home-appliance/microwave-others/', product_category_view, {'subcategory': 'Microwave & others'}, name='home_appliance_microwave_others'),

    path('digital-electronics/other-digital-items/', product_category_view, {'subcategory': 'Other Digital Items'}, name='digital_electronics_other_digital_items'),
    path('digital-electronics/tv/', product_category_view, {'subcategory': 'T.V.'}, name='digital_electronics_tv'),
    path('digital-electronics/fridge/', product_category_view, {'subcategory': 'Fridge'}, name='digital_electronics_fridge'),
    path('digital-electronics/washing-machine/', product_category_view, {'subcategory': 'Washing Machine'}, name='digital_electronics_washing_machine'),

]


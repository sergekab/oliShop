from django.urls import path
from .views import login, home, signup, cart, checkout, orders
#from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('check_out', checkout.CheckOut.as_view(), name='checkout'),
    path('orders', orders.OrderView.as_view(), name='orders')
    #path('orders', auth_middleware(orders.OrderView.as_view()), name='orders'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('users/token/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('users/register/', views.registerUser, name='register-users'),
    # path('users/login/', views.loginUser, name='login-users'),
    path('users/', views.getUsers, name='users'),
    path('users/profile/', views.getUserProfile, name='user-profile'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>/', views.getProduct, name='product'),
]

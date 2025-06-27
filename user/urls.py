from django.urls import path
from .views import UserProfileView, UserCartView, UserFavoritesView

urlpatterns = [
    path('me/', UserProfileView.as_view(), name='user-profile'),
    path('me/cart/', UserCartView.as_view(), name='user-cart'),
    path('me/favorites/', UserFavoritesView.as_view(), name='user-favorites'),
]
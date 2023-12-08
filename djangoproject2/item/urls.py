from django.urls import path

from .views import ItemBuyRetrieveView, ItemRetrieveView

urlpatterns = [
    path('buy/<int:pk>/', ItemBuyRetrieveView.as_view()),
    path('item/<int:pk>/', ItemRetrieveView.as_view()),
]

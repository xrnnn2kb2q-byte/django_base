from django.urls import path
from book import views

urlpatterns = [
    path('create/',views.create_book),
    path('<city_id>/<shop_id>',views.shop)
]
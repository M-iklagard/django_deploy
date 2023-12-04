from django.urls import path
from .import views


urlpatterns = [
    path("", views.main_shop),
    path("cat/<str:chosen_cat>/", views.category),
    path("prod/<str:chosen_product>/", views.product),
    path("prod/<str:chosen_product>/buy", views.Buy.as_view()),
    path("api/", views.AllProducts.as_view())
]

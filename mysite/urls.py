from django.urls import path
from .views import MysiteView


urlpatterns = [
    path('', MysiteView.as_view(), name='home'),
]

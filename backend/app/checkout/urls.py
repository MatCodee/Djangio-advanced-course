from django.urls import path,include
from . import views

urlpatterns = [
    path('link/<str:code>',views.LinkAPIView.as_view()),
    
]
                
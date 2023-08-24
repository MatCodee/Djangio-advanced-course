from django.urls import path,include
from . import views


urlpatterns = [
    path('',include('common.urls')),
    path('products/frontend',views.ProductFrontendAPIView.as_view()),
    path('products/backend',views.ProductBackendAPIView.as_view()),
    path('links',views.LinkAPIView.as_view()),
    path('stats',views.StatsAPIView.as_view()),
    path('rankings',views.RankingsAPIView.as_view(),)
]
                
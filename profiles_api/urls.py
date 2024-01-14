from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()

# basename jest do uzyskiwanie url
router.register('hello-viewset', views.HelloViewset, basename='hello-viewset') #url jako argument

from profiles_api import views
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
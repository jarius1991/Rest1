from rest_framework.routers import DefaultRouter
from django.urls import path, include
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)  # nie musimy dawac basename bo mamy queryset, dajemy basename jesli chcemy przypisac nazwę powiązanego queryset
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view', views.HelloApiiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

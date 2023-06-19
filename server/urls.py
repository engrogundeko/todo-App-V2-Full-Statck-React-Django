from rest_framework.routers import DefaultRouter
from .views import UserViewSet
# from django.urls import path

router = DefaultRouter()
router.register('', UserViewSet, basename="todo")
urlpatterns = router.urls

# urlpatterns = [
#     path('create/', CreateUser.as_view(), name="createtodo"),
#     path('list/<int:pk>/', ListUser.as_view(), name="Listtodo"),
# ]


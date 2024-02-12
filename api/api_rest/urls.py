from rest_framework.routers import DefaultRouter
from api.api_rest.views import ProductoViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet, basename='producto')
urlpatterns = router.urls

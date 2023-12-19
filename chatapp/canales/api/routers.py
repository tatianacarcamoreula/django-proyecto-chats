from rest_framework.routers import DefaultRouter
from canales.api.viewsets import *

router = DefaultRouter()
router.register(
    prefix=r'chats',
    viewset=ListCreatePutChat,
    basename='chats',
)

urlpatterns = router.urls

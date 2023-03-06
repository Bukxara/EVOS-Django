"""evos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryView)
router.register('product', ProductView)
router.register('basket', BasketView)
router.register('order', AllOrdersView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),
    path('api/v1/', include(router.urls)),
    path('filter/category/<str:name>/', CategoryViewByName.as_view()),
    path('filter/category/id/<int:pk>/', ProductsByCategoryId.as_view()),
    path('filter/category/name/<str:name>/', ProductsByCategoryName.as_view()),
    path('filter/product/name/<str:name>/', ProductViewByName.as_view()),
    path('filter/basket/<str:tg_id>/', BasketByUser.as_view()),
    path('types/', AllCategories.as_view()),
    path('upgrade/<str:tg_id>/<str:product_id>/', upgrade),
    path('users/<str:tg_id>/', UsersView.as_view()),
    path('users/', post_users),
    path('orders/<str:tg_id>/', get_post_order),
    path('orders/', get_post_order)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

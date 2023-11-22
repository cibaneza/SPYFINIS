from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('create_post/', views.create_post, name='create-post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit-post'),

     path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

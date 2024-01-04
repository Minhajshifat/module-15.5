from django.urls import path,include
from . import views
urlpatterns = [
    path('add_album/', views.add_album, name='add_album'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
]
from django.urls import path
from .views import Single, Create, Update, List, Delete

urlpatterns = [
    path('single/<int:pk>', Single.as_view(), name='single'),
    path('list/', List.as_view(), name='list_phrase'),
    path('create/', Create.as_view(), name='create_phrase'),
    path('update/<int:pk>', Update.as_view(), name='edit_phrase'),
    path('Delete/<int:pk>', Delete.as_view(), name='delete_phrase'),
]

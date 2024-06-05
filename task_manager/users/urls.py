from django.urls import path, include
from task_manager.users.views import UsersListView, UserCreateView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='users_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('signin/', include('django.contrib.auth.urls')),
    path('signup/', include('django.contrib.auth'))
]
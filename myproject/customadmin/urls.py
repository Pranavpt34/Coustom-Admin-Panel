#
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.admin_login, name='login'),
#     path('dashboard/', views.dashboard, name='dashboard'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path("",views.admin_login,name='admin_login'),
    path("home",views.admin_homepage,name='admin_home'),
    path('users',views.show_users,name='user_admin_home'),
    path('logout',views.logout,name='logout'),
    path('user_edit',views.edit_user,name='edit_user'),
    path("user_delete",views.delete_user,name="delete_user"),
    path('search_user',views.searched_user,name='search_page'),
    path('user_register',views.user_register,name='user_register')
]
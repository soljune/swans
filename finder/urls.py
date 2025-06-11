from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    # path('payment/', views.payment, name='payment'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('pools/', views.pool_list, name='pool_list'),
    path('add_pool/', views.add_pool, name='add_pool'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('workout/<int:pk>/', views.workout_detail, name='workout_detail'),
    path('workout/<int:pk>/update/', views.workout_update, name='workout_update'),
    path('pool/<int:pk>/', views.pool_detail, name='pool_detail'),
    path('pool/<int:pk>/update/', views.pool_update, name='pool_update'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('pool/delete-pool/<str:pk>/', views.deletepool, name='delete-pool'),
    path('workout/deleteworkout/<str:pk>/', views.deleteworkout, name='deleteworkout'),

]
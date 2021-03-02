from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('plants/', views.index, name='index'),
     path('plants/<int:plant_id>/', views.plants_detail, name='plant_detail'),
     path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
     path('plants/<int:pk>/update/',
         views.PlantUpdate.as_view(), name='plants_update'),
     path('plants/<int:pk>/delete/',
         views.PlantDelete.as_view(), name='plants_delete'),
     path('plants/<int:plant_id>/add_watering/',
         views.add_watering, name='add_watering'),
     path('problems/', views.ProblemList.as_view(), name='problems_index'),
     path('problems/<int:pk>/', views.ProblemDetail.as_view(), name='problems_detail'),
     path('problems/create/', views.ProblemCreate.as_view(), name='problems_create'),
     path('problems/<int:pk>/update/', views.ProblemUpdate.as_view(), name='problems_update'),
     path('problems/<int:pk>/delete/', views.ProblemDelete.as_view(), name='problems_delete'),
     path('plants/<int:plant_id>/assoc_problem/<int:problem_id>/', views.assoc_problem, name='assoc_problem'),
     path('accounts/', include('django.contrib.auth.urls')),
     path('accounts/signup/', views.signup, name='signup'),

 
]

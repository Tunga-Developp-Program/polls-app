from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name="index"),
    # path('questions/', views.questions, name="questions"),
    # path('choices/', views.choices, name="questions"),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('choices/', views.ChoiceList.as_view()),
    path('choices/<int:pk>/', views.ChoiceDetail.as_view()),

]

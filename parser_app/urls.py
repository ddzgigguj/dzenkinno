from django.urls import path
from . import views

urlpatterns = [
    path('kivano_list_parser/', views.ParserKivanoListView.as_view()),
    path('faberlic_list_parser/', views.ParserFaberlicListView.as_view()),
    path('start_parsing/', views.ParserFormView.as_view()),
]
from django.urls import path

from polls.views import *

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('main/login', LoginView.as_view(), name='login'),
    path('register/', RegisterViews.as_view(), name='register'),
]

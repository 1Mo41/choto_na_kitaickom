from django.urls import path

from polls.views import *

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('main/login/', LoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('register/', RegisterViews.as_view(), name='register'),
    path('main/logout/', BBLogoutView.as_view(), name='logout'),
    path('main/register/done/', RegisterDoneView.as_view(), name='register_done'),
]

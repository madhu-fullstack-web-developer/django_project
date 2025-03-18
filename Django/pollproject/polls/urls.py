from django.urls import path
from .views import poll_list, poll_detail, vote, poll_results

urlpatterns = [
    path('', poll_list, name='poll_list'),
    path('<int:question_id>/', poll_detail, name='poll_detail'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('<int:question_id>/results/', poll_results, name='poll_results'),
]

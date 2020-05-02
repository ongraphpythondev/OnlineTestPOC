from django.urls import path

from exam.views import ExamCreateView, ExamListView, QuestionCreateView, OptionCreateView

app_name = 'exam'

urlpatterns = [
    path('create/', ExamCreateView.as_view()),
    path('list/', ExamListView.as_view()),
    path('create-question/', QuestionCreateView.as_view()),
    path('add-option/', OptionCreateView.as_view())
]

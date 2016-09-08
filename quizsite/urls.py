from django.conf.urls import url
from quiz import views
urlpatterns = [
	url(r"^$", views.start, name="start_page"),
	url(r"^quiz/([0-9]+)/$", views.quiz, name="quiz_page"),
	url(r"^quiz/([0-9]+)/question/([0-9]+)/$", views.question, name="question_page"),
	url(r"^quiz/([0-9]+)/result/$", views.result, name="result_page"),
	]


quizzes = [
	{
		"quiz_number": 1,
   		"name": "Klassiska böcker",
	   	"description": "Hur bra kan du dina klassiker?",
	   	"image" : "https://cdn1.cdnme.se/1024491/9-3/dsc05048_572a54a3ddf2b35586374f95.jpg"
	},
	{
		"quiz_number": 2,
   	   	"name": "Största 1slagen",
	   	"description": "Kan du dina lag?",
	   	"image": "https://cdn1.cdnme.se/1024491/7-3/aaaaaaaa_54117af62a6b22195b43bb70.jpg"
	},
	{
		"quiz_number": 3,
   	    	"name": "Världens mest kända hackare",
	    	"description": "Hackerhistoria är viktigt, kan du den?",
	    	"image": "https://d3vjk4jagnknqc.cloudfront.net/uploads/2013/11/f1190198-2048x1151.jpg",
	    	}
]



from django.shortcuts import render
def start(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/start.html", context)
def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz1.html", context)
def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    	"question": "Hur många bultar har ölandsbron?",
		"answer1": "12",
	   	"answer2": "66 400",
	    	"answer3": "7 428 954",
	    	"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)
def result(request, quiz_number):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/result.html", context)



# Create your views here.

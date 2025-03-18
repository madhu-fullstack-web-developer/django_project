from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

# Create your views here.
def poll_list(request):
    question = Question.objects.all()
    return render(request, 'polls/poll_list.html', {'questions': question})

def poll_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/poll_detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        selected_choice = question.choice_set.get(id=request.POST['choice'])
        selected_choice.votes +=1
        selected_choice.save()
        return redirect('poll_results', question_id=question.id)
    
def poll_results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/poll_results.html', {'question': question})


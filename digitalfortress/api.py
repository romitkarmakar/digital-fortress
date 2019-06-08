from django.http import HttpResponse, JsonResponse
from . import models
from django.contrib.auth.models import User
from .models import Hint, Solved, Round
from django.contrib.auth.decorators import login_required


@login_required
def getHints(request):
    if request.user.is_authenticated:
        responses = []
        user = User.objects.get(username=request.user.username)
        hints = Hint.objects.filter(round=user.profile.currRound)
        solved = Solved.objects.filter(user=request.user)

        for index, hint in enumerate(hints):
            val = 0
            for i in solved:
                if i.hint.id == hint.id:
                    val = 1

            responses.append({
                'question': hint.hint,
                'isSolved': val,
                'position': hint.position
            })

        return JsonResponse(responses, safe=False)


@login_required
def getRound(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        round = Round.objects.get(round=user.profile.currRound)

        return JsonResponse({
            'no': round.id,
            'question': round.question,
        })


@login_required
def checkHint(request):
    if request.user.is_authenticated:
        hintId = request.GET.get('id')
        hint = Hint.objects.get(id=hintId)
        if hint.answer == request.GET.get('answer'):
            return JsonResponse({
                'isTrue': 1,
                'position': hint.position
            })
        else:
            return JsonResponse({
                'isTrue': 0
            })

@login_required
def getLocations(request):
    if request.user.is_authenticated:
        response = []
        hints = Hint.objects.filter(round=request.user.profile.currRound)
        for hint in hints:
            response.append({
                'position': hint.position
            })
        
        return JsonResponse(response, safe=False)

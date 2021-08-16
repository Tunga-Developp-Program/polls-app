from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question,Choice
from .serializers import QuestionSerializer,ChoiceSerializer
from rest_framework import generics

# Create your views here.

# python dictionary
# person = {
#     "name":"John Doe",
#     "age": 34,
#     "country":"Uganda"

# }


#endpoints

endpoints={ 
    '1. questions': 'polls/questions',
    '2. single question':'polls/question/{id}',
    '3. choice': 'polls/choices',
    '4 single choice': 'polls/choice/{id}',

}

@api_view(["GET"])
def index(request):
    return Response(endpoints)



# # MOVED TO NEW FILE


@api_view(["GET", "POST"])
def questions(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        res = QuestionSerializer(questions, many=True) 
        return Response(res.data) # return JSON  instead of a template
    elif request.method == 'POST':
        req = QuestionSerializer(data=request.data) 
        if req.is_valid():
            req.save()
            return Response(req.data)
    return

@api_view(["GET", "POST"])
def choices(request):
    if request.method == 'GET':
        choices = Choice.objects.all()
        res = ChoiceSerializer(choices, many=True) 
        return Response(res.data)
    elif request.method == 'POST':
        req = ChoiceSerializer(data=request.data) 
        if req.is_valid():
            req.save()
            return Response(req.data)
    return

# end point can GET and POST
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# end point can GET, PATCH / PUT , DELETE
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer




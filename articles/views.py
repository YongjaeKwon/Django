from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    food = ['apple', 'banana', 'coconut',]
    info = {
        'name' : 'Yongjae'
    }
    context = {
        'foods' : food,
        'info' : info,
    }

    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['족발','치킨','라면','초밥','소주','맥주','콜라','피자',
    '막국수','삼겹살','햄버거','순대국']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods,
    }

    return render(request, 'dinner.html', context)

def throw(request):
    
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)
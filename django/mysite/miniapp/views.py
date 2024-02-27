from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
def models_list(request):
    random_number = random.randint(1, 100)
    return HttpResponse(f"Random number {random_number}")


def post_list(request):
    random_number = random.randint(1, 100)
    return render(request, "miniapp/post_list.html", {"num": random_number})

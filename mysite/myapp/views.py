from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.
def index(request):

    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')

        # get the food object from Food model
        consumed = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consumed)
        consume.save()
        foods = Food.objects.all()
    
    consumed_food = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()
    return render(request,'myapp/index.html',{'foods':foods, 'consumed_food':consumed_food})


def delete(request,id):
    food_to_del = Consume.objects.get(id=id)
    food_to_del.delete()
    return redirect('index')
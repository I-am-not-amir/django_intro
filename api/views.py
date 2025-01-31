from django.shortcuts import render,HttpResponse
import random
import string  
import requests

def random_password(request):
    # تعریف حروف بزرگ، حروف کوچک و اعداد  
    characters = string.ascii_letters + string.digits  
    # تولید پسورد تصادفی  
    password = ''.join(random.choice(characters) for i in range(12))   
    return HttpResponse(f'{password}')

def random_number(request):  
    # تولید عدد تصادفی  
    random_number = random.randint(1, 1000)  
    # دریافت اطلاعات از API  
    response = requests.get(f'http://numbersapi.com/{random_number}')  
    fact = response.text  
    # نمایش داده در قالب  
    return render(request, 'random_number/random_number.html', {'number': random_number, 'fact': fact})
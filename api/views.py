from django.shortcuts import render,HttpResponse
import random
import string  

def random_password(request):
    # تعریف حروف بزرگ، حروف کوچک و اعداد  
    characters = string.ascii_letters + string.digits  
    # تولید پسورد تصادفی  
    password = ''.join(random.choice(characters) for i in range(12))   
    return HttpResponse(f'{password}')

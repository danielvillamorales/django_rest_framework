from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render

class HelloWorldView(View):
    def get(self, request):
        context = {
        'name' : 'Daniel Villa Morales',
        'lenguajes' : ['Python', 'JavaScript', 'Java', 'C#', 'C++']
        }
        return render(request, 'hello.html', context)

# Create your views here.



from django.http import HttpResponse
from django.shortcuts import render

class TemplatesViews:

   def Index(self, request):
    return render(request, 'index.html')
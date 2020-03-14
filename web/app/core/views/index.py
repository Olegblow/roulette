from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse

class Index(View):
    
    def get(self, request):
        return JsonResponse(
            {
                'message': 'nice dick'
            }
        )


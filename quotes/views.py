from django.http.response import JsonResponse
from django.shortcuts import render

from .get_quotes import get_quotes

def index(req):
    
    return render(req, 'index.html') 

def get_quotes_ajax(req):
    if req.method == "POST":
        query = req.POST["query"]
        quotes = get_quotes(query)
        # context = {}
        # context["quotes"] = quotes
        return JsonResponse(quotes, safe=False)
    else:
        return JsonResponse({"error": "True"})


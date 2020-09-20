from django.shortcuts import render, HttpResponse

# Create your views here.

def hola_mundo(request):
    return HttpResponse("""
    <h1>Hola mundo con Django</h1>
    <h3>Me llamo Juan Manuel</h3>
    """)
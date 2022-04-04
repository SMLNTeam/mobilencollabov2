from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'drawing/index.html')

def Canvas(request):
    return render(request,'drawing/canvas.html')
from django.shortcuts import render

# Create your views here.
def ifelse(request):
    d={'a':10,'b':20}
    return render(request,'ifelse.html',d)

from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

TEMPLATE_DIR = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, 'index.html')
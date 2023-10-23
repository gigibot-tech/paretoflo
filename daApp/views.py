from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def upload(request):
    if request.method == "POST" and request.FILES:
        uploaded_files = request.FILES.getlist("files")
        for file in uploaded_files:
            print(file.name)
            print(file.read())

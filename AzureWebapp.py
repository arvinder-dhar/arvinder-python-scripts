def hello(request):
    print("Handling request to home page.")
    return HttpResponse("Hello, Arvinder!")

from django.shortcuts import render


def test_core(request):
    return render(request,'test_cors.html')
def test_core_server(request):
    return render(request,'test_cors_server.html')
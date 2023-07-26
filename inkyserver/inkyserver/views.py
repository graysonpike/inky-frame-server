from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, FileResponse
from .banking import generate_dashboard
from .rendering import get_hello_world_jpg_bytes


def plaid_link(request):
    if request.method == 'POST':
        test_value = request.POST.get('test_field', None)
        # Temporary for testing: run create dashboard function
        generate_dashboard()
        print(f'Test Value: {test_value}')
        return redirect("plaid_link")
    if request.method == "GET":
        return render(request, 'inkyserver/plaid_link.html')
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def cairo_test(request):
    bytes = get_hello_world_jpg_bytes()
    return FileResponse(bytes, as_attachment=True, filename='blank.jpg')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
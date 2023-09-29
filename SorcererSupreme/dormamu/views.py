from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DormamuSerializer
from .models import Dormamu

# Create your views here.

def strange(request):
    context = { }
    return render(request,"index.html",context)

@api_view(['GET','POST'])
def dormamu_list(request):
    if request.method == 'GET':
        dormamu = Dormamu.objects.all()
        serializer = DormamuSerializer(dormamu,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DormamuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def dormamu_delete(request,pk):
    try:
        dormamu = Dormamu.objects.get(pk=pk)
    except Dormamu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        dormamu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
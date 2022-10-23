from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from super_types.serializers import *
# Create your views here.


@api_view(['GET','POST'])
def supersList(request):
    
    if request.method == 'GET':
        
        super_type = request.query_params.get('type')
        
        supers = Super.objects.all()
        
        supers_heroes = SuperSerializer(supers.filter(super_type=1),many=True)
        supers_villains = SuperSerializer(supers.filter(super_type=2),many=True)
        
        custom_response = {
            'Heroes': supers_heroes.data,
            'Villains': supers_villains.data
        }
        
        serializer = custom_response
        
        if super_type:
            supers = supers.filter(super_type__type=super_type)   
            serializer = SuperSerializer(supers,many=True)
            serializer = serializer.data
        return Response(serializer)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def supersDetail(request, pk):

    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super) 
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
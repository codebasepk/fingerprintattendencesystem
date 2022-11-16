from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import FingerprintProfileModel
from .serializers import FingerprintProfileSerializer
from .serializers import RegisterPersonSereializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import io


class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = FingerprintProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg': 'Data Uploaded Successfully',
                'status': 'success', 'candidate': serializer.data},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def registerUser(self, request, format=None):
        serializer = RegisterPersonSereializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg': 'Data Uploaded Successfully',
                'status': 'success', 'candidate': serializer.data},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        candidates = FingerprintProfileModel.objects.all()
        serializer = FingerprintProfileSerializer(candidates, many=True)
        return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = FingerprintProfileModel.objects.get(id=id)
        serializer = FingerprintProfileSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

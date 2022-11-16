from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import FingerprintProfileModel
from .serializers import FingerprintProfileSerializer
from .serializers import RegisterPersonSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import io


class RegisterView(APIView):
    def post(self, request, format=None):
        serializer = RegisterPersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg': 'Data Uploaded Successfully',
                'status': 'success', 'candidate': serializer.data},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


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

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            candidates = FingerprintProfileModel.objects.get(id=id)
            serializer = FingerprintProfileSerializer(candidates)
            return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)
        candidates = FingerprintProfileModel.objects.all()
        serializer = FingerprintProfileSerializer(candidates, many=True)
        return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        id = pk
        candidates = FingerprintProfileModel.objects.get(pk=id)
        serializer = FingerprintProfileSerializer(candidates, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

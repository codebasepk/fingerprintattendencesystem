import io

import django_filters
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.templatetags.rest_framework import data

from .models import FingerprintProfileModel, RegisterPersonModel
from .serializers import FingerprintProfileSerializer
from .serializers import RegisterPersonSerializer
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveUpdateAPIView, \
    get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework import authentication, permissions
from django_filters import rest_framework as filters


# class RobotList(generics.ListAPIView):
#     queryset = FingerprintProfileModel.objects.all()
#     serializer_class = FingerprintProfileSerializer
#     filter_backends = (filters.DjangoFilterBackend, SearchFilter)
#     filterset_fields = ('fpid', 'currentdate')
#     search_fields = ('fpid', 'currentdate')


# class ListUsers(APIView):
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.fpid for user in FingerprintProfileModel.objects.all()]
#         currentdate = [user.currentdate for user in FingerprintProfileModel.objects.all()]
#         return Response(currentdate)

class ChangeStatus(generics.GenericAPIView):
    serializer_class = FingerprintProfileSerializer

    def patch(self, request, *args, **kwargs):
        fpid = kwargs.get('fpid', '0')
        currentdate = kwargs.get('currentdate', '0')
        instance = get_object_or_404(FingerprintProfileModel, fpid=fpid, currentdate=currentdate)
        serializer = FingerprintProfileSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def get(self, request, pk=None, format=None):
        fpid = pk
        if fpid is not None:
            candidates = RegisterPersonModel.objects.get(fpid=fpid)
            serializer = RegisterPersonSerializer(candidates)
            return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)
        candidates = RegisterPersonModel.objects.all()
        serializer = RegisterPersonSerializer(candidates, many=True)
        return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk=None, format=None):
        fpid = pk
        stu = RegisterPersonModel.objects.get(fpid=fpid)
        stu.delete()
        return Response({'msg': 'Data Deleted'})


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
        fpid = pk
        if fpid is not None:
            candidates = FingerprintProfileModel.objects.get(fpid=fpid)
            serializer = FingerprintProfileSerializer(candidates)
            return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)
        candidates = FingerprintProfileModel.objects.all()
        serializer = FingerprintProfileSerializer(candidates, many=True)
        return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)

    # def patch(self, request, pk, format=None):
    #     fpid = pk
    #     candidates = FingerprintProfileModel.objects.get(fpid=fpid)
    #     serializer = FingerprintProfileSerializer(candidates, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': 'partially data updated', 'candidates': serializer.data},
    #                         status=status.HTTP_200_OK)
    #     return Response(serializer.errors)

    def patch(self, request, *args, **kwargs):
        fpid = kwargs.get('fpid', '0')
        currentdate = kwargs.get('currentdate', '0')
        instance = get_object_or_404(FingerprintProfileModel, fpid=fpid, currentdate=currentdate)
        serializer = FingerprintProfileSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

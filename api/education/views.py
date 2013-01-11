from api.education.models import Education
from api.education.serializers import EducationSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

ALLOWED_ORIGINS = '*'
ALLOWED_METHODS = 'GET,POST,PUT,DELETE,OPTIONS'


# class EducationList(APIView):

#     def get(self, request, format=None):
#         ed_list = Education.objects.all()
#         serializer = EducationSerializer(ed_list)
#         headers = {
#                 'Access-Control-Allow-Origin': ALLOWED_ORIGINS,
#                 'Access-Control-Allow-Methods': ALLOWED_METHODS
#                 }
#         return Response(serializer.data, headers=headers)


# class EducationView(APIView):

#     def get_object(self, pk):
#         try:
#             Education.objects.get(pk=pk)
#         except: DoesNotExcist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         education = self.get_object(pk)
#         serializer = EducationSerializer(education)
#         return Response(serializer.data)        


class EducationList(generics.ListCreateAPIView):
    model = Education
    serializer_class = EducationSerializer


class EducationView(APIView):
    model = Education
    serializer_class = EducationSerializer
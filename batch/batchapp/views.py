from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
import random
import string
from django.contrib.auth.models import User
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import action

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        batch = Batch.objects.all()
        return batch

    def create(self, request, *args, **kwargs):
        # global code_list
        code_list=[]
        data = request.data
        print("Batch Name:",data.get("batch_name"))
        print("NUmber of Codes you want to generate:",data.get("num"))
        number = data.get("num")

        def get_random_string():
            for j in range(int(number)):
                source = string.ascii_letters + string.digits
                result_str = ''.join(random.choice(source) for i in range(10))
                code_list.append(result_str)

        get_random_string()
        new_batch = Batch.objects.create(user_id=request.user,
                                         batch_name = data.get("batch_name"),
                                         code = code_list,
                                         num = data.get("num"),
                                         user = data.get("user")
                                         )
        serializer = BatchSerializer(new_batch)
        return Response(serializer.data)

    def retrive(self, request, pk=None):
        queryset = Batch.objects.filter(pk=pk,user_id=request.user, )
        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = BatchSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    # @action(detail=True, methods=["GET"])
    # def codes(self, request, pk=None):
    #     if request.method == 'GET':
    #         user=request.user.is_authenticated
    #         if user:
    #             user = self.request.user
    #             print(user)
    #             codes = Batch.objects.filter(code=request.user)
    #             print(codes)
    #             serializer = UserSerializer(codes, many=True)
    #             return Response(serializer.data, status=200)
    #         else:
    #             pass



class StoreCodesApi(APIView):
    def get(self, request,**kwargs):
        if kwargs.get('pk'):
            pk = kwargs.get('pk')
            obj = get_object_or_404(Store.objects.all(), pk=pk)
            codes = StoreSerializer(obj)
            return Response({'codes':codes.data})
        query_set = Store.objects.all().last()
        serializer = StoreSerializer(query_set)
        return Response(serializer.data)






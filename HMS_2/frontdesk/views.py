from django.shortcuts import render

from rest_framework.decorators import APIView
from rest_framework.response import Response

from frontdesk.models import GuestInfo
from frontdesk.serializers import GuestInfoSerializer


# Create your views here.

class GuestInfoView(APIView):
    
    def get(self,request):
        guest_objs = GuestInfo.objects.all()
        serializer = GuestInfoSerializer(guest_objs,many=True)
        return Response({"status": 200, "payload":serializer.data})
    
    def post(self,request):
        serializer = GuestInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "payload":serializer.data})
        else:
            return Response({"status": 403, "error": serializer.errors})
        
    def put(self,request):
        guestinfo_obj = GuestInfo.objects.get(id=request.data['id'])
        serializer = GuestInfoSerializer(guestinfo_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "payload":serializer.data})
        else:
            return Response({"status": 403, "error": serializer.errors})
        
    def patch(self,request):
        guestinfo_obj = GuestInfo.objects.get(id=request.data['id'])
        serializer = GuestInfoSerializer(guestinfo_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "payload":serializer.data})
        else:
            return Response({"status": 403, "error": serializer.errors})
        
    def delete(self,request):
        try:   
            id = request.GET.get('id')
            guest_obj = GuestInfo.objects.get(id=id)
            guest_obj.delete()
            return Response({'status': 200, 'message': 'data deleted'})
        except:
            return Response({"status": 403, "message": "Invalid id data not found!"})
import logging 

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.


logger = logging.getLogger(__name__)


@api_view(["POST"])
def create_user(request):
    data = request.data

    username = data.get("username")
    password = data.get("password")
    is_active = data.get("is_active", True)
    user = User.objects.create_user(
            username=username,
            password=password,
            is_active=is_active
        )
    
    user.save()
    return Response({
        "status":"successfully added"
    })



@api_view(['PATCH'])
def deactivate_user(request, user_id):
    try :
        user = User.objects.filter(id=user_id).first()
        

        if not user:
            logger.warning(f"User {user_id} not found")
            return Response({
                "Stauts":"failed","message":f"User {user_id} not found"
            })
        
        if not user.is_active :
            logger.info(f"User {user_id} already inactive")
            return Response({
                "Status":"success","message":f"User {user_id} already inactive"   
            })
        
        user.is_active = False 
        user.save()

        logger.info(f"Successfully deactivated {user_id}")

        return Response({
               "status":"success","message":f"Successfully deactivated {user_id}"
        })
        
    except Exception as e :
        logger.error(f"Error while deactivating user {user_id}: {str(e)}")
        return Response({
            "Status":"error","message":f"Internal server error"
        })



from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import User, Referral
from .serializers import UserSerializer, ReferralSerializer

@api_view(['POST'])
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def referrals(request):
    user = request.user
    referrals = Referral.objects.filter(referrer=user)
    
    paginator = PageNumberPagination()
    paginated_referrals = paginator.paginate_queryset(referrals, request)
    
    serializer = ReferralSerializer(paginated_referrals, many=True)
    return paginator.get_paginated_response(serializer.data)
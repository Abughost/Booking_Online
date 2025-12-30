from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.seralizers import SendCodeSerializer
from apps.seralizers.auth import VerifyCodeSerializer
from apps.utils import send_code, check_code
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class SendCodeApiView(APIView):

    serializer_class = SendCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        _valid, ttl = send_code(data['phone'])
        if _valid:
            return Response({"message" : "Sms code send"}, status.HTTP_200_OK)
        return Response({"message": f"You have {ttl} seconds left"}, status.HTTP_400_BAD_REQUEST)

class VerifyCodeApiView(APIView):
    serializer_class =VerifyCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone , code = data['phone'], data['code']
        valid = check_code(phone,code)
        if not valid:
            return Response({"message": "incorrect code"}, status.HTTP_400_BAD_REQUEST)

        return Response({'message': "correct code",
                         "data": serializer.get_data(phone),},
                        status.HTTP_202_ACCEPTED)

from rest_framework import viewsets
from .models import Lottery
from .serializers import LotterySerializer

class LotteryViewSet(viewsets.ModelViewSet):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer

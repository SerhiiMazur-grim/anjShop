from rest_framework import generics

from .models import NewPostShipping, UkrPostShipping
from .serializer import NewPostShippingSerializer, UkrPostShippingSerializer


class NewPostShippingCreateView(generics.CreateAPIView):
    queryset = NewPostShipping
    serializer_class = NewPostShippingSerializer


class UkrPostShippingCreateView(generics.CreateAPIView):
    queryset = UkrPostShipping
    serializer_class = UkrPostShippingSerializer

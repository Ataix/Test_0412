import stripe
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import ItemSerializer


class ItemBuyRetrieveView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': instance.name,
                        },
                        'unit_amount': int(instance.price * 100),
                    },
                    'quantity': 1
                }
            ],
            mode='payment',
            success_url='http://localhost:8000/api/schema/swagger-ui/',
            cancel_url='http://localhost:8000/api/schema/swagger-ui/',
        )
        return Response(
            {'session_id': session.id}
        )


class ItemRetrieveView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_retrieve.html'

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item)
        return Response(
            {
                'serializer': serializer,
                'item': item
            }
        )

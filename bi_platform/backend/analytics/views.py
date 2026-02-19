
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import OrderItem

@api_view(['GET'])
def sales_summary(request):
    data = OrderItem.objects.values('product__name').annotate(total_sales=Sum('quantity'))
    return Response(data)

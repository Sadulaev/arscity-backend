from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem, Favorite, Order, OrderItem
from .serializers import CartItemSerializer, FavoriteSerializer, OrderSerializer


class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CartTotalPriceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total = 0.0
        for item in cart_items:
            price = getattr(item.product, 'price', 0.0)
            total += float(price) * item.quantity
        return Response({'total_price': round(total, 2)})


class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class FavoriteDeleteView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CreateOrderFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)
        if not cart_items.exists():
            return Response({'detail': 'Cart is empty.'}, status=400)

        data = request.data
        required = ['first_name', 'last_name', 'phone', 'email', 'delivery_method', 'payment_method']
        for field in required:
            if field not in data:
                return Response({field: 'This field is required.'}, status=400)

        if data['delivery_method'] == 'delivery' and not data.get('delivery_address'):
            return Response({'delivery_address': 'Required for delivery.'}, status=400)

        total = 0
        for item in cart_items:
            price = getattr(item.product, 'price', 0)
            total += float(price) * item.quantity

        order = Order.objects.create(
            user=user,
            first_name=data['first_name'],
            last_name=data['last_name'],
            patronymic=data.get('patronymic', ''),
            phone=data['phone'],
            email=data['email'],
            comment=data.get('comment', ''),
            delivery_method=data['delivery_method'],
            delivery_address=data.get('delivery_address', ''),
            payment_method=data['payment_method'],
            total_price=total
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                content_type=item.content_type,
                object_id=item.object_id,
                quantity=item.quantity
            )

        cart_items.delete()
        return Response(OrderSerializer(order).data, status=201)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
from rest_framework.views import APIView, Request, Response, status
from .serializer import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404

class ProductView(APIView):
    def get(self, request: Request) -> Response:
        prducts = Product.objects.all()
        serializer = ProductSerializer(prducts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ProductDetailsView(APIView):
    def get(self, request: Request, product_id: int) -> Response:
        product = get_object_or_404(Product, id=product_id)  
        serializer = ProductSerializer(instance=product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request: Request, product_id: int) -> Response:
        post = get_object_or_404(Product, id=product_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
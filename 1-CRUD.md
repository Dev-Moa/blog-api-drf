
________________________________ CRUD IN REST API  _________________________________________________________________

```python 

class ProductsAPIView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data,status=201)
    
    def post(self,request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    
class ProductAPIView(APIView):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product,many=False)
        return Response(serializer.data,status=201)
    def put(self,request,pk):
        data = request.data
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(instance=product,data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        product.delete()
        return Response("Product was deleted")

```
USING MIXINS

```python

class ProductsAPIView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



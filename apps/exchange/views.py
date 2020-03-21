
from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import viewsets

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

from .permissions import IsOwnerOrReadOnly, IsBuyerOrSeller

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from .serializers import *


#------------------------------------------------------------------------------
#Category
#------------------------------------------------------------------------------


class CategoryList(ListAPIView):
    """
        This view is for API get request for Category
    """
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny]



class CategoryDetail(RetrieveAPIView):
    """
        This view is for API get request for Category
    """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [AllowAny]


#------------------------------------------------------------------------------
#Items
#------------------------------------------------------------------------------

class ItemImageViewset(viewsets.ModelViewSet):
    """
        This view is for API get request for Images attached to the Item.
    """
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer
    permission_classes = [AllowAny]

class ItemCreate(CreateAPIView):
    """
        This view is for API post request for Items to be created
    """
    queryset = Item.objects.all()
    serializer_class = ItemCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class ItemUpdate(RetrieveUpdateAPIView):
    """
        This view is for API post request for Items to be updated

    """
    queryset = Item.objects.all()
    serializer_class = ItemCreateUpdateSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        serializer.save()

class ItemDelete(DestroyAPIView):
    """
        This view is for API post request for Items to be deleted
    """
    queryset = Item.objects.all()
    serializer_class =  ItemDetailSeralizer
    permission_classes = [IsAdminUser]


class ItemDetail(RetrieveAPIView):
    """
        This view is for API get request for the details of an Item
    """
    queryset = Item.objects.all()
    serializer_class = ItemDetailSeralizer
    permission_classes = [AllowAny]

class ItemList(ListAPIView):
    """
        This view is for API get request for detail ItemList
    """

    queryset = Item.objects.all()
    serializer_class = ItemListlSeralizer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['name', 'category', 'description']
    ordering_fields = ('lastActive',)
    permission_classes = [AllowAny]


#------------------------------------------------------------------------------
#Listing
#------------------------------------------------------------------------------


# class ListingCreate(CreateAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingCreateUpdateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(seller = self.request.user)
#
# class ListingUpdate(RetrieveUpdateAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingCreateUpdateSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#
#     def perform_update(self, serializer):
#         serializer.save(seller = self.request.user)
#
# class ListingDelete(DestroyAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingDetailSeralizer
#     permission_classes = [IsOwnerOrReadOnly]
#
#
# class ListingDetial(RetrieveAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingDetailSeralizer
#     permission_classes = [AllowAny]
#
#
# class ListingList(ListAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingListSeralizer
#     permission_classes = [AllowAny]
#
#     def get_queryset(self, *args, **kwargs):
#         queryset_list = Listing.objects.all()
#         query = self.request.GET.get("q")
#         if query:
#             queryset_list = queryset_list.filter(
#             Q(item__name__icontains = query)|
#             Q(item__description__icontains = query)|
#             Q(item__subCategory__name__icontains = query)|
#             Q(item__category__name__icontains = query)|
#             Q(price__icontains = query)
#
#             ).distinct()
#         return queryset_list




#------------------------------------------------------------------------------
#Transaction
#------------------------------------------------------------------------------

class TransactionCreate(CreateAPIView):
    """
        This view is for the API post request to create an Transaction
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionCreateUpdateSerializer
    premission_classes = [IsAuthenticated]


    #def perform_create(self, serializer):

class TransactionUpdate(RetrieveUpdateAPIView):
    """
        This view is for the API post request to update Transactions
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionCreateUpdateSerializer
    permission_classes = [IsBuyerOrSeller, IsAdminUser]

##Need to add the query to this thing
class TransactionList(ListAPIView):
    """
        This view is for the API get request to list out Transactions
    """
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if (user.is_superuser):
            return Transaction.objects.all()
        else:
            return Transaction.objects.filter(Q(seller = user) | Q(buyer = user))


class TransactionDetail(RetrieveAPIView):
    """
        This view is for the API get request for a detailed view of Transaction
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsBuyerOrSeller, IsAdminUser]

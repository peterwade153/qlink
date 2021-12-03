from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http.response import Http404, HttpResponseRedirect
from django.db.models import F
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Url
from .serializers import ShortenerSerializer


class ShortenerView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        serializer = ShortenerSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "message": "failed",
                "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save(user=request.user)
        return Response({
            "original_url": serializer.data['original_url'],
            "new_url": request.build_absolute_uri('/') + 'api/' + serializer.data['short_url'],
            "message": "success"
            },
            status=status.HTTP_201_CREATED
        )

    def get(self, request):
        urls = Url.objects.filter(user=request.user.id).order_by('-created')
        serializer = ShortenerSerializer(urls, many=True)
        return Response({
            "urls": serializer.data},
            status=status.HTTP_200_OK
        )


class RedirectView(APIView):

    def get(self, request, short_url):
        try:
            url = Url.objects.get(short_url=short_url)
            url.visit_count = F('visit_count') + 1
            url.save()
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            raise Http404("Link Broken!")
        return HttpResponseRedirect(url.original_url)

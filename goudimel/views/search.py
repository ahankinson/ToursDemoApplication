# from django.views.generic import View
# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, JSONPRenderer

from goudimel.serializers.search import SearchSerializer
from goudimel.renderers.custom_html_renderer import CustomHTMLRenderer
from goudimel.helpers.solrsearch import SolrSearch
from goudimel.helpers.paginate import SolrPaginator, SolrGroupedPaginator
from goudimel.helpers.json_response import JsonResponse

class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(APIView):
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, SearchViewHTMLRenderer)

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', None)
        # if we don't have a query parameter, send an empty response
        # back to the template. It will then present the search page
        # to the user
        if not query:
            return Response({}, status=status.HTTP_200_OK)

        s = SolrSearch(request)
        search_results = s.search()
        facets = s.facets(['publisher', 'composer_src'])

        result = {'results': search_results, 'facets': facets.facet_counts}
        response = Response(result, status=status.HTTP_200_OK)
        return response
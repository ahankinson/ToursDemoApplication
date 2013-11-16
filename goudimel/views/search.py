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
        querydict = request.GET

        s = SolrSearch(request)
        facets = s.facets(['publisher', 'composer_src', 'forces'])

        # if we don't have a query parameter, send empty search results
        # back to the template, but still send along the facets.
        # It will then present the search page to the user with the facets
        if not querydict:
            result = {'results': [], 'facets': facets.facet_counts}
            return Response(result, status=status.HTTP_200_OK)

        search_results = s.search()
        result = {'results': search_results, 'facets': facets.facet_counts}
        response = Response(result, status=status.HTTP_200_OK)
        return response
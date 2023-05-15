from rest_framework.views import APIView # APIView is the class we need to create our API views
from rest_framework.response import Response # Response is the standard response object returned by our APIView

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None): # format=None is used to add format suffixes to the end of our endpoint URLs
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview}) # Response must always be passed a dictionary or a list
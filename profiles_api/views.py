from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ test api view"""

    def get(self,request,format = None):

        """return a list of APIView feature"""

        an_apiview = [

            'Uses HTTP methods as function (get,post,patch,delete)',
            'Is similar to traditional django view',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

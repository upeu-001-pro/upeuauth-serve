import json
from rest_framework.response import Response
from rest_framework.views import APIView

from oauth2_backend.models.menu import Menu
from backend_utils.logs import log_params

from logging import getLogger
log = getLogger(__name__)


class RouterView(APIView):
    """
    View to list routers of menu.
    """

    def get(self, request, format=None):
        """
        Insertar json en el campo router_json
    {
        "catalogo.catalogo.categorias": {
            "url": "/categorias",
            "data": {
                "section": "Catálogo",
                "page": "Categorías"
            },
            "templateUrl": "app/views/categorias/index.html",
            "loginRequired": true
        },
        "catalogo.catalogo.categoriasNew": {
            "url": "/categorias/new",
            "data": {
                "section": "Catálogo",
                "page": "Categorías"
            },
            "templateUrl": "app/views/categorias/form.html"
        },
        "catalogo.catalogo.categoriasEdit": {
            "url": "/categorias/:id/edit",
            "data": {
                "section": "Catálogo",
                "page": "Categorías"
            },
            "templateUrl": "app/views/categorias/form.html"
        }
    }
        """

        router_list = list(col["router_json"] for col in Menu.objects
                           .values("router_json")
                           .filter().order_by("pos"))

        router_json = []

        if router_list:
            for router in router_list:
                # '{"key": "value"}'
                # '{\r\n    \"catalogo\": {\r\n \"url\": \"/catalogo\" }\r\n}'
                if router:
                    router_json.append(
                        json.loads(router)
                    )
        # print('router_json=', (router_json))

        return Response(router_json)

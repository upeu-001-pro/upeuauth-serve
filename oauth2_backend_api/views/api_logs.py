import os
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from backend_utils.logs import log_params
from logging import getLogger
log = getLogger(__name__)


class LogView(APIView):
    """
    View to list log.
    """
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None, param=None):
        """
        Return menu of current user.
        """
        filedebug = 'temp\logs\log%s.txt' % (param)
        LOG_FILE = os.path.join(settings.BASE_DIR, filedebug)

        list = []
        try:

            audit = None
            try:
                audit = open(LOG_FILE, 'r')
            except (OSError, IOError) as e:
                print("%s no se encuentra" % filedebug)
                pass
            if audit:
                try:
                    for row in reversed(audit.readlines()):

                        data = row.split(']')
                        print (data)

                        list.append({
                            "date": data[0].strip().strip('['),
                            "type": data[1].strip().strip('['),
                            "mod": data[2].strip().strip('['),
                            "path": data[3].strip().strip('['),
                            "ip": data[4].strip().strip('['),
                            "user": data[5].strip().strip('['),
                            "method": data[6].strip().strip('['),

                            "desc": data[7].strip(),
                        })
                except:
                    pass

            if audit:
                audit.close()

        except Exception as e:
            print(e)

        return Response(list)

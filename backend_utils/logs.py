"""
@copyright   Copyright (c) 2013
@author      Angel Sullon (@asullom)
@package     utils

Descripcion: datos extra para los archivos logYYYY-MM-DD.txt
"""
import logging
log = logging.getLogger(__name__)


def log_params(request):
    """
    Usar en todos los log
    Usage::
        import logging
        log = logging.getLogger(__name__)
        ...
        log.info('Writing in log file', extra=log_params(self.request))
        log.warning('Writing in log file ',extra=log_params(self.request))
        log.error(force_text('Writing file'), extra=log_params(self.request))
        log.critical('Writing in log file', extra=log_params(self.request))
        log.debug('Writing in log file',
                  extra=log_params(self.request))  # no usar en consola
    """

    return {
        'path': request.get_full_path(),
        'ip': request.META['REMOTE_ADDR'],
        'user': request.user,
        'method': request.method
    }

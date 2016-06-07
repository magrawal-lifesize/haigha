import warnings

from haigha.transports.gevent_transport import GeventTransport

try:
    from gevent import ssl, socket
except ImportError:
    warnings.warn('Failed to load gevent modules')

class GeventSSLTransport(GeventTransport):
    def connect(self, (host, port)):
        '''
        Connect using a host,port tuple
        '''
        def _sslwrapper(family, socktype, proto):
            sock = socket.socket(family, socktype, proto)
            return ssl.wrap_socket(sock)

        super(GeventTransport, self).connect((host, port), klass=_sslwrapper)

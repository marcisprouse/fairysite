from .signals import page_viewed_signal

class PageViewedMixin(object):
    def get_url(self, *args, **kwargs):
        context = super(PageViewedMixin, self).get_url(*args, **kwargs)
        request = self.request
        host = self.request.META['HTTP_HOST']
        path = self.request.META['REQUEST_URI']
        if host:
            page_viewed_signal.send(host=host, path=path, request=request)
        retval = {
            'context':context,
            'host':host,
            'path':path
            }
        return retval

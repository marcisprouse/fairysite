from django.dispatch import Signal

post_viewed_signal = Signal(providing_args=['post', 'request'])

page_viewed_signal = Signal(providing_args=['host', 'path', 'request'])
"""
ASGI config for safelock project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from channels.auth import AuthMiddlewareStack
from . import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'safelock.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter([
        re_path(r"practice", consumers.PracticeConsumer.as_asgi())
    ]))
})
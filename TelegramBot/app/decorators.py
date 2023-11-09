from django.shortcuts import redirect
from app.telegrambot import IsAuth
import asyncio

def telethon_login_requierd(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if asyncio.run(IsAuth()) == True:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("login")
    return _wrapped_view
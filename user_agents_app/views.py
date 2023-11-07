from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import HttpResponse


def index(req):
    return render(req, "user_agents_app/index.html")


def info_user_agent(req):
    user_agent = get_user_agent(req)
    return render(req, "user_agents_app/user_agent.html", {"info_user_agent": user_agent})


def get_agent(req):
    user_agent = get_user_agent(req)
    ip = req.META.get('REMOTE_ADDR')
    is_mobile = user_agent.is_mobile
    is_touch_capable = user_agent.is_touch_capable
    is_pc = user_agent.is_pc
    is_tablet = user_agent.is_tablet
    is_bot = user_agent.is_bot
    if is_mobile:
        text = 'El cliente es un telefono movil con ip: ' + ip
        if is_touch_capable:
            text += ' y el dispositivo es tactil'
        else:
            text += ' y el dispositivo no es tactil'

    elif is_pc:
        text = 'El cliente es un PC con ip: ' + ip
        if is_touch_capable:
            text += ' y el dispositivo es tactil'
        else:
            text += ' y el dispositivo no es tactil'

    elif is_tablet:
        text = 'El cliente es una Tablet con ip: ' + ip
        if user_agent.is_touch_capable:
            text += ' y el dispositivo es tactil'
        else:
            text += ' y el dispositivo no es tactil'


    elif is_bot:
        text = 'El cliente es un Bot con ip: ' + ip
        if is_touch_capable:
            text += ' y el dispositivo es tactil'
        else:
            text += ' y el dispositivo no es tactil'

    return render(req, "user_agents_app/info_device.html", {"text": text})

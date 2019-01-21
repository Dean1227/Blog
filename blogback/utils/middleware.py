import re

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import User


class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        path = request.path
        if path == '/':
            return None
        not_need_check = ['/user/register/', '/user/login/', '/media/.*', '/web/.*', '/static/.*']
        for check_path in not_need_check:
            if re.match(check_path, path):
                # 当前path路径为不需要做登录校验的路由
                return None
        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            request.user = user

        except Exception as e:
            return HttpResponseRedirect(reverse('user:login'))





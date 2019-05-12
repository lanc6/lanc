from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
   # TemplateView를 상속받을 때 template_name 클래스 변수 오버라이딩은 필수
    # 템플릿 파일의 이름을 지정하는데, 파일의 위치는 settings.TEMPLATES.DIRS 항목에서 정의함
    template_name = 'layout.html'

class login(TemplateView):
    template_name = 'registration/login.html'

class register(TemplateView):
    template_name = 'registration/register.html'

# 계정 등록                                         ch11 2/2
class UserCreateView(CreateView):
	# /accounts/register/ URL을 처리하는 뷰
	# 아래와 같이 중요한 속성만 지정하면, 그에 따라서 폼을 템플릿에 보여주고,
	# 입력 오류 검사 후, 입력한 내용으로 사용자 레코드를 생성하고,
	# 성공하면, success_url로 리다이렉트 시킴
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
	# User 생성이 성공하면 success_url 요청을 처리하는 뷰
	template_name = 'registration/register_done.html'


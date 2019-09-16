"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]  # path() 中的路由是一个字符串，用于定义要匹配的URL模式。该字符串可能包括一个命名变量（尖括号中）
"""URL 映射通过urlpatterns 变量管理，它是path() 函数的一个Python列表结构。 
每个path()函数要么将URL式样(URL pattern)关联到特定视图(specific view)，将在模式匹配时显示；要么关联到某个URL式样列表的测试代码。 
(第二种情况下，URL式样是目标模型里的“base URL”). 
urlpatterns 列表最开始定义了一个函数，这个函数将所有带有模型 admin/ 的URL映射到模块admin.site.urls。这个函数包含了Administration 应用自己的URL映射定义。"""
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/')),
]

urlpatterns += static(settings.STATIC_URL, documment_root=settings.STATIC_ROOT)
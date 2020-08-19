from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from ..products.models import *


# Create your views here.
def home(request):
    return render(request, 'calculator/home.html')


class BaaS_View(View, LoginRequiredMixin):
    template_name = 'calculator/main/baas.html'
    redirect_field_name = 'login'
    context = { }

    def get(self, request):
        if not request.user:
            redirect('login')
        baas = Riserva.objects.all().order_by('name')
        subscriptions = Subscriptions.objects.all()
        self.context.update({ 'baas': baas, 'subscriptions': subscriptions })
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        if request.POST.get('clear'):
            return redirect('pricing_baas')
        rq = int(request.POST.get('riserva'))
        riserva = Riserva.objects.get(pk=rq)
        cbq = int(request.POST.get('backup_tb'))
        cloud_backup_price = int(cbq * Subscriptions.objects.get(name='Per TB On Cloud').selling_price)
        bsq = int(request.POST.get('bandwidth_mb'))
        bandwidth_shared_price = int(bsq * Subscriptions.objects.get(name='Bandwidth').selling_price)
        total_per_month = int(riserva.selling_price + cloud_backup_price + bandwidth_shared_price)
        pricing = { 'total_per_month': total_per_month,
                    'nrc': 1999,
                    'total_12': total_per_month * 12 + 1999,
                    'total_36': total_per_month * 36 + 1999,
                    'riserva': int(riserva.selling_price),
                    'cloud_backup_price': cloud_backup_price,
                    'bandwidth_shared_price': bandwidth_shared_price }
        values = { 'riserva': riserva, 'cbq': str(cbq), 'bsq': str(bsq) }
        self.context = { 'pricing': pricing, 'values': values }
        return render(request, self.template_name, context=self.context)


class IaaS_View(View):
    template_name = 'calculator/main/iaas.html'
    redirect_field_name = 'login'
    login_url = 'login'
    context = { }

    def get(self, request):
        if not request.user.is_authenticated:
            redirect('login')
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        if request.POST.get('clear'):
            return redirect('pricing_iaas')
        values = request.POST
        iaas_products = list(IaaS.objects.all())
        draas_products = list(DRaaS.objects.all())
        all_products = iaas_products + draas_products
        pricing = dict(mrc=0)
        for i in request.POST.keys():
            for p in all_products:
                if i in pricing:
                    continue
                elif i == 'STD_2Core':
                    pricing[i] = int(round(IaaS.objects.get(name='SQL 2017 STD /2Core').selling_price *
                                           int(request.POST.get(i)), 0))
                    pricing['mrc'] += pricing[i]
                elif i in p.name:
                    pricing[i] = int(round(p.selling_price * int(request.POST.get(i)), 0))
                    pricing['mrc'] += pricing[i]
        pricing['bhas'] = int(pricing['mrc']*0.22)
        pricing['mrc'] += pricing['bhas']
        pricing.update(dict(total_1=pricing['mrc']*12 + 2999,
                            total_2=pricing['mrc']*24 + 2999,
                            total_3=pricing['mrc']*36 + 2999))
        self.context = { 'pricing': pricing, 'values': values }
        return render(request, self.template_name, context=self.context)

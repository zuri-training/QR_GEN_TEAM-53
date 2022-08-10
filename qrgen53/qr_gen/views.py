import io
from datetime import date, datetime

import segno
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect

from .forms import QrcodeCreate
from .models import QRcode

# Create your views here.

today = date.today()
now = datetime.now()


@login_required(login_url='login')
def qrcode_create_view(request):
    form = QrcodeCreate()
    if request.method == 'POST':
        form = QrcodeCreate(request.POST)
        if form.is_valid():
            owner = request.user.id
            base_url = form.cleaned_data['base_url']
            dark = form.cleaned_data['dark']
            light = form.cleaned_data['light']
            title = form.cleaned_data['title']
            type_qr = form.cleaned_data['type_qr']
            qrcode = segno.make_qr(base_url)  # TODO: create rule if QR is pdf, create jpeg by default and save both
            buff = io.BytesIO()
            qrcode.save(buff, kind=type_qr, light=light, dark=dark, scale=7)
            qr_code = QRcode(title=title, owner=owner, base_url=base_url,
                             type_qr=type_qr, light=light, dark=dark, )
            url_img = '/static/qrcodes/' + title + '.' + type_qr
            created = True
            t2 = title + '.' + type_qr
            qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)
            context = {
                'form': form,
                'url_img': url_img,
                'created': created
            }

            """if request.user not in database
                OwnerCreate.objects.create(request.user.id)
            else:
                AddOwner.up
            # qr_form.save()
            # qr_form = QrcodeCreate()"""
            return render(request, 'qr_create.html', context)
            # return send_
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'qr_create.html', context)


@login_required(login_url='login')
def qrcode_gallery_view(request):
    queryset = QRcode.objects.all()  # list of objects
    # TODO: add functionality for when the qr code gallery is empty
    context = {
        "object_list": queryset
    }
    return render(request, 'qr_gallery.html', context)


@login_required(login_url='login')
def qrcode_detail_dy_view(request, qr_id):
    # TODO: apply this
    # obj = QRcode.objects.get(id=qr_id)
    obj = get_object_or_404(QRcode, id=qr_id)
    location = '/' + str(obj.qrcode)
    context = {
        'owner': request.user,
        'title': obj.title,
        'date': obj.date_created,
        'url': obj.base_url,
        'type': obj.type_qr,
        'stats': obj.stats,
        'qrcode': obj.qrcode,
        'location': location
    }
    return render(request, 'qr_detail.html', context)


@login_required(login_url='login')
def qrcode_delete_view(request, qr_id):
    obj = get_object_or_404(QRcode, id=qr_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'qr_delete.html', context)


@login_required(login_url='login')
def dashboard_view(request):
    username = request.user
    """total_codes = request.user.qr_total
    total_clicks = request.user.click_total
    active_codes = request.user.active_codes"""
    context = {
        'username': username,
        'date': today.strftime("%B %d, %Y"),
        'time': now.strftime("%H:%M"),
    }
    """ 'total_codes': total_codes,  # TODO: add total QRcodes field to user model
        'total_clicks': total_clicks,  # TODO: add total clicks field to user model
        'active_codes': active_codes,  # TODO: add total active field to user model
        'inactive_codes': (total_codes - active_codes) """
    return render(request, "dashboard-main.html", context)


@login_required(login_url='login')
def dashboard_other_view(request):
    username = request.user
    context = {
        'username': username
    }
    return render(request, "dashboard-other.html", context)


@login_required(login_url='login')
def analytics_view(request):
    username = request.user
    context = {
        'username': username
    }
    return render(request, 'analytics-page.html', context)


@login_required(login_url='login')
def setting_view(request):
    username = request.user
    context = {
        'username': username
    }
    return render(request, "settings.html", context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return render(request, 'index.html')


"""

    initial_data = {
        'light': 'white',
        'dark' : 'black'
    }
    qr_form = QrcodeCreate(request.POST, initial=initial_data)
"""

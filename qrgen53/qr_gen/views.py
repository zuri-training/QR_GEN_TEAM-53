import io
import mimetypes
from datetime import date, datetime
from pathlib import Path

import segno
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from segno import helpers

from .forms import QrcodeCreate, QrcodeLocationCreate, QrcodeEmailCreate, QrcodeWifiCreate
from .models import QRcode, QRcodeEmail, QRcodeWifi

# Create your views here.

today = date.today()
now = datetime.now()
BASE_DIR = Path(__file__).resolve().parent.parent


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
            title = form.cleaned_data['title'].replace(' ', '_')
            type_qr = form.cleaned_data['type_qr']
            tag = form.cleaned_data['tag']
            qrcode = segno.make_qr(base_url)  # TODO: create rule if QR is pdf, create jpeg by default and save both
            if tag == 'jpg':
                img = qrcode.to_pil(light=light, dark=dark, scale=7)
                buff = io.BytesIO()
                img.save(buff, format='jpeg')

            else:
                buff = io.BytesIO()
                qrcode.save(buff, kind=tag, light=light, dark=dark, scale=7)

            qr_code = QRcode(title=title, owner=owner, base_url=base_url,
                             type_qr=type_qr, light=light, dark=dark, tag=tag,
                             )
            url_img = '/media/media/' + title + '.' + tag
            url_down = ''
            created = True
            if tag != 'pdf':
                url_down = url_img
                t2 = title + '.' + tag
                qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)
            else:
                t2 = title + '.pdf'
                qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)

                b2 = io.BytesIO()
                qrcode.save(b2, kind='png', light=light, dark=dark, scale=7)
                q_code = QRcode(title=title, owner=owner, base_url=base_url,
                                type_qr=type_qr, light=light, dark=dark, tag='png',
                                )
                t3 = title + '.png'
                q_code.qrcode.save(t3, ContentFile(b2.getvalue()), save=True)

                url_img = '/media/media/' + title + '.png'
                url_down = '/media/media/' + title + '.pdf'
            print(url_down)

            context = {
                'form': form,
                'url_img': url_img,
                'created': created,
                'url_down': url_down,
                'username': request.user,
                'name': t2,
            }
            return render(request, 'qr_create.html', context)
        else:
            print(form.errors)

    context = {
        'form': form,
        'username': request.user
    }
    return render(request, 'qr_create.html', context)


@login_required(login_url='login')
def qrcode_wifi_view(request):
    form = QrcodeWifiCreate()
    if request.method == 'POST':
        form = QrcodeWifiCreate(request.POST)
        if form.is_valid():
            owner = request.user.id
            title = form.cleaned_data['title'].replace(' ', '_')
            ssid = form.cleaned_data['ssid']
            password = form.cleaned_data['password']
            security = form.cleaned_data['security']
            dark = form.cleaned_data['dark']
            light = form.cleaned_data['light']
            tag = form.cleaned_data['tag']
            qrcode = helpers.make_wifi(ssid, password, security)
            qrcode.save(title + '.' + tag, scale=7)
            if tag == 'jpg':
                img = qrcode.to_pil(light=light, dark=dark, scale=7)
                buff = io.BytesIO()
                img.save(buff, format='jpeg')

            else:
                buff = io.BytesIO()
                qrcode.save(buff, kind=tag, light=light, dark=dark, scale=7)

            qr_code = QRcodeWifi(title=title, owner=owner, ssid=ssid, password=password, security=security,
                                 light=light, dark=dark, tag=tag, )
            url_img = '/media/media/' + title + '.' + tag
            url_down = ''
            created = True
            if tag != 'pdf':
                url_down = url_img
                t2 = title + '.' + tag
                qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)
            else:
                t2 = title + '.pdf'
                qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)

                b2 = io.BytesIO()
                qrcode.save(b2, kind='png', light=light, dark=dark, scale=7)
                q_code = QRcode(title=title, owner=owner, ssid=ssid, password=password, security=security,
                                light=light, dark=dark, tag='png',
                                )
                t3 = title + '.png'
                q_code.qrcode.save(t3, ContentFile(b2.getvalue()), save=True)

                url_img = '/media/media/' + title + '.png'
                url_down = '/media/media/' + title + '.pdf'
            print(url_down)

            context = {
                'form': form,
                'url_img': url_img,
                'created': created,
                'url_down': url_down,
                'username': request.user,
                'name': t2,
            }
            return render(request, 'create-wifi-qr.html', context)
        else:
            print(form.errors)

    context = {
        'form': form,
        'username': request.user
    }
    return render(request, 'create-wifi-qr.html', context)


@login_required(login_url='login')
def qrcode_location_view(request):
    form = QrcodeLocationCreate()
    if request.method == 'POST':
        form = QrcodeLocationCreate(request.POST)
        if form.is_valid():
            owner = request.user.id
            title = form.cleaned_data['title'].replace(' ', '_')
            long = form.cleaned_data['long']
            lat = form.cleaned_data['lat']
            dark = form.cleaned_data['dark']
            light = form.cleaned_data['light']
            tag = form.cleaned_data['tag']
            qrcode = helpers.make_geo(lat=lat, lng=long)
            qrcode.save(title + '.' + tag, scale=7)
            if tag == 'jpg':
                img = qrcode.to_pil(light=light, dark=dark, scale=7)
                buff = io.BytesIO()
                img.save(buff, format='jpeg')

            else:
                buff = io.BytesIO()
                qrcode.save(buff, kind=tag, light=light, dark=dark, scale=7)

            qr_code = QRcodeWifi(title=title, owner=owner, long=long, lat=lat,
                                 light=light, dark=dark, tag=tag, )
            url_img = '/media/media/' + title + '.' + tag
            url_down = ''
            created = True
            if tag != 'pdf':
                url_down = url_img
                t2 = title + '.' + tag
                qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)
            else:
                t2 = title + '.pdf'
                qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)

                b2 = io.BytesIO()
                qrcode.save(b2, kind='png', light=light, dark=dark, scale=7)
                q_code = QRcode(title=title, owner=owner, long=long, lat=lat,
                                light=light, dark=dark, tag='png',
                                )
                t3 = title + '.png'
                q_code.qrcode.save(t3, ContentFile(b2.getvalue()), save=True)

                url_img = '/media/media/' + title + '.png'
                url_down = '/media/media/' + title + '.pdf'
            print(url_down)

            context = {
                'form': form,
                'url_img': url_img,
                'created': created,
                'url_down': url_down,
                'username': request.user,
                'name': t2,
            }
            return render(request, 'create-location-qr.html', context)
        else:
            print(form.errors)

    context = {
        'form': form,
        'username': request.user
    }
    return render(request, 'create-location-qr.html', context)


@login_required(login_url='login')
def qrcode_email_view(request):
    form = QrcodeEmailCreate()
    if request.method == 'POST':
        form = QrcodeEmailCreate(request.POST)
        if form.is_valid():
            owner = request.user.id
            title = form.cleaned_data['title'].replace(' ', '_')
            to = form.cleaned_data['to']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            dark = form.cleaned_data['dark']
            light = form.cleaned_data['light']
            tag = form.cleaned_data['tag']
            qrcode = helpers.make_email(to=to, subject=subject, body=body)
            qrcode.save(title + '.' + tag, scale=7)
            if tag == 'jpg':
                img = qrcode.to_pil(light=light, dark=dark, scale=7)
                buff = io.BytesIO()
                img.save(buff, format='jpeg')

            else:
                buff = io.BytesIO()
                qrcode.save(buff, kind=tag, light=light, dark=dark, scale=7)

            qr_code = QRcodeEmail(title=title, owner=owner, to=to, subject=subject, body=body,
                                  light=light, dark=dark, tag=tag, )
            url_img = '/media/media/' + title + '.' + tag
            url_down = ''
            created = True
            if tag != 'pdf':
                url_down = url_img
                t2 = title + '.' + tag
                qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)
            else:
                t2 = title + '.pdf'
                qr_code.qrcode.save(t2, ContentFile(buff.getvalue()), save=True)

                b2 = io.BytesIO()
                qrcode.save(b2, kind='png', light=light, dark=dark, scale=7)
                q_code = QRcode(title=title, owner=owner, to=to, subject=subject, body=body,
                                light=light, dark=dark, tag='png', )
                t3 = title + '.png'
                q_code.qrcode.save(t3, ContentFile(b2.getvalue()), save=True)

                url_img = '/media/media/' + title + '.png'
                url_down = '/media/media/' + title + '.pdf'
            print(url_down)

            context = {
                'form': form,
                'url_img': url_img,
                'created': created,
                'url_down': url_down,
                'username': request.user,
                'name': t2,
            }
            return render(request, 'create-email-qr.html', context)
        else:
            print(form.errors)

    context = {
        'form': form,
        'username': request.user
    }
    return render(request, 'create-email-qr.html', context)


def download_file_view(request, filename=''):
    if filename != '':
        # filepath = BASE_DIR + '/media/media/' + filename
        filepath = str(BASE_DIR) + "\\media\\media\\" + filename
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        form = QrcodeCreate()
        context = {
            'form': form,
            'username': request.user
        }
        return render(request, 'qr_create.html', context)


@login_required(login_url='login')
def qrcode_gallery_view(request):
    userid = request.user.id
    queryset = QRcode.objects.filter(owner=userid)  # list of objects
    # TODO: add functionality for when the qr code gallery is empty
    if queryset.exists():

        context = {
            "object_list": queryset,
            'username': request.user,
        }
        return render(request, 'qr_gallery.html', context)
    else:
        context = {
            'username': request.user,
        }
        return render(request, 'qr_empty_gallery.html', context)


@login_required(login_url='login')
def qrcode_detail_dy_view(request, qr_id):
    # TODO: apply this
    # obj = QRcode.objects.get(id=qr_id)
    obj = get_object_or_404(QRcode, id=qr_id)
    location = '/media/' + str(obj.qrcode)
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
        'username': username,
        'date': today.strftime("%B %d, %Y"),
        'time': now.strftime("%H:%M"),
    }
    return render(request, 'analytics-page.html', context)


@login_required(login_url='login')
def setting_view(request):
    username = request.user
    context = {
        'username': username
    }
    return render(request, "settings.html", context)

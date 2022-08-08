from django.shortcuts import render, get_object_or_404, redirect
from .models import QRcode
from .forms import QrcodeCreate
from django.contrib.auth.decorators import login_required, permission_required


# from .qr import *

# Create your views here.

@ login_required(login_url='login')
def qrcode_gallery_view(request):
    queryset = QRcode.objects.all()  # list of objects
    # TODO: add functionality for when the qr code gallery is empty
    context = {
        "object_list": queryset
    }
    return render(request, 'qr_gen/qr_gallery.html', context)


@ login_required(login_url='login')
def qrcode_detail_dy_view(request, qr_id):
    # TODO: apply this
    # obj = QRcode.objects.get(id=qr_id)
    obj = get_object_or_404(QRcode, id=qr_id)
    context = {
        'title': obj.title,
        'date': obj.date_created,
        'url': obj.base_url,
        'type': obj.type_qr,
        'stats': obj.stats
    }
    return render(request, 'qr_gen/qr_detail.html', context)


@ login_required(login_url='login')
def qrcode_create_view(request):
    qr_form = QrcodeCreate()
    if request.method == "POST":
        qr_form = QrcodeCreate(request.POST)
        if qr_form.is_valid():
            QRcode.objects.create(**qr_form.cleaned_data)
            qr_form = QrcodeCreate()
            # qr_form.save()
            # qr_form = QrcodeCreate()
        else:
            print(qr_form.errors)

    context = {'form': qr_form}
    return render(request, 'qr_gen/qr_create.html', context)


@ login_required(login_url='login')
def qrcode_delete_view(request, qr_id):
    obj = get_object_or_404(QRcode, id=qr_id)
    if request.method == "POST":
        # method above confirms delete
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "qr_gen/qr_delete.html", context)


"""
    initial_data = {
        'light': 'white',
        'dark' : 'black'
    }
    qr_form = QrcodeCreate(request.POST, initial=initial_data)
"""

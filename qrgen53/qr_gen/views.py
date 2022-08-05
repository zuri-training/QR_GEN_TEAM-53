from django.shortcuts import render
from .models import QRcode
from .forms import QrcodeCreate


# Create your views here.


def qrcode_detail_view(request):
    # TODO: apply this

    obj = QRcode.objects.get(id=3)
    context = {
        'title': obj.title,
        'date': obj.date_created,
        'url': obj.base_url,
        'type': obj.type_qr,
        'stats': obj.stats
    }
    return render(request, 'qr_gen/qr_detail.html', context)


def qrcode_create_view(request):
    form = QrcodeCreate(request.POST)
    if form.is_valid():
        form.save()
        form = QrcodeCreate()

    context = {'form': form}
    return render(request, 'qr_gen/qr_create.html', context)
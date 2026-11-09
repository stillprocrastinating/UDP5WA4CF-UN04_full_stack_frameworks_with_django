from django.shortcuts import render


def lessons_view(request):

    subscription = {
        'class_1': 'price_1Ua1kQ643VTaWZ4DNJTNGVbw',
        'class_2': 'price_1Ua1gm643VTaWZ4DAcFsZM52',
        'class_3': 'price_1Ua1lt643VTaWZ4DlP6TPOQC',
        'class_4': 'price_1Ua1nZ643VTaWZ4DbAk2OnNm',
        'class_8': 'price_1Ua1vy643VTaWZ4DUzppEGWk'
    }

    context = {'subscription': subscription}

    return render(request, 'lessons/lessons.html', context)

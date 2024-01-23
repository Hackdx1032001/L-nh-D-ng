from urllib import request
from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.


def chiller_view(request):
    # Lấy dữ liệu nhiệt độ chiller từ cơ sở dữ liệu
    chiller_data = [
        {
            "id": 1,
            "temperature": 25,
            "status": "on"
        },
        {
            "id": 2,
            "temperature": 26,
            "status": "off"
        },
        {
            "id": 3,
            "temperature": 27,
            "status": "on"
        },
        {
            "id": 4,
            "temperature": 28,
            "status": "off"
        }
    ]

    # Tạo template HTML
    template_name = "chiller.html"
    context = {
        "chiller_data": chiller_data
    }
    return render(request, template_name, context)



def chiller_set_temperature(request, chiller_data):
    # Lấy giá trị nhiệt độ đặt từ request
    
    temperature = request.POST.get("temperature")

    # Cập nhật trạng thái chiller
    for chiller in chiller_data:
        chiller.temperature = temperature

    # Lưu trạng thái chiller mới vào cơ sở dữ liệu
    chiller_model.objects.bulk_update(chiller_data)

    # Trả về phản hồi JSON
    return JsonResponse({"success": True})

chiller_data = chiller_view(request)
chiller_set_temperature(request, chiller_data)
from django.db import models

# Create your models here.
from parameter.models import parameter

class query_temp(parameter):
    
    # Hàm tính toán hoặc xử lý dữ liệu từ kết quả truy vấn
    def calculate_result_from_queryset(queryset):
        
        
        average_value = queryset.aggregate(models.Avg('Temperature'))['temperature__avg']
        return average_value
    
    # Hàm thực hiện truy vấn CSDL Django
calculator = calculate_result_from_queryset(queryset)
def fitness_function(query_params):
    
    queryset = query_temp.objects.filter(**query_params)

    
    result_value = calculate_result_from_queryset(queryset)

    return result_value
    
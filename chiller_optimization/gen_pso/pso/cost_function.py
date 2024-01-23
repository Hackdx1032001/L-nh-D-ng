from parameter.views import readtemp

ip_address = '192.168.0.1'
db_number = 1
ct_out_address = 9
ch_in_address = 10
m = 3
c = 4.91
def sphere(x):
    diff_temp_value=readtemp(ip_address,db_number, ct_out_address, ch_in_address)
    power = diff_temp_value*m*c
    return power
if __name__ == "pso.sphere":
    sphere()
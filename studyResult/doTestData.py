def do_text_data():

    filename = r'C:\Users\Administrator\Desktop\test.txt'
    mobile_phone = 15000000000
    a = 0
    with open(filename,'w') as file_object:
        while a < 10000:
            file_object.write(str(mobile_phone)+' login'+'\n')
            file_object.write(str(mobile_phone)+' mp_material'+'\n')
            file_object.write(str(mobile_phone)+' mp_product'+'\n')
            file_object.write(str(mobile_phone)+' mp_shop'+'\n')
            mobile_phone += 1
            a += 1

do_text_data()
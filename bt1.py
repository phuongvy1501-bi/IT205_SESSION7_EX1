import random
is_running = True
raw_input = input("nhập chuỗi dữ liệu gốc: ")
info = raw_input.strip().split(";")            
birth_year = int(info[1])
full_name = info[0]
while is_running:
    print("==== HỆ THỐNG XỬ LÝ THÀNH VIÊN ====")
    print("1.Hiển thị chuỗi dữ liệu gốc")
    print("2.Chuẩn hóa họ tên và tính tuổi")
    print("3.Tạo mã ID và Email tự động")
    print("4.Thoát chương trình")
    print("="* 10)
    choice = int(input("nhập vào lựa chọn của bạn: "))
    match choice:
        case 1:
            print(f"Chuỗi dữ liệu gốc là: {raw_input}")
            
        case 2:
            print(f"Họ và tên: {full_name.strip().title()}")
            print(f"Tuổi hiện tại: {2026 - birth_year}")                                        
        
        case 3:
            email = ""
            name = full_name.strip().split(" ")
            id = name[len(name) - 1].upper()
            id += f"{random.randint(10,99)}"
            for i in range(len(name)):
                if i+1 >= len(name):
                    email += name[i]
                else:
                    email += name[i][0]
            email += "@gmail.com"
            print(f"Họ và tên: {full_name.strip().title()}")
            print(f"Tuổi hiện tại: {2026 - birth_year}")
            print(f"ID: {id}")
            print(f"Email: {email}")
        case 4:
            is_running = False
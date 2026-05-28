#input
# mã: string
# nhiệt độ: float
# nhịp tim: int

# 1: ep kiểu trực tiếp khi nhập
    # chuyển kiểu ngay khi nhập
    # ko cần biến trung gian
    # dễ đọc, ít biến, ngắn gọn, kho kiểm tra dữ liệu lỗi
# 2: nhập chuỗi trước, ép kiểu sau
    # lưu dữ liệu gốc trước khi ép kiểu
    # dài hơn, dễ kiểm tra dữ liệu nhập
    
# chọn 2, vì: dữ liệu bệnh nhân cần độ chính xác cao, cần kiểm tra lỗi nhập liệu

patient_id = input("Nhập mã bệnh nhân: ")
temp_input = input("Nhập nhiệt độ cơ thể: ")
heart_input = input("Nhập nhịp tim: ")

temperature = float(temp_input)
heart_rate = int(heart_input)
print(f"Mã bệnh nhân: {patient_id}")
print(f"Nhiệt độ cơ thể: {temperature} độ C")
print("Kiểu dữ liệu hệ thống ghi nhận:", type(temperature))
print(f"Nhịp tim: {heart_rate} nhịp/phút")
print("Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))

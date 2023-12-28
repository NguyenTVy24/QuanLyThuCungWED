# Đồ án kết thúc môn học
## Thành viên tham gia
- 2051220169 Nguyễn Quốc Cường
- 2051220067 Nguyên Ngô Hoàng Vũ
- 2051220068 Nguyễn Thành Vỹ
## Mục đích tranh web
- Định danh thú cưng
- Giúp người dùng xác thực thông tin của thú cưng
- Truy xuất nguồn gốc của thú cưng
## Cấu Trúc Đối Tượng Thú Cưng
- Tên Pet: name_pet = models.CharField(max_length=200) 
- Ngày Sinh: day_of_birth = models.DateTimeField()
- Giới Tính: sex = models.BooleanField(default=0)
- Giống: animal_type = models.CharField(max_length=200)
- Hình Ảnh Pet: pet_image = models.ImageField(default="")
## test thêm data 

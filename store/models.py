from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS_CHOICES = (
    ("Pending", "Chờ xử lý"),
    ("Accepted", "Đã chấp nhận"),
    ("Packed", "Đã đóng gói"),
    ("On The Way", "Đang vận chuyển"),
    ("Delivered", "Đã giao hàng"),
    ("Cancelled", "Đã hủy"),
)


class TimeBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    class Meta:
        abstract = True


class StatusBaseModel(models.Model):
    is_active = models.BooleanField(verbose_name="Hoạt động?")
    is_featured = models.BooleanField(verbose_name="Nổi bật?")

    class Meta:
        abstract = True


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    locality = models.CharField(max_length=150, verbose_name="Nearest Location")
    city = models.CharField(max_length=150, verbose_name="City")
    state = models.CharField(max_length=150, verbose_name="State")

    class Meta:
        verbose_name_plural = "Địa chỉ"

    def __str__(self):
        return self.locality


class Category(TimeBaseModel, StatusBaseModel):
    title = models.CharField(max_length=50, verbose_name="Tiêu đề")
    slug = models.SlugField(max_length=55, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    category_image = models.ImageField(
        upload_to="category", blank=True, null=True, verbose_name="Ảnh"
    )

    class Meta:
        verbose_name_plural = "Danh mục"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class Product(TimeBaseModel, StatusBaseModel):
    title = models.CharField(max_length=150, verbose_name="Tiêu đề")
    slug = models.SlugField(max_length=160, verbose_name="Slug")
    sku = models.CharField(max_length=255, unique=True, verbose_name="SKU")
    short_description = models.TextField(verbose_name="Mô tả ngắn gọn")
    detail_description = models.TextField(
        blank=True, null=True, verbose_name="Mô tả chi tiết"
    )
    product_image = models.ImageField(
        upload_to="product", blank=True, null=True, verbose_name="Ảnh"
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category, verbose_name="Danh mục sản phẩm", on_delete=models.CASCADE
    )
    view = models.IntegerField(default=0, verbose_name="Lượt xem sản phẩm")
    class Meta:
        verbose_name_plural = "Sản phẩm"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class Cart(TimeBaseModel):
    user = models.ForeignKey(User, verbose_name="Người dùng", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name="Sản phẩm", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Số lượng")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Giỏ hàng"

    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="Người dùng", on_delete=models.CASCADE)
    address = models.ForeignKey(
        Address, verbose_name="Địa chỉ", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, verbose_name="Sản phẩm", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(verbose_name="Số lượng")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đặt hàng")
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default="Pending")

    class Meta:
        verbose_name_plural = "Đơn hàng"

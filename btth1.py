   
inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def process_sale(quantity, sell):
    global inventory_stock
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return 0
    discount = (quantity * sell)
    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${sell:.1f}")
    print(f"Tạm tính: ${discount:1f}")
    if discount >= 1000:
        discount *= 0.1
        print(f"Giảm giá (10%): ${discount}")
    vat = ((quantity * sell) * 0.9) * 0.08

    print(f"Thuế VAT (8%): ${vat:.1f}")
    final_total = ((quantity * sell) * 0.9) * 1.08
    print(f"Tổng thanh toán: ${final_total:.1f}")
    print("Đã bán thành công!")

    return final_total


def print_report(stock, revenue):
    print(f"""
Tồn kho hiện tại: {stock} sản phẩm
Tổng doanh thu: ${revenue:1f}
""")

while True:
    print("""
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
""")
    while True:
        try:
            choice = int(input("Chọn chức năng (1-4): "))
            if choice >= 1 and choice <= 4:
                break
            else:
                print("Chọn từ 1 - 5")
        except ValueError:
            print("Chọn từ 1 - 5")
    match choice:
        case 1:
            print("--- NHẬP HÀNG ---")
            while True:
                try:
                    amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
                    if amount > 0 :
                        break
                    else:
                        print("số lượng sản phẩm phải lớn hơn 0!")
                except ValueError:
                    print("số lượng sản phẩm phải lớn hơn 0!")
            add_stock(amount)
        case 2:
            print("--- BÁN HÀNG ---")
            while True:
                try:
                    quantity = int(input("Nhập số lượng mua: "))
                    if quantity > 0 :
                        break
                    else:
                        print("số lượng mua phải lớn hơn 0!")
                except ValueError:
                    print("số lượng mua phải lớn hơn 0!")
            while True:
                try:
                    sell = float(input("Nhập đơn giá ($): "))
                    if sell > 0 :
                        break
                    else:
                        print("đơn giá phải lớn hơn 0!")
                except ValueError:
                    print("đơn giá phải lớn hơn 0!")
            total_revenue += process_sale(quantity, sell)
        case 3:
            print("--- BÁO CÁO KINH DOANH ---")
            print_report(inventory_stock, total_revenue)
        case 4:
            break
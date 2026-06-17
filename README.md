# 🧩 Block Blast — Xây dựng game Block Blast sử dụng thư viện Pygame

> Bài tập nhóm môn **Lập trình Python** — Nhóm 7, Lớp CTK47MMT  
> Trường Đại học Đà Lạt, Khoa Công nghệ Thông tin

---

## 📖 Giới thiệu

**Block Blast** là một trò chơi giải đố xếp hình 2D được xây dựng bằng ngôn ngữ Python với thư viện đồ họa Pygame. Người chơi kéo-thả các khối hình học vào một lưới 8×8, cố gắng lấp đầy các hàng và cột để ghi điểm cao nhất có thể.

---

## ✨ Tính năng

- 🎮 **Lưới chơi 8×8** với giao diện bo viền hiện đại
- 🟦 **20+ loại khối** đa dạng: 1×1, 2×2, chữ I, L, J, T, Z, vuông 3×3...
- 🎨 **Màu sắc ngẫu nhiên** mỗi ván chơi
- 🖱️ **Kéo-thả bằng chuột** mượt mà với hiệu ứng phóng to khi kéo
- 💥 **Tự động xóa hàng/cột** khi được lấp đầy hoàn toàn
- 🏆 **Hệ thống tính điểm** — 10 điểm/ô đặt, 100 điểm/hàng hoặc cột bị xóa
- 💀 **Phát hiện Game Over** tự động khi không còn nước đi hợp lệ
- 🔄 **Chơi lại** ngay lập tức bằng phím `R`

---

## 🚀 Cài đặt và Chạy

### Yêu cầu hệ thống

- Python **3.x** trở lên
- Thư viện **Pygame**

### Các bước thực hiện

**1. Clone repo về máy**

```bash
git clone https://github.com/NLBLonk/Python_BlockBlast.git
cd Python_BlockBlast
```

**2. Cài đặt thư viện Pygame**

```bash
pip install pygame
# macOS / Linux dùng:
pip3 install pygame
```

**3. Chạy game**

```bash
python main.py
# macOS / Linux dùng:
python3 main.py
```

Cửa sổ game có tên **"Bờ lóc bờ lát (Block Blast)"** sẽ xuất hiện — bắt đầu chơi thôi! 🎉

---

## 🕹️ Cách chơi

| Thao tác | Mô tả |
|---|---|
| **Click + Giữ** vào khối | Chọn và kéo khối lên lưới |
| **Thả chuột** | Đặt khối xuống vị trí hợp lệ |
| Thả vào vị trí **không hợp lệ** | Khối tự động quay về khay |
| Lấp đầy **hàng ngang / cột dọc** | Hàng/cột biến mất, +100 điểm |
| Nhấn **`R`** (khi Game Over) | Chơi lại từ đầu |

---

## 🗂️ Cấu trúc mã nguồn

```
Python_BlockBlast/
├── main.py          # Logic chính — lớp Block & Game, vòng lặp game
├── shapes_data.py   # Cấu hình hằng số, bảng màu và dữ liệu hình khối
└── README.md
```

### `shapes_data.py`
File cấu hình trung tâm: định nghĩa kích thước màn hình, lưới, màu sắc và toàn bộ 20+ hình khối dưới dạng danh sách các tuple tọa độ tương đối `(dx, dy)`.

### `main.py`
Được thiết kế theo **Lập trình hướng đối tượng (OOP)** với 2 lớp:

- **`Block`** — Quản lý từng khối gạch: vị trí, kích thước, trạng thái kéo thả, và render.
- **`Game`** — Bộ não của toàn hệ thống: vòng lặp game 60 FPS, xử lý sự kiện chuột, thuật toán xóa hàng/cột, kiểm tra Game Over, và vẽ giao diện.

---

## 👨‍💻 Thành viên nhóm

| MSSV | Họ và tên |
|---|---|
| 2312604 | Phạm Thái Ngọc Duy |
| 2312606 | Cil Ha Ly Gơs |
| 2312678 | Nguyễn Lê Bảo Long |

**Giảng viên hướng dẫn:** ThS. Đoàn Minh Khuê  
**Trường:** Đại học Đà Lạt — Khoa CNTT  

---

## 📜 Giấy phép

Dự án được thực hiện phục vụ mục đích học tập.

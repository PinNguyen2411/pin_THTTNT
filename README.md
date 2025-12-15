## Giới thiệu chung
Repository này chứa mã nguồn cài đặt 3 thuật toán AI cốt lõi, được viết bằng Python theo phong cách Hướng đối tượng (OOP). Mục tiêu là tối ưu hóa thuật toán, hỗ trợ nhập liệu động (Dynamic Input) và xây dựng ứng dụng thực tế.

---

## 1. Phân loại dữ liệu (K-Nearest Neighbors - KNN)

###  Giải thích Code
* **Class `KNNClassifier`**: Quản lý tập dữ liệu huấn luyện và thực hiện dự đoán.
* **Hàm `predict(new_point, k)`**:
    * **Bước 1 (Khoảng cách):** Tính khoảng cách Euclidean từ điểm mới đến tất cả điểm cũ theo công thức Py-ta-go $\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$.
    * **Bước 2 (Lân cận):** Sắp xếp khoảng cách tăng dần và lấy ra **K** người hàng xóm gần nhất.
    * **Bước 3 (Bầu chọn):** Dùng cơ chế Voting. Nhãn nào xuất hiện nhiều nhất trong K hàng xóm sẽ là kết quả cuối cùng.

###  Ứng dụng thực tế: Gợi ý Size quần áo
* **Bài toán:** Khách hàng nhập chiều cao, cân nặng -> Hệ thống gợi ý nên mua áo size S, M hay L.
* **Ánh xạ:** Dữ liệu mẫu là lịch sử mua hàng của khách cũ. Điểm mới là khách hàng hiện tại.

###  Kịch bản Demo
1. **Case 1 (K nhỏ):** Nhập K=1. Kết quả rất nhạy cảm, chỉ cần 1 người gần nhất lạ thường là kết quả đổi ngay.
2. **Case 2 (K ổn định):** Nhập K=5. Máy tham khảo ý kiến số đông -> Kết quả chính xác hơn.
3. **Case 3 (Input động):** Nhập chiều cao/cân nặng bất kỳ từ bàn phím để xem máy phân loại Nam hay Nữ.

---

## 2. Thuật toán Tô màu đồ thị (Graph Coloring)

###  Giải thích Code
* **Class `GraphColoring`**: Quản lý đồ thị và thực hiện tô màu tham lam (Greedy).
* **Hàm `solve(max_colors)`**:
    * **Bước 1 (Heuristic):** Ưu tiên xử lý các đỉnh có nhiều kết nối (bậc cao) trước để giảm thiểu xung đột.
    * **Bước 2 (Greedy):** Duyệt qua từng đỉnh, tìm màu "nhỏ nhất" (0, 1, 2...) chưa bị hàng xóm sử dụng.
    * **Bước 3 (Visualizer):** Sử dụng thư viện `networkx` để vẽ trực quan kết quả ra màn hình.

###  Ứng dụng thực tế: Xếp lịch thi / Lịch họp
* **Bài toán:** Xếp lịch sao cho các môn thi chung sinh viên không bị trùng giờ.
* **Ánh xạ:** Đỉnh = Môn thi; Cạnh nối = Có sinh viên thi cả 2 môn; Màu = Ca thi.
* **Ý nghĩa:** Số màu ít nhất = Số ca thi tối thiểu cần tổ chức.

###  Kịch bản Demo
1. **Case 1 (Tối ưu):** Nhập 3 đỉnh nối vòng tròn -> Máy tự động dùng **3 màu**.
2. **Case 2 (Thiếu màu):** Ép chỉ cho dùng 2 màu cho đồ thị tam giác -> Code báo **"Không thể tô màu"**.
3. **Case 3 (Phức tạp):** Nhập đồ thị nhiều cạnh ngẫu nhiên -> Máy vẽ hình minh họa các đỉnh không trùng màu nhau.

---

## 3. Game Tic-Tac-Toe / Caro (Minimax + Depth Limit)

###  Giải thích Code
* **Class `TicTacToe`**: Quản lý bàn cờ $N \times N$ linh hoạt (không chỉ 3x3).
* **Hàm `minimax(depth, is_max, max_depth)`**:
    * **Minimax:** Đệ quy thử nước đi. Máy (Max) muốn điểm cao nhất (+10), Người (Min) muốn điểm thấp nhất (-10).
    * **Dynamic Size:** Sử dụng mảng 1 chiều để xử lý bàn cờ kích thước bất kỳ do người dùng nhập.
    * **Depth Limit (Giới hạn độ sâu):**
        * Nếu bàn cờ nhỏ (3x3): Máy tính toán toàn bộ nước đi (Bất bại).
        * Nếu bàn cờ lớn ($N \ge 4$): Máy chỉ tính trước vài nước (như người thật) để tránh treo máy.

###  Ứng dụng thực tế: Hệ thống chiến thuật
* **Bài toán:** Xây dựng đối thủ ảo trong game hoặc hệ thống hỗ trợ ra quyết định trong môi trường đối kháng.
* **Nguyên lý:** Luôn giả định đối thủ sẽ đi nước hay nhất để tìm phương án đối phó an toàn nhất.

###  Kịch bản Demo
1. **Input động:** Nhập kích thước bàn cờ (ví dụ 3x3 hoặc 5x5) ngay khi chạy.
2. **Chặn nước thắng:** Người chơi sắp tạo thành đường thẳng -> Máy tự động đánh chặn đầu.
3. **Xử lý tọa độ:** Người dùng nhập Hàng/Cột, máy tự quy đổi sang chỉ số mảng để xử lý.

import math
from collections import Counter

class KNNClassifier:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def euclidean_distance(self, point1, point2):
        # Tính khoảng cách Euclidean: sqrt((x2-x1)^2 + (y2-y1)^2)
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

    def predict(self, new_point, k):
        # 1. Tính khoảng cách từ điểm mới đến tất cả các điểm trong data
        distances = [] 
        for i in range(len(self.data)):
            dist = self.euclidean_distance(new_point, self.data[i])
            distances.append((dist, self.labels[i]))

        # 2. Sắp xếp theo khoảng cách tăng dần và lấy K điểm gần nhất
        k_nearest = sorted(distances, key=lambda x: x[0])[:k]

        # 3. Lấy nhãn của K điểm đó
        k_labels = [label for _, label in k_nearest]

        # 4. Bầu chọn (Voting) - Nhãn nào xuất hiện nhiều nhất là kết quả
        most_common = Counter(k_labels).most_common(1)
        return most_common[0][0]

# --- PHẦN DEMO (MAIN) ---
if __name__ == "__main__":
    print("=== DEMO KNN ALGORITHM ===")
    # Dữ liệu mẫu (Giả sử: [Chiều cao, Cân nặng])
    train_data = [[158, 50], [170, 60], [180, 80], [160, 55], [175, 75]]
    train_labels = ["Nữ", "Nam", "Nam", "Nữ", "Nam"]
    
    knn = KNNClassifier(train_data, train_labels)

    # NHẬP LIỆU ĐỘNG (Dynamic Input)
    try:
        h = float(input("Nhập chiều cao (cm): "))
        w = float(input("Nhập cân nặng (kg): "))
        k_input = int(input("Nhập số lượng K (hàng xóm): "))
        
        result = knn.predict([h, w], k_input)
        print(f"-> Kết quả dự đoán với K={k_input}: Là {result}")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
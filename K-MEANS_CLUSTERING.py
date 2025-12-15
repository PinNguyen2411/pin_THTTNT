import random
import math

class KMeansSimple:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = []

    def _dist(self, p1, p2):
        # Tính khoảng cách Euclidean
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

    def fit(self, data):
        # 1. Khởi tạo tâm cụm ngẫu nhiên
        self.centroids = random.sample(data, self.k)
        
        for _ in range(self.max_iters):
            clusters = [[] for _ in range(self.k)]
            
            # 2. Gán mỗi điểm vào cụm gần nhất
            for point in data:
                distances = [self._dist(point, c) for c in self.centroids]
                closest_idx = distances.index(min(distances))
                clusters[closest_idx].append(point)
            
            # 3. Cập nhật tâm cụm mới (Trung bình cộng)
            prev_centroids = self.centroids[:]
            for i in range(self.k):
                if clusters[i]:
                    # Tính trung bình tọa độ các điểm trong cụm
                    dim = len(data[0])
                    avg = [sum(p[d] for p in clusters[i])/len(clusters[i]) for d in range(dim)]
                    self.centroids[i] = avg
            
            # Nếu tâm không đổi thì dừng sớm (Tối ưu)
            if prev_centroids == self.centroids:
                break
        return clusters

# --- DEMO ---
if __name__ == "__main__":
    print("--- DEMO K-MEANS ---")
    # Tạo dữ liệu mẫu (Chiều cao, Cân nặng)
    data = [[170, 65], [172, 68], [180, 80], [150, 45], [155, 48], [160, 55]]
    print("Dữ liệu mẫu:", data)
    
    k_input = int(input("Nhập số cụm K muốn chia (2 hoặc 3): "))
    
    model = KMeansSimple(k=k_input)
    result_clusters = model.fit(data)
    
    print("\n--- KẾT QUẢ ---")
    for i, cluster in enumerate(result_clusters):
        print(f"Cụm {i+1} (Tâm: {[round(x,1) for x in model.centroids[i]]}):")
        print(f"  -> Các điểm: {cluster}")
import networkx as nx
import matplotlib.pyplot as plt

class GraphColoring:
    def __init__(self):
        """Khởi tạo đồ thị rỗng sử dụng danh sách kề."""
        self.graph = {}
        self.nodes = []

    def add_edge(self, u, v):
        """Thêm cạnh nối giữa hai đỉnh u và v."""
        if u not in self.graph:
            self.graph[u] = []
            self.nodes.append(u)
        if v not in self.graph:
            self.graph[v] = []
            self.nodes.append(v)
            
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_color_name(self, color_index):
        """Chuyển đổi số thành tên màu để hiển thị."""
        colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Pink']
        if color_index < len(colors):
            return colors[color_index]
        return f"Color_{color_index}"

    def solve(self, max_colors):
        """
        Thuật toán tham lam (Greedy) để tô màu.
        Return: Dictionary chứa màu của các đỉnh hoặc None nếu không giải được.
        """
        result = {}
        
        # Sắp xếp các đỉnh theo bậc (số lượng hàng xóm) giảm dần -> Tối ưu hơn (Heuristic)
        # Các đỉnh có nhiều kết nối sẽ khó tô hơn nên cần tô trước.
        sorted_nodes = sorted(self.nodes, key=lambda x: len(self.graph[x]), reverse=True)

        for node in sorted_nodes:
            # Tìm các màu mà hàng xóm đã dùng
            neighbor_colors = set()
            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor in result:
                        neighbor_colors.add(result[neighbor])
            
            # Chọn màu thấp nhất chưa bị hàng xóm dùng
            color = 0
            while color in neighbor_colors:
                color += 1
            
            # Kiểm tra nếu số màu vượt quá giới hạn cho phép (Dynamic Input)
            if color >= max_colors:
                return None # Không tìm được giải pháp với số màu này
            
            result[node] = color
            
        return result

    def visualize(self, solution):
        """Vẽ đồ thị kết quả (cần thư viện networkx và matplotlib)."""
        G = nx.Graph()
        for u in self.graph:
            for v in self.graph[u]:
                G.add_edge(u, v)
        
        color_map = []
        if solution:
            # Map màu từ index sang tên màu của matplotlib
            vis_colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']
            for node in G.nodes():
                color_index = solution.get(node, 0)
                color_map.append(vis_colors[color_index % len(vis_colors)])
        else:
            color_map = 'gray'

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=800, font_color="white")
        plt.show()

# --- PHẦN MAIN 
if __name__ == "__main__":
    print("=== DEMO ĐỒ ÁN: TÔ MÀU ĐỒ THỊ (GRAPH COLORING) ===")
    
    # 1. Khởi tạo đối tượng (OOP)
    app = GraphColoring()
    
    
    try:
        num_edges = int(input("Nhập số lượng đường nối (cạnh) muốn tạo: "))
        print(f"Nhập {num_edges} cặp đỉnh nối với nhau :")
        
        for i in range(num_edges):
            u, v = map(int, input(f"Cạnh thứ {i+1} (u v): ").split())
            app.add_edge(u, v)
            
        max_colors_input = int(input("Nhập số lượng màu tối đa được phép dùng: "))
        
        # 3. Chạy thuật toán và show kết quả
        print(f"\nDang to mau voi toi da {max_colors_input} mau...")
        solution = app.solve(max_colors_input)
        
        if solution:
            print("\n--- KẾT QUẢ TÔ MÀU ---")
            for node, color in solution.items():
                print(f"Đỉnh {node} -> Màu: {app.get_color_name(color)}")
            
            print("\nĐang hiển thị hình ảnh đồ thị...")
            app.visualize(solution)
        else:
            print(f"\nKHÔNG THỂ TÔ MÀU! Đồ thị này quá phức tạp để tô chỉ với {max_colors_input} màu.")
            
    except ValueError:
        print("Lỗi nhập liệu! Vui lòng nhập số nguyên.")
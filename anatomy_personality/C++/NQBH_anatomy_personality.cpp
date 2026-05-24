/** author: NQBH
 * content:mã nguồn C++ xây dựng một hệ thống hướng đối tượng nhằm mô hình hóa bài toán tối ưu hóa cấu trúc nhân cách, trạng thái khoảng không hiện sinh và khủng hoảng hiện sinh theo đúng các định nghĩa toán học & thuật toán định tuyến hành vi được nghiên cứu trong NQBH_anatomy_personality.{pdf,tex}.
 */

#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

// đại diện cho không gian trạng thái nội tại (space of inner states) S_inner(P, t) of person P at time/moment t
struct Inner_State {
	double self_awareness = 1.0, connection_depth = 1.0, intrinsic_value = 1.0; // khả năng tự nhận thức, độ sâu gắn kết xã hội & với con người, giá trị nội tại tự thân

	void display() const {
		std::cout << "[Inner] Awareness: " << self_awareness << " | Connection: " << connection_depth << " | Intrinsic: " << intrinsic_value << '\n';
	}
};

// đại diện cho hệ thống tham số ngoại tại (a representative system of outer parameters)
struct Outer_System { // PhD, coder, programmer & the like
	double Q1_papers = 0.0, h_index = 0.0, salary = 0.0, control_over_power = 0.0, psychological_manipulation_level = 0.0; // biến số quyền lực kiểm soát

	// hàm đánh giá mức độ tối ưu hóa ngoại vi
	double evaluate_outer_optimum(double Q1_papers_coeff = 20.0, double h_index_coeff = 5.0, double salary_coeff = 0.01, double control_over_power_coeff = 15.0, double psychological_manipulation_level_coeff = 30.0) const { // do not use hard-coded constant coefficients, use adjustable parameters/hyperparameters instead
		return Q1_papers * Q1_papers_coeff + h_index * h_index_coeff + salary * salary_coeff + control_over_power * control_over_power_coeff + psychological_manipulation_level * psychological_manipulation_level_coeff;
	}

	void display() const {
		std::cout << "[Outer] Q1: " << Q1_papers << " | h-index: " << h_index << " | Salary Score: " << salary << " | Control-over Power: " << control_over_power << " | Psychological Manipulation Level/Skills: " << psychological_manipulation_level << '\n';
	}
};

// định nghĩa các trạng thái ổn định/mất ổn định của hệ thống tâm lý
enum class System_Status {
	STABLE,
	EXISTENTIAL_VACUUM, // khoảng không hiện sinh (existential vacuum)
	EXISTENTIAL_CRISIS, // khủng hoảng hiện sinh (vòng lặp vô hạn/sụp đổ động lực) (existential crisis/motivation collapse)
	OVERFITTING_PLEASURE, // quá khớp (overfitting) vào thú vui ngắn hạn (Gây nhiễu tín hiệu)
	TOXIC_POWER_COMPENSATION // bù trừ bằng cách kiểm soát độc hại (quay lại Chap. Adler, Sect. power): zero-sum game of existential energy of a human being
};

// lớp đại diện cho cá nhân P thuộc U_human: universe set of all human beings: possibly extend to animals & their psychology?
class Human {
private:
	std::string identifier; // tên định danh của cá nhân P, hoặc 1 list các mảnh nhân cách vừa đủ để xác định cấu hình tâm lý tổng quát (bắt chước Abstract Algebra: I am a very sick mathematician wannabe though)
	Inner_State s_t; // trạng thái nội tại s_t
	Outer_System outer_system; // hệ thống ngoại tại

	double current_time = 0.0, starved_duration = 0.0; // biến thời gian t & khoảng thời gian đang đo để so với ngưỡng \Delta t_{\rm threshold} để hàm M(P,t)(s_t) tiệm cận 0 liên tục

	// các siêu tham số cấu hình hệ thống (hyperparameters of a human's inner-outer system): as a Fullstack Survivor through Existential Crisis/Vacuum of the Game of Life
	const double Delta_t_threshold = 5.0, meaning_epsilon = 1e-3; // \Delta t_{threshold} để kích hoạt Nguyên lý: Sự bù trù dòng năng lượng hiện sinh (Principle: Zero-sum game of existential energy of a human being); ngưỡng tiệm cận 0 của hàm M

	System_Status status = System_Status::STABLE;

public:
	Human(std::string id, Inner_State initial_inner, Outer_System initial_outer) : identifier(std::move(id)), s_t(initial_inner), outer_system(initial_outer) {}
	// hàm mục tiêu nội tại M(P, t)(s_t) -- chỉ số ý nghĩa (meaning index)
	double compute_meaning_index(double outer_score_coeff = 0.05) const {
		double intrinsic_score = s_t.self_awareness * s_t.connection_depth * s_t.intrinsic_value;
		double outer_score = outer_system.evaluate_outer_optimum();

		if (outer_score <= 0.0) return intrinsic_score;

		// mô hình hóa: khi quá tập trung tối ưu tham số ngoại tại mà bỏ quên nội tại thì sự mất cân bằng sẽ khiến hàm M(P, t)(s_t) tiệm cận về 0

		return intrinsic_score / (1.0 + outer_score_coeff * outer_score); // should change/parameterize constant 1.0?
	}

	// thuật toán định tuyến hành vi: ước lượng gradient tăng trưởng của hàm M
	double calculate_meaning_gradient(double outer_score_coeff = 0.05) {
		double step = 1e-4, M_current = compute_meaning_index();

		// giả lập thử nghiệm tiến 1 bước nhỏ trong không gian nhận thức nội tại
		double simulated_awareness = s_t.self_awareness + step;
		double simulated_intrinsic = simulated_awareness * s_t.connection_depth * s_t.intrinsic_value;
		double M_simulated = simulated_intrinsic / (1.0 + outer_score_coeff * outer_system.evaluate_outer_optimum());

		// gradient = dM / d(awareness): maybe Python JAX's autograd better here
		return (M_simulated - M_current) / step;
	}

	// cực đại hóa cục bộ các biến số ngoại tại, e.g., cỗ máy tối ưu hóa của PhD, coder, programmer & the like
	void optimzie_outer_parameters(double num_paper, double h, double money) {
		outer_system.Q1_papers += num_paper;
		outer_system.h_index += h;
		outer_system.salary += money;

		// mental tradeoff: trả giá bằng việc suy giảm tài nguyên nội tại do phân phối năng lượng sai lệch inner/outer cognitive energy gap
		s_t.connection_depth *= 0.4; // đứt gãy các mối quan hệ sâu sắc: (hyper-)parameterize this constant
		s_t.self_awareness *= 0.7; // suy giảm khả năng tự nhận thức, tự tỉnh thức: (hyper-)parameterize this constant
	}

	// kích hoạt Nguyên lý: Cơ chế bù trừ dòng năng lượng hiện sinh (compensatory mechanism)
	void apply_compensatory_mechanism() {
		std::cout << "\n[CRITICAL ALERT] P = " << identifier << " bế tắc năng lượng vượt ngưỡng Delta T_{threshold}: Kích hoạt Nguyên lý Compensatory Mechanism.\n";

		if (s_t.self_awareness < 0.5) {
			// nhập thức đủ thấp => overfitting vào thú vui ngắn hạn để gây nhiễu hệ thống nhận thức
			status = System_Status::OVERFITTING_PLEASURE;
			std::cout << "=> Định tuyến thất bại: Hệ thống chọn OVERFITTING vào khoái lạc ngắn hạn\n";
		} else {
			// nhận thức cao hơn nhưng mất định hướng => Chiếm đoạt quyền lực ngoại tại để bù đắp (from Adlerian psychology)
			status = System_Status::TOXIC_POWER_COMPENSATION;
			outer_system.control_over_power += 50.0;
			std::cout << "=> Định tuyến thất bại: Chuyển dịch tài nguyên sang kiểm soát/chèn ép người khác.\nHệ thống rơi vào chu kỳ bỏng nóng / bỏng lạnh liên tiếp.\n";
		}
	}
	// cập nhật trạng thái hệ thống theo bước thời gian dt
	void update_system_state(double dt) {
		current_time += dt;
		double M = compute_meaning_index(), gradient = calculate_meaning_gradient(), outer_score = outer_system.evaluate_outer_optimum();

		// kiểm tra trạng thái khoảng không hiện sinh (existential vacuum): đạt tối ưu ngoại tại nhưng M(P, t)(s_t) tiệm cận về 0
		if (outer_score > 50.0 && M < meaning_epsilon)
			if (status == System_Status::STABLE) status = System_Status::EXISTENTIAL_VACUUM;

		// kiểm tra trạng thái khủng hoảng hiện sinh (Existential Crisis)
		// thuật toán định tuyến không tìm thấy gradient tăng trưởng, i.e., gradient <= 0
		if (status == System_Status::EXISTENTIAL_VACUUM && gradient <= 0.0) status = System_Status::EXISTENTIAL_CRISIS;

		// theo dõi thời gian bị ``đói'' ý nghĩa liên tục \forall t\in[t_start, t_curr]
		if (M < meaning_epsilon) starved_duration += dt;
		else starved_duration = 0.0;

		// thực thi hệ quả của nguyên lý Conpensatory Mechanism nếu vượt ngưỡng thời gian quy định \Delta t_{threshold}
		if (starved_duration >= Delta_t_threshold && status != System_Status::OVERFITTING_PLEASURE && status != System_Status::TOXIC_POWER_COMPENSATION) apply_compensatory_mechanism();
	}

	void print_telemetry() const {
		std::cout << "========================================================\nTelemetry for person P: " << identifier << " | Time t = " << current_time << '\n';
		s_t.display();
		outer_system.display();
		std::cout << "Meaning Index M(P, t)(s_t) = " << compute_meaning_index() << "\nSystem Status: ";
		switch (status) {
		case System_Status::STABLE: std::cout << "STABLE\n"; break;
		case System_Status::EXISTENTIAL_VACUUM: std::cout << "EXISTENTIAL_VACUUM (Khoảng không hiện sinh)\n"; break;
		case System_Status::EXISTENTIAL_CRISIS: std::cout << "EXISTENTIAL_CRISIS (Infinite Loop / No Gradient)\n"; break;
		case System_Status::OVERFITTING_PLEASURE: std::cout << "OVERFITTING_PLEASURE (Gây nhiễu tín hiệu)\n"; break;
		case System_Status::TOXIC_POWER_COMPENSATION: std::cout << "TOXIC_POWER_COMPENSATION (Adlerian Toxic Power)\n"; break;
		}
		std::cout << "========================================================\n";
	}
};

int main() {
	// ============================================================================
	// BASIC FRAMEWORK
	// ============================================================================
		std::cout << "BASIC FRAMEWORK\n";

	// khởi tạo thực thể nghiên cứu sinh PhD/coder/programmer P với cấu trúc nội tâm ban đầu cân bằng
	Inner_State initial_inner{1.2, 1.0, 1.5};
	Outer_System initial_outer{0, 0, 1000.0, 0};

	Human PhD_student ("NQBH [25, PhD student]", initial_inner, initial_outer);
	std::cout << "--- Trạng thái ban đầu (Initial State) ---\n";
	PhD_student.print_telemetry();

	// giả lập chuỗi hành vi: tối ưu hóa điên cuồng các tham số ngoại tại, e.g., quên cả bạn gái giỏi thay lòng & skip mấy con trap girls ái kỷ
	std::cout << "\n>>> Thực hiện thuật toán tối ưu ngoại tại: Cày bài báo Q1, tăng h-index...\n";
	PhD_student.optimzie_outer_parameters(5.0, 12.0, 5000.0); // đạt global optimum của hệ thống ngoài

	// chạy mô phỏng dòng thời gian để kiểm tra sự mất ổn định của hệ thống
	for (int step = 1; step <= 6; ++step) { // đang mô phỏng quá trình AI, thông qua cơ chế  Trí thông minh cá nhân-- Cá nhân hoá cuộc trò chuyện khi cần thiết   bắt chước style suy luận từ Bachelor Thesis of Nguyễn Ngọc Thạch
		PhD_student.update_system_state(1.0); // mỗi bước thời gian dt = 1.0
		if (step == 1 || step == 3 || step == 6) {
			std::cout << "\n--- Bước mô phỏng t = " << step << " ---";
			PhD_student.print_telemetry();
		}
	}

	// ============================================================================
	// ADVANCED FRAMEWORK
	// ============================================================================
	std::cout << "ADVANCED FRAMEWORK\n";

	// ============================================================================
	// PARALLELIZATION FRAMEWORK
	// ============================================================================
	std::cout << "PARALLELIZATION FRAMEWORK\n";

}

/*
compilation:
g++ -O3 -Wall -march=native -fopenmp -std=c++26 -I /usr/include/eigen3 NQBH_anatomy_personality.cpp -o NQBH_anatomy_personality
time ./NQBH_anatomy_personality

[addinng] use mpirun & MP flags for PARALLELIZATION FRAMEWORK later
*/
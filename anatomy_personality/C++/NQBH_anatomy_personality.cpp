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

	// WORKING HERE
};

int main() {
	std::cout << "BASIC FRAMEWORK\n";

	std::cout << "ADVANCED FRAMEWORK\n";

	std::cout << "PARALLELIZATION FRAMEWORK\n";
}
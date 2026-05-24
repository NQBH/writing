/**
 * @author: Nguyen Quan Ba Hong [NQBH]
 * @file: NQBH_anatomy_personality.cpp (or maybe NQBH_human_personality_anatomy.cpp)
 * @brief: Advanced Differential Dynamical System for Human Personality Anatomy based on Alfred Adler's Individual Psychology & Viktor Emil Frankl's Logotherapy
 * @content: Mã nguồn C++ xây dựng một hệ thống hướng đối tượng nhằm mô hình hóa bài toán tối ưu hóa cấu trúc nhân cách, trạng thái khoảng không hiện sinh & khủng hoảng hiện sinh theo đúng các định nghĩa toán học & thuật toán định tuyến hành vi được nghiên cứu trong NQBH_anatomy_personality.{pdf,tex}
 */

#include <algorithm>
#include <cmath>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <memory>
#include <numeric>
#include <stdexcept>
#include <string>
#include <string_view>
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

// ============================================================================
// ADVANCED FRAMEWORK
// ============================================================================

namespace Psychodynamics {

// ========================================================================
// 1MATHEMATICAL STATE SPACES: Toán Học Hóa Không Gian Trạng Thái
// ========================================================================

// không gian nội tại: \mathcal{S}_{\rm inner}(P, t)\in\mathbb{R}^3
struct Inner_Space {
	double awareness, connection, integrity; // tự nhận thức (perception), gắn kết sâu sắc (senses of humanity), tính chính trực (integrity)

	// l2 norm: khối lượng tài nguyên nội tại: use other norms?
	[[nodiscard]] constexpr double l2_norm() const noexcept {
		return std::sqrt(awareness * awareness + connection * connection + integrity * integrity);
	}

	// zero-sum game principle: hao mòn nội tại theo hàm phân rã mũ (exponential decay)
	constexpr Inner_Space& decay(double decay_rate, double dt) noexcept {
		double factor = std::exp(-decay_rate * dt);
		awareness = std::max(0.001, awareness * factor);
		connection = std::max(0.001, connection * factor);
		integrity = std::max(0.001, integrity * factor);
		return *this;
	}

	// nạp chồng toán tử cho Đại số tuyến tính (operator overloading for Linear Algebra)
	[[nodiscard]] constexpr Inner_Space operator+(const Inner_Space& rhs) const noexcept {
		return {awareness + rhs.awareness, connection + rhs.connection, integrity + rhs.integrity};
	}

	[[nodiscard]] constexpr Inner_Space operator*(double scalar) const noexcept {
		return {awareness * scalar, connection * scalar, integrity * scalar};
	}
};

// Space of Outer Parameters: không gian ngoại tại
struct Outer_Space {
	double wealth, academic_metrics, toxic_power_control; // vật chất, tài chính; số Q1 papers, h-index; quyền lực thao túng kiểu Adlerian

	// hàm mục tiêu ngoại tại tuyến tính
	[[nodiscard]] constexpr double evaluate_global_optimum() const noexcept {
		return wealth * 0.05 + academic_metrics * 10.0 + toxic_power_control * 15.0;
	}
};

struct Personality_Traits {
	bool is_highly_sensitive_person = false; // tính nhạy cảm cao
	double superiority_tendency = 0.5; // khao khát quyền lực độc hại [0.0, 1.0]
};

// ========================================================================
// PSYCHOLOGICAL STATE MACHINE: Máy Trạng Thái Tâm Lý
// ========================================================================
enum class System_Phase {
	EQUILIBRIUM, // cân bằng, khỏe mạnh
	EXISTENTIAL_VACUUM, // khoảng không hiện sinh (M(P,t)(s_t) -> 0)
	EXISTENTIAL_CRISIS, // Khủng hoảng hiện sinh (\nabla M <= 0, Infinite Loops)
	OVERFITTING_PLEASURE, // bù trừ: Quá khớp (overfitting) khoái lạc ngắn hạn, gây nhiễu nhận thức
	TOXIC_POWER_COMPENSATION // bù trừ: Tìm quyền lực chèn ép người khác (Adlerian toxic)
};

[[nodiscard]] constexpr std::string_view phase2string(System_Phase phase) noexcept {
	switch (phase) {
	case System_Phase::EQUILIBRIUM:              return "\033[1;32mEQUILIBRIUM (Cân Bằng)\033[0m";
	case System_Phase::EXISTENTIAL_VACUUM:       return "\033[1;33mEXISTENTIAL_VACUUM (Khoảng Không Hiện Sinh)\033[0m";
	case System_Phase::EXISTENTIAL_CRISIS:       return "\033[1;31mEXISTENTIAL_CRISIS (Khủng Hoảng/Bế Tắc)\033[0m";
	case System_Phase::OVERFITTING_PLEASURE:     return "\033[1;35mOVERFITTING_PLEASURE (Gây nhiễu nhận thức)\033[0m";
	case System_Phase::TOXIC_POWER_COMPENSATION: return "\033[1;31mTOXIC_POWER_COMPENSATION (Quyền Lực Độc Hại)\033[0m";
	default:                                    return "UNKNOWN";
	}
}

// ========================================================================
// CORE HUMAN CLASS: Thực thể Con Người Để Giải Phẫu Nhân Cách
// ========================================================================
class Human {
public:
	// dependency injection/embedding: cho phép tiêm/nhúng hàm ý nghĩa (meaning function) từ bên ngoài
	using Meaning_Policy = std::function<double(const Inner_Space&, const Outer_Space&)>;

private:
	std::string       identifier_;
	Inner_Space        inner_;
	Outer_Space        outer_;
	Personality_Traits traits_;
	Meaning_Policy     evaluator_M_;

	System_Phase       phase_ = System_Phase::EQUILIBRIUM;
	double            time_t_ = 0.0;
	double            starved_duration_ = 0.0;

	// cấu trúc dữ liệu hàng đợi sliding window để phát hiện vòng lặp vô hạn (infinite loops)
	std::deque<double> meaning_history_;
	static constexpr size_t HISTORY_WINDOW_SIZE = 5;

	// systematic/system-dependent hyperparameters: siêu tham số hệ thống
	static constexpr double EPSILON_MEANING = 1e-3, GRADIENT_STEP = 1e-4, DELTA_T_THRESHOLD = 5.0, OUTER_SATISFACTION = 100.0;

	// hàm khởi tạo được ẩn đi, bắt buộc dùng Builder Pattern để thiết lập
	Human(std::string_view id, Inner_Space in_sp, Outer_Space out_sp, Personality_Traits trace, Meaning_Policy policy)
		: identifier_(id), inner_(in_sp), outer_(out_sp), traits_(trace), evaluator_M_(std::move(policy)) {
		if (!evaluator_M_) throw std::invalid_argument("Meaning Policy (Hàm M) không được để trống.");
	}

	// ước lượng đạo hàm có hướng (directional gradient): thuật toán dò đường
	[[nodiscard]] double compute_directional_gradient() const noexcept {
		double M_current = evaluator_M_(inner_, outer_);

		// giả lập cá nhân nỗ lực tăng nhận thức lên 1 lượng vi phân nhỏ để tìm lối thoát
		Inner_Space forward_state = inner_ + Inner_Space{GRADIENT_STEP, 0.0, 0.0};
		double M_forward = evaluator_M_(forward_state, outer_);

		return (M_forward - M_current) / GRADIENT_STEP;
	}

	// kích hoạt Compensatory Principle: Cơ Chế Bù Trừ
	void trigger_compensatory_mechanism() noexcept {
		if (phase_ == System_Phase::OVERFITTING_PLEASURE || phase_ == System_Phase::TOXIC_POWER_COMPENSATION) return;

		// bộ định tuyến hành vi kết hơp tính nhạy cảm cao (high sensitivity) & chính trực (integrity)
		if (inner_.awareness < 0.5) {
			// nhận thức quá thấp => rơi vào hố đen gây nhiễu
			phase_ = System_Phase::OVERFITTING_PLEASURE;
			inner_.decay(2.0, 1.0);
		} else {
			// biến đổi thành toxic colleages/parents
			phase_ = System_Phase::TOXIC_POWER_COMPENSATION;
			outer_.toxic_power_control += 50.0 * traits_.superiority_tendency; // bẻ cong thang quyền lực
			inner_.connection *= 0.05; // triệt tiêu vĩnh viễn tính đồng cảm
		}
	}

public:
	// ====================================================================
	// BUILDER PATTERN: initialize C++ elegantly & safely
	// ====================================================================
	class Builder {
	private:
		std::string       id_ = "Anonymous Entity";
		Inner_Space        inner_ = {1.0, 1.0, 1.0};
		Outer_Space        outer_ = {0.0, 0.0, 0.0};
		Personality_Traits traits_;
		Meaning_Policy     policy_;

	public:
		Builder& set_identifier(std::string_view id)		 {
			id_ = std::string(id);
			return *this;
		}

		Builder& set_inner_space(Inner_Space inner_space) {
			inner_ = inner_space;
			return *this;
		}

		Builder& set_outer_space(Outer_Space outer_space) {
			outer_ = outer_space;
			return *this;
		}

		Builder& set_traits(Personality_Traits personality_trait) {
			traits_ = personality_trait;
			return *this;
		}

		Builder& set_meaning_policy(Meaning_Policy meaning_policy) {
			policy_ = std::move(meaning_policy);
			return *this;
		}

		// trả về smart pointer unique_ptr để tự động dọn dẹp bộ nhớ
		[[nodiscard]] std::unique_ptr<Human> build() const {
			return std::unique_ptr<Human>(new Human(id_, inner_, outer_, traits_, policy_));
		}
	};

	// ====================================================================
	// BEHAVIORAL KINEMATICS: Động Học Hành Vi
	// ====================================================================

	// ví dụ: đánh đổi linh hồn để tối ưu hóa cỗ máy tham số ngoại tại
	void grind_outer_parameters(double intensity, double dt) noexcept {
		if (phase_ == System_Phase::OVERFITTING_PLEASURE || phase_ == System_Phase::TOXIC_POWER_COMPENSATION) return;

		outer_.academic_metrics += intensity * 5.0 * dt;
		outer_.wealth += intensity * 20.0 * dt;

		// zero-sum game: bòn rút năng lượng không gian nội tại, cô lập bản thân
		inner_.decay(intensity * 0.15, dt);
	}

	// Time-Step Integration: tiến hóa hệ thống theo thời gian thực
	void evolve(double dt) noexcept {
		time_t_ += dt;
		double M_current = evaluator_M_(inner_, outer_), grad_M = compute_directional_gradient(), out_opt = outer_.evaluate_global_optimum();

		// cập nhật sliding window để phân tích vòng lặp
		meaning_history_.push_back(M_current);
		if (meaning_history_.size() > HISTORY_WINDOW_SIZE) meaning_history_.pop_front();

		// toán học hóa vòng lặp vô tận: tính phương sai (variance)
		bool is_infinite_loop = false;
		if (meaning_history_.size() == HISTORY_WINDOW_SIZE) {
			double variance = 0.0, mean = std::accumulate(meaning_history_.begin(), meaning_history_.end(), 0.0) / HISTORY_WINDOW_SIZE;
			for (double val : meaning_history_) variance += (val - mean) * (val - mean);
			variance /= HISTORY_WINDOW_SIZE;

			if (variance < 1e-9) is_infinite_loop = true; // giá trị M(P, t)(s_t) kẹt cứng (OMG! I am stuck), không suy suyển
		}

		// rơi vào khoảng không hiện sinh: đạt đỉnh ngoại tại nhưng hàm M(P, t)(s_t) tiệm cận 0
		if (phase_ == System_Phase::EQUILIBRIUM && out_opt > OUTER_SATISFACTION && M_current < EPSILON_MEANING) phase_ = System_Phase::EXISTENTIAL_VACUUM;

		// chuyển pha thành khủng hoảng hiện sinh: gradient <= 0 hoặc bị mắc kẹt vô hạn
		if (phase_ == System_Phase::EXISTENTIAL_VACUUM && (grad_M <= 0.0 || is_infinite_loop)) phase_ = System_Phase::EXISTENTIAL_CRISIS;

		// tích lũy đồn bẩy thời gian chịu đựng
		if (M_current < EPSILON_MEANING) starved_duration_ += dt;
		else starved_duration_ = std::max(0.0, starved_duration_ - dt);

		// bẻ gãy cấu trúc nhân cách nếu vượt ngưỡng \Delta t_{\rm threshold}
		if (starved_duration_ >= DELTA_T_THRESHOLD && (phase_ == System_Phase::EXISTENTIAL_VACUUM || phase_ == System_Phase::EXISTENTIAL_CRISIS)) trigger_compensatory_mechanism();
	}

	// ====================================================================
	// TELEMETRY: GIAO DIỆN HIỂN THỊ
	// ====================================================================
	void render_telemetry() const noexcept {
		std::cout << std::string(75, '=') << "\n";
		std::cout << " [TELEMETRY P] ID: " << identifier_ << (traits_.is_highly_sensitive_person ? " (HSP)" : "")
		          << " | t = " << std::fixed << std::setprecision(1) << time_t_ << "\n";
		std::cout << std::string(75, '-') << "\n";
		std::cout << " > \033[1;36mS_inner (Nội tại)\033[0m  : Aw[" << std::setprecision(3) << inner_.awareness
		          << "] Con[" << inner_.connection << "] Int[" << inner_.integrity << "] (Norm: " << inner_.l2_norm() << ")\n";
		std::cout << " > \033[1;33mS_outer (Ngoại tại)\033[0m: Global Optimum = " << outer_.evaluate_global_optimum() << "\n";
		std::cout << "                      (Wealth:" << outer_.wealth << " Acad:" << outer_.academic_metrics
		          << " ToxPwr:" << outer_.toxic_power_control << ")\n";

		double M_t = evaluator_M_(inner_, outer_);
		std::cout << " > \033[1;32mMeaning M(P,t)\033[0m     : " << std::scientific << M_t << std::fixed << "\n";
		std::cout << " > Gradient \u2207M        : " << compute_directional_gradient() << "\n";
		std::cout << " > Starved Duration \u0394t: " << std::setprecision(1) << starved_duration_ << " / " << DELTA_T_THRESHOLD << "\n";
		std::cout << " > SYSTEM PHASE       : " << phase2string(phase_) << "\n";
		std::cout << std::string(75, '=') << "\n\n";
	}
};

} // end of namespace Psychodynamics

// ============================================================================
// MAIN FUNCTION
// ============================================================================

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
	// ADVANCED FRAMEWORK: SIMULATION KINEMATICS
	// ============================================================================
	using namespace Psychodynamics;

	std::cout << "ADVANCED FRAMEWORK: MAIN EXECUTION & SIMULATION KINEMATICS\n";

	// toán học hóa Triết học Logotherapy của Viktor Emil Frankl (dependency injection/embedding): hàm ý nghĩa sụp đổ theo hàm suy giảm phân rã mũ nếu ngoại tại nuốt chửng sự cân bằng của nội tại
	auto Viktor_Frankl_meaning_evaluator = [](const Inner_Space & inner_space, const Outer_Space & outer_space) -> double {
		double inner_strength = inner_space.l2_norm(), outer_pressure = outer_space.evaluate_global_optimum(), existential_gap = std::max(0.0, outer_pressure * 0.1 - inner_strength);
		return inner_strength * std::exp(-0.5 * existential_gap);
	};

	try {
		// kịch bản: PhD student/coder/programmer khởi điểm với sức khỏe tâm lý khỏe mạnh
		auto PhD_student = Psychodynamics::Human::Builder().set_identifier("H [25, PhD Student]").set_inner_space({2.0, 2.0, 2.0}).set_outer_space({0.0, 5.0, 0.0}).set_traits({true, 0.8})/* là người nhạy cảm cao (HSP), có thiên hướng có phức cảm thượng đẳng (superiority complex)*/.set_meaning_policy(Viktor_Frankl_meaning_evaluator).build();
	
		std::cout << "[PHASE 0] TRẠNG THÁI KHỞI NGUYÊN (CÂN BẰNG NỘI TẠI)\n";
		PhD_student->render_telemetry();

		std::cout << "[PHASE 1] TỐI ƯU HÓA CỰC ĐOAN NGOẠI TẠI (The External Grind)\n=> Cá nhân cày cuốc ngày đêm, hi sinh kết nối xã hội & giá trị cốt lõi...\n\n";

		for (int step = 1; step <= 3; ++step) {
			PhD_student->grind_outer_parameters(3.0, 1.0); // dồn năng lượng khổng lồ
			PhD_student->evolve(1.0);
		}
		PhD_student->render_telemetry();

		std::cout << "[PHASE 2] RƠI VÀO KHOẢNG KHÔNG & KHỦNG HOẢNG HIỆN SINH (Lúc 2:00 Sáng)\n=> Chạm đỉnh ngoại tại (Global Optimum), nhưng Hàm Ý Nghĩa M(t) bốc hơi.\n=> Bị giam cầm trong vòng lặp vô tận (Infinite loop).\n\n";

		for (int step = 4; step <= 7; ++step) PhD_student->evolve(1.0); // thời gian tự trôi, hệ thống mắc kẹt vô định
		PhD_student->render_telemetry();

		std::cout << "[PHASE 3] VƯỢT NGƯỠNG ĐỘ KÉO ĐỨT (Starvation > \\Delta t_{threshold})\n=> Kích hoạt Nguyên lý 1: Đứt gãy. Chuyển hóa thành \"Đồng nghiệp độc hại\" (Adler).\n\n";
	
		PhD_student->evolve(2.0); // đẩy starved_duration vượt mốc 5.0: \Delta t_{\rm threshold}
		PhD_student->render_telemetry();
	} catch (const std::exception& e) {
		std::cerr << "[FATAL ERROR] " << e.what() << '\n';
        return EXIT_FAILURE;
	}


	// ============================================================================
	// PARALLELIZATION FRAMEWORK
	// ============================================================================
	std::cout << "PARALLELIZATION FRAMEWORK\n";
	// build later when NQBH becomes psychologically confident & intellectually mad enough

	return EXIT_SUCCESS; // return 0
}

/*
compilation:
g++ -O3 -Wall -march=native -fopenmp -std=c++26 -I /usr/include/eigen3 NQBH_anatomy_personality.cpp -o NQBH_anatomy_personality
time ./NQBH_anatomy_personality

[addinng] use mpirun & MP flags for PARALLELIZATION FRAMEWORK later

terminal output of compilation & execution:

nqbh@msi:~/writing/anatomy_personality/C++$ g++ -O3 -Wall -march=native -fopenmp -std=c++26 -I /usr/include/eigen3 NQBH_anatomy_personality.cpp -o NQBH_anatomy_personality
nqbh@msi:~/writing/anatomy_personality/C++$ time ./NQBH_anatomy_personality 
BASIC FRAMEWORK
--- Trạng thái ban đầu (Initial State) ---
========================================================
Telemetry for person P: NQBH [25, PhD student] | Time t = 0
[Inner] Awareness: 1.2 | Connection: 1 | Intrinsic: 1.5
[Outer] Q1: 0 | h-index: 0 | Salary Score: 1000 | Control-over Power: 0 | Psychological Manipulation Level/Skills: 0
Meaning Index M(P, t)(s_t) = 1.2
System Status: STABLE
========================================================

>>> Thực hiện thuật toán tối ưu ngoại tại: Cày bài báo Q1, tăng h-index...

--- Bước mô phỏng t = 1 ---========================================================
Telemetry for person P: NQBH [25, PhD student] | Time t = 1
[Inner] Awareness: 0.84 | Connection: 0.4 | Intrinsic: 1.5
[Outer] Q1: 5 | h-index: 12 | Salary Score: 6000 | Control-over Power: 0 | Psychological Manipulation Level/Skills: 0
Meaning Index M(P, t)(s_t) = 0.042
System Status: STABLE
========================================================

--- Bước mô phỏng t = 3 ---========================================================
Telemetry for person P: NQBH [25, PhD student] | Time t = 3
[Inner] Awareness: 0.84 | Connection: 0.4 | Intrinsic: 1.5
[Outer] Q1: 5 | h-index: 12 | Salary Score: 6000 | Control-over Power: 0 | Psychological Manipulation Level/Skills: 0
Meaning Index M(P, t)(s_t) = 0.042
System Status: STABLE
========================================================

--- Bước mô phỏng t = 6 ---========================================================
Telemetry for person P: NQBH [25, PhD student] | Time t = 6
[Inner] Awareness: 0.84 | Connection: 0.4 | Intrinsic: 1.5
[Outer] Q1: 5 | h-index: 12 | Salary Score: 6000 | Control-over Power: 0 | Psychological Manipulation Level/Skills: 0
Meaning Index M(P, t)(s_t) = 0.042
System Status: STABLE
========================================================
ADVANCED FRAMEWORK: MAIN EXECUTION & SIMULATION KINEMATICS
[PHASE 0] TRẠNG THÁI KHỞI NGUYÊN (CÂN BẰNG NỘI TẠI)
===========================================================================
 [TELEMETRY P] ID: H [25, PhD Student] (HSP) | t = 0.0
---------------------------------------------------------------------------
 > S_inner (Nội tại)  : Aw[2.000] Con[2.000] Int[2.000] (Norm: 3.464)
 > S_outer (Ngoại tại): Global Optimum = 50.000
                      (Wealth:0.000 Acad:5.000 ToxPwr:0.000)
 > Meaning M(P,t)     : 1.607e+00
 > Gradient ∇M        : 0.732
 > Starved Duration Δt: 0.0 / 5.0
 > SYSTEM PHASE       : EQUILIBRIUM (Cân Bằng)
===========================================================================

[PHASE 1] TỐI ƯU HÓA CỰC ĐOAN NGOẠI TẠI (The External Grind)
=> Cá nhân cày cuốc ngày đêm, hi sinh kết nối xã hội & giá trị cốt lõi...

===========================================================================
 [TELEMETRY P] ID: H [25, PhD Student] (HSP) | t = 3.0
---------------------------------------------------------------------------
 > S_inner (Nội tại)  : Aw[0.518] Con[0.518] Int[0.518] (Norm: 0.898)
 > S_outer (Ngoại tại): Global Optimum = 509.000
                      (Wealth:180.000 Acad:50.000 ToxPwr:0.000)
 > Meaning M(P,t)     : 1.246e-11
 > Gradient ∇M        : 0.000
 > Starved Duration Δt: 3.0 / 5.0
 > SYSTEM PHASE       : EXISTENTIAL_VACUUM (Khoảng Không Hiện Sinh)
===========================================================================

[PHASE 2] RƠI VÀO KHOẢNG KHÔNG & KHỦNG HOẢNG HIỆN SINH (Lúc 2:00 Sáng)
=> Chạm đỉnh ngoại tại (Global Optimum), nhưng Hàm Ý Nghĩa M(t) bốc hơi.
=> Bị giam cầm trong vòng lặp vô tận (Infinite loop).

===========================================================================
 [TELEMETRY P] ID: H [25, PhD Student] (HSP) | t = 7.0
---------------------------------------------------------------------------
 > S_inner (Nội tại)  : Aw[0.518] Con[0.026] Int[0.518] (Norm: 0.734)
 > S_outer (Ngoại tại): Global Optimum = 1109.000
                      (Wealth:180.000 Acad:50.000 ToxPwr:40.000)
 > Meaning M(P,t)     : 8.774e-25
 > Gradient ∇M        : 0.000
 > Starved Duration Δt: 7.0 / 5.0
 > SYSTEM PHASE       : TOXIC_POWER_COMPENSATION (Quyền Lực Độc Hại)
===========================================================================

[PHASE 3] VƯỢT NGƯỠNG ĐỘ KÉO ĐỨT (Starvation > \Delta t_{threshold})
=> Kích hoạt Nguyên lý 1: Đứt gãy. Chuyển hóa thành "Đồng nghiệp độc hại" (Adler).

===========================================================================
 [TELEMETRY P] ID: H [25, PhD Student] (HSP) | t = 9.0
---------------------------------------------------------------------------
 > S_inner (Nội tại)  : Aw[0.518] Con[0.026] Int[0.518] (Norm: 0.734)
 > S_outer (Ngoại tại): Global Optimum = 1109.000
                      (Wealth:180.000 Acad:50.000 ToxPwr:40.000)
 > Meaning M(P,t)     : 8.774e-25
 > Gradient ∇M        : 0.000
 > Starved Duration Δt: 9.0 / 5.0
 > SYSTEM PHASE       : TOXIC_POWER_COMPENSATION (Quyền Lực Độc Hại)
===========================================================================

PARALLELIZATION FRAMEWORK

real	0m0.006s
user	0m0.002s
sys	0m0.005s
nqbh@msi:~/writing/anatomy_personality/C++$ 

*/
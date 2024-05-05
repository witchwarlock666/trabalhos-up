#include <iostream>
#include <vector>
#include <set>
#include <bitset>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

class Input {
public:
	set<int> group = {};
	uint8_t x_mask = 0;
	uint8_t value = 0;
	uint8_t id = 0;

	Input(uint8_t value) : value(value), id(value) {
		group.insert(id);
	}

	size_t count_ones() {
		value = value & ~x_mask;
		size_t ones = 0;
		for (size_t i = 0; i < 8; i++) ones += (value >> i) & 1;
		return ones;
	}

	bool try_merge(Input& other) {

		uint8_t value_equals_mask = value ^ other.value;
		uint8_t mask_equals_mask = x_mask ^ other.x_mask;
		/*cout << to_string() << endl;
		cout << other.to_string() << endl;
		cout << "value " << bitset<4>(value_equals_mask) << endl;
		cout << "mask " << bitset<4>(mask_equals_mask) << endl;*/

		size_t equals = 0;
		for (size_t i = 0; i < 8; i++) {
			equals += ((value_equals_mask >> i) & 1);
			equals += ((mask_equals_mask >> i) & 1);
		}
		//cout << (equals != 1 ? "Not Merged" : "Merged") << endl;
		if (equals != 1) return false;

		x_mask = x_mask | value_equals_mask | other.x_mask;
		merge(other);

		return true;
	}

	string to_string() {
		string val;
		for (size_t i = 8; i > 0; i--) {
			if ((x_mask >> i - 1) & 1) val += 'X';
			else val += (value >> i - 1) & 1 ? '1' : '0';
		}
		val += " (";
		for (auto& id : group) {
			val += std::to_string(id) + ',';
		}
		val += ')';
		return val;
	}

	string circuit_string(size_t size) {
		string val;
		int l = 0;

		for (size_t i = 0; i < size+1; i++) {
			if (!((x_mask >> i) & 1)) {
				int k = 1;
				for (auto g : group) {
					k = (g >> l) & k;
				}
				if (k == 0) {
					val += '~';
				}
				val += (char)(l + 65);
			}
			l++;
		}
		return val;
	}

	bool in_group(Input& other) {
		//if (group.size() != other.group.size()) return false;
		for (auto& val : other.group) if (!group.contains(val)) return false;
		//for (auto& val : group) if (!other.group.contains(val)) return false;
		return true;
	}
	bool in_group(int other) {
		return group.contains(other);
	}

	bool equals(Input& other) {
		if (group.size() != other.group.size()) return false;
		for (auto& val : other.group) if (!group.contains(val)) return false;
		for (auto& val : group) if (!other.group.contains(val)) return false;
		return true;
	}

	void merge(Input& other) {
		for (auto val : other.group) group.insert(val);
	}

	Input copy() {
		Input new_input(value);
		new_input.merge(*this);
		new_input.x_mask = x_mask;
		return new_input;
	}
};

void clear_duplicated(vector<Input>& inputs) {
	size_t i = 0;
	for (size_t i = 0; i < inputs.size(); i++) {
		Input input = inputs[i];

		for (size_t e = 0; e < inputs.size(); e++) {
			if (i != e && (input.in_group(inputs[e]))) {
				inputs.erase(inputs.begin() + e);
				/*clear_duplicated(inputs);
				return;*/
				i = -1;
				break;
			}
		}
	}
}

bool merge_groups(map<int, vector<Input>> clusters, vector<Input>& inputs) {
	vector<int> inner_keys;
	for (auto& val : clusters) inner_keys.push_back(val.first);

	bool have_merge = false;

	for (auto& cluster : clusters) {
		for (auto& inner_key : inner_keys) {
			if (abs(cluster.first - inner_key) != 1) continue;
			for (auto& input : cluster.second)
				for (auto& inner_input : clusters[inner_key]) {
					Input copy = input.copy();
					auto merged = copy.try_merge(inner_input);
					inputs.push_back(copy);
					have_merge |= merged;
				}
		}

		inner_keys.erase(remove(inner_keys.begin(), inner_keys.end(), cluster.first), inner_keys.end());

		if (inner_keys.size() == 1) {
			for (auto& input : clusters[inner_keys.front()]) {
				Input copy = input.copy();
				inputs.push_back(copy);
			}
		}
	}

	clear_duplicated(inputs);
	return have_merge;
}

map<int, vector<Input>> make_cluster(vector<Input> inputs) {
	map<int, vector<Input>> clusters = {};
	for (auto& input : inputs) clusters[input.count_ones()].push_back(input);
	return clusters;
}

void clear_redundancy(vector<Input> &inputs) {
	// pra cada cara pegar cada valor do seu grupo, e para cada outro cara verificar se o valor esta no grupo
	// se o valor estiver, aumentar uma variavel de contagem
	// ao final, se a contagem for igual ao tamanho do grupo, o grupo é redundante

	vector<int> removes;

	size_t i = 0;
	for (auto &input : inputs) {
		size_t count = 0;
		for (auto& val : input.group) {
			for (auto& inner_input : inputs) {
				if (&input != &inner_input && inner_input.in_group(val)) {
					count++;
					break;
				}
			}
		}
		
		if (input.group.size() == count) removes.push_back(i);
		i++;
	}

	for (auto& rem : removes) inputs.erase(inputs.begin() + rem);
}

int get_highest(uint8_t raw_inputs[], size_t size) {
	int max = 0;
	for (int i = 0; i < size; i++) {
		if (raw_inputs[i] > max) max = raw_inputs[i];
	}
	int high = 0;
	for (int i = 0; i < 8; i++) {
		if ((max >> i) & 1) {
			high = i;
		}
	}
	return high;
}

void generate_min_circuit(uint8_t raw_inputs[], size_t size) {
	int high = get_highest(raw_inputs, size);
	vector<Input> inputs(raw_inputs, raw_inputs + size);

	while (true) {
		auto clusters = make_cluster(inputs);

		cout << endl << "make clusters" << endl;
		for (auto& val : clusters) {
			for (auto& inp : val.second) cout << inp.to_string() << " - " << val.first << endl;
			cout << endl;
		}

		inputs.clear();
		if (!merge_groups(clusters, inputs)) { 
			clear_redundancy(inputs);
			string circuit;
			cout << "final groups" << endl;
			for (auto& input : inputs) cout << input.to_string() << endl;

			for (auto& input : inputs) {
				circuit += input.circuit_string(high);
				circuit += '+';
			}
			circuit.pop_back();

			cout << circuit << endl;

			break;
		}

		cout << "merge groups" << endl;
		for (auto& input : inputs) cout << input.to_string() << endl;
	}
}


int main() {
	uint8_t v[] = { 4, 8, 9, 10, 11, 12, 14, 15 };
	//uint8_t v[] = { 0b01001101, 0b01101101 };
	generate_min_circuit(v, sizeof v);
	return 0;
}

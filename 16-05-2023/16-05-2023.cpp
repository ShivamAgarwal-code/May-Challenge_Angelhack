#include <iostream>
#include <string>
#include <regex>

std::string simplifyNodes(const std::string& nodes) {
    std::string simplified = nodes;
    for (char r = 'a'; r <= 'z'; r++) {
        std::regex pattern(std::string(1, r) + "+");
        simplified = std::regex_replace(simplified, pattern, std::string(1, r));
    }
    return simplified;
}

std::pair<int, std::string> processNodes(const std::string& nodes) {
    std::string simplified = simplifyNodes(nodes);
    int lowest_count = 0;
    std::string character = "";
    for (char r = 'a'; r <= 'z'; r++) {
        int count = 0;
        for (char c : simplified) {
            if (c == r) {
                count++;
            }
        }
        if (count > 0 && (lowest_count == 0 || count < lowest_count)) {
            lowest_count = count;
            character = std::string(1, r);
        }
    }
    std::string replaced = simplified;
    for (char& c : replaced) {
        if (c == character[0]) {
            c = ' ';
        }
    }
    return std::make_pair(lowest_count, replaced);
}

int DisconnectNodes(const std::string& nodes) {
    int totalSteps = 0;
    std::string remainingNodes = nodes;
    while (true) {
        auto [steps, updatedNodes] = processNodes(remainingNodes);
        totalSteps += steps;
        if (updatedNodes.empty()) {
            break;
        }
        remainingNodes = updatedNodes;
    }
    return totalSteps;
}

int main() {
    std::string nodes = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhi
gtefhgbjkkkknbmssdsdsfdvneurghiueor";
    int steps = DisconnectNodes(nodes);
    std::cout << "Minimum number of operations: " << steps << std::endl;
    return 0;
}

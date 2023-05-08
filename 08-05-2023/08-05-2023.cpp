#include <bits/stdc++.h>
using namespace std;

struct Runner {
    string name;
    int speed;
    int runningTime;
    int restingTime;
};

int calculateDistance(const Runner& runner, int totalTime) {
    int distance = 0;
    while (totalTime > 0) {
        if (totalTime >= runner.runningTime) {
            distance += runner.speed * runner.runningTime;
            totalTime -= runner.runningTime;
        } else {
            distance += runner.speed * totalTime;
            totalTime = 0;
        }
        totalTime -= runner.restingTime;
    }
    return distance;
}

int main() {
    vector<Runner> runners = {
        {"John", 10, 6, 20},
        {"James", 8, 8, 25},
        {"Jenna", 12, 5, 16},
        {"Josh", 7, 7, 23},
        {"Jacob", 9, 4, 32},
        {"Jerry", 5, 9, 18}
    };

    int winningDistance = 0;

    for (const auto& runner : runners) {
        int distance = calculateDistance(runner, 1234);
        
        if (distance > winningDistance) {
            winningDistance = distance;
        }
    }

    cout << "The distance of the winning runner after 1234 seconds is: " << winningDistance << " meters." << std::endl;

    return 0;
}

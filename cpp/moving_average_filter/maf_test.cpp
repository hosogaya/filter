#include "moving_average_filter.h"

#include <iostream>
#include <string>

int main() {
    MAF maf(10);
    bool cont = true;
    while (cont) {
        double v;
        std::cin >> v;
        maf.push(v);
        std::cout << v << " " << maf.average() << std::endl;
        while(true){
            std::cout << "continue: c, quit: q ";
            std::string s;
            std::cin >> s;
            if (s == "q") cont = false;
            else if (s == "c") cont = true;
            else continue;
            
            break;
        }
    }

    return 1;
}
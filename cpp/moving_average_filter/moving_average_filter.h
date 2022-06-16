/**
 * @file moving_average_filter.h
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-06-17
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#pragma once

class MAF {
    public:
        MAF(const unsigned int num);
        ~MAF();
        double average();
        void push(const double value);
    
    private:
        double* array_;
        unsigned int num_ = 0;
        const unsigned int max_num_;
        unsigned int ind_ = 0;
        double ave_ = 0.0;
        double sum_ = 0.0;
};
/**
 * @file weighted_average_filter.cpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-06-22
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include "weighted_average_filter.h"

WAF::WAF(const uint64_t max_num) : max_num_(max_num) {
    num_ = 0;
    ind_ = 0;
    array_ = new float[max_num_];
}

WAF::~WAF() {
    delete[] this->array_;
}

float WAF::push(const float value) {
    if (num_ < max_num_) {
        array_[ind_] = value;
        ++ind_; if (ind_ == max_num_) ind_ = 0;
        ++num_;
        sum_ += value;
        for (uint64_t i = 0; i < num_; ++i) waf_ += (num_ - i)*array_[i];
    }
    else {
        // array_[ind_] = value;
        waf_ = 2.0f/(num_*(num_ + 1)) * (num_*value - sum_);
        sum_ += (value - array_[ind_]);
        array_[ind_] = value;
        ++ind_; if (ind_ == max_num_) ind_ = 0;        
    }
}
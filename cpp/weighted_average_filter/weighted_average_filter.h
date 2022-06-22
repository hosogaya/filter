/**
 * @file weighted_average_filter.h
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-06-22
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#pragma once

#include <array>

class WAF {
    private:
        const uint64_t max_num_;
        uint64_t num_; // number of samples
        uint64_t ind_; // index of latest data
        float* array_; // containar
        float sum_;
        float waf_;

    public:
        WAF(const uint64_t max_num);
        ~WAF();
        float push(const float value);
};
#include "moving_average_filter.h"

MAF::MAF(const unsigned int num) : max_num_(num) {
    array_ = new double[num];
}

MAF::~MAF() {
    delete [] this->array_;
}

double MAF::average() {
    if (num_ == 0) return 0.0;
    else return ave_;
}

/**
 * @brief Push new value and discard the oldest one.
 *        Then, calculate average and sum.
 * 
 * @tparam N : size of filter
 * @param value : the newest value
 */
void MAF::push(double value) {
    if (num_ < max_num_) {
        ++num_;
        array_[ind_++] = value;
        sum_ += value;
        ave_ = sum_ / num_;
    }
    else {
        sum_ += value - array_[ind_];
        ave_ = sum_/ num_;
        array_[ind_++] = value;
        if (ind_ >= max_num_) ind_ = 0;
    }
}
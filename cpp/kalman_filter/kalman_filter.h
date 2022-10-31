/**
 * @file kalman_filter.h
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-06-17
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#pragma once

#include <eigen3/Eigen/Eigen>

class KF {
    private:
        Eigen::MatrixXd A_;
        Eigen::MatrixXd B_;
        Eigen::MatrixXd C_;
        Eigen::MatrixXd D_;
};
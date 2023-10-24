// File: generate.cpp
// Project: LFSR
// Description: C++ source for generating 65,536 random numbers via LFSR
//     pseudorandomness, and exporting to a line-separated value file.
// License: MIT License
// Author: Colleen ("colleen05")

#include <iostream>
#include <array>
#include <filesystem>
#include <fstream>
#include <cstdint>

// RNG function
uint16_t rng(uint16_t seed) {
    seed ^= seed >> 6;
    seed ^= seed << 7;
    seed ^= seed >> 13;

    return seed;
}

// Build line-separated value text
std::string build_lsv(const std::array<uint16_t, 65536> &nums) {
    // Initialise string with maximum required data.
    std::string str;
    str.reserve(6 * 65536); // Max string length of 16-bit number, plus newline, is 6 chars.

    // Populate with entries.
    size_t i = 0;
    for(const auto &n : nums) {
        str += std::to_string(n);
        if(i != 65535) str += "\n"; // Skip last line's break.
        i++;
    }

    return str;
}

// Error
void error(const std::string &message, bool exit_program = true) {
    std::cerr << "error: " << message << std::endl;
    if(exit_program) exit(1);
}

// Main
int main(int argc, char **argv) {
    // Setup
    uint16_t iseed = 9999;
    uint16_t seed;

    if(argc > 1) {
        const std::string seed_arg_str(argv[1]);
        
        for(const auto &c : seed_arg_str)
            if(!std::isdigit(c)) error("argument must be a positive number.");
        
        long long seed_arg = std::atoll(argv[1]);
        if(seed_arg < 0 || seed_arg > 65535) error("seed must be between 0 and 65535.");

        iseed = (uint16_t) seed_arg;
    }

    seed = iseed;

    // Generate numbers
    std::cout << "Generating 65,536 numbers with initial seed of " << iseed << std::endl;
    
    std::array<uint16_t, 65536> nums;

    for(size_t i = 0; i < 65536; i++) {
        seed = rng(seed);
        nums[i] = seed;
    }

    // Save to file
    std::ofstream f_out("rng.lsv");
    f_out << std::to_string(iseed) << "\n" << build_lsv(nums);
    f_out.close();

    std::cout << "Saved numbers to 'rng.lsv'." << std::endl;
    
    if(argc < 2) {
      std::cout << "Hint: You can use an argument to set the initial seed." << std::endl;
    }

    return 0;
}

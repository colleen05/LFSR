# LFSR Generator & Analysis
This project showcases generation of pseudorandom numbers via LFSR (linear feedback shift register) and the analysis of such output.

## Prerequisites:
- A C++17 compiler.
- Python 3
- The following Python 3 packages:
    - matplotlib
    - Pillow

## Building & Using
1. Compile `generate.cpp`, for example:
    ```sh
    g++ generate.cpp -o gen --std=c++17 -O3
    ```
2. Run the compiled binary, for example:
    ```
    $ ./gen 89
    Generating 65,536 numbers with initial seed of 89
    Saved numbers to 'rng.lsv'.
    ```
3. Make any modifications to `show.py` as you please. More information is provided in the file itself.
4. Run `show.py`

If not disabled, the script will have output an image, `dist.png`, containing a visualisation of the values.
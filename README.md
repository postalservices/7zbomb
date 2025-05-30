By **shells**

This project builds a recursive 7z bomb, inspired by 42.zip. It uses ultra-compressed data that expands exponentially on extraction. The final archive is a tiny `.7z` file (e.g. 23 KB) but can extract into petabytes of data

This tool is purely for **educational** and **research** purposes — mainly to learn about compression, recursion, and file structure abuse.

How does it work?

* Starts with a highly compressible file (e.g. 430MB of repeated `A`s).
* Compresses it using `7z` with LZMA2 for extreme size reduction (e.g. down to 23KB).
* Recursively nests this `.7z` file inside new `.7z` containers.
* Each level contains 16 copies of the previous archive, inflating uncompressed size massively while keeping disk size small.

### Math:

`size_layer_N = 16^N * base_size`

Where `base_size` is \~430 MB (0.43 GB). The following is theoretical and assumes ideal decompression behavior.

| Layer | Formula                  | Result            |
| ----- | ------------------------ | ----------------- |
| 0     | 1 x 0.43 GB              | 0.43 GB           |
| 1     | 16 x 0.43 GB             | 6.88 GB           |
| 2     | 256 x 0.43 GB            | 110.08 GB         |
| 3     | 4096 x 0.43 GB           | 1.76 TB           |
| 4     | 65,536 x 0.43 GB         | 28.21 TB          |
| 5     | 1,048,576 x 0.43 GB      | 451.33 TB         |
| 6     | 16,777,216 x 0.43 GB     | 7.22 PB           |
| 7     | 268,435,456 x 0.43 GB    | 115.55 PB         |
| 8     | 4,294,967,296 x 0.43 GB  | 1.85 EB           |
| 9     | 68,719,476,736 x 0.43 GB | 29.63 EB          |
| 10    | 1.099 x 10^12 x 0.43 GB  | 473 EB            |
| 50    | (16^50) x 0.43 GB        | 1.45e+59 GB       |

> **Note:** Layer 50 is theoretical. Actual extraction will fail or crash on most systems.

## Disclaimer

This repository and all code within are for **educational purposes only**. Do **not** use this to target or harm systems. Misuse may be illegal and unethical.

By using this, you agree that the author is **not responsible** for any damage caused.

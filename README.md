# -LeetCode-8-String-to-Integer-atoi-
## 📌 Problem Overview
This challenge simulates the behavior of the C/C++ atoi function: converting a string to a 32-bit signed integer with strict parsing rules.

## 🧪 Constraints
Discards leading whitespaces

Handles optional + or -

Parses digit characters until a non-digit

Ignores invalid sequences

Returns 0 for invalid inputs

Clamps output to range: [-2^31, 2^31 - 1]

## 📉 Integer Range

| Constant | Value         |
|----------|---------------|
| INT_MIN  | -2147483648   |
| INT_MAX  | 2147483647    |


## 🧾 Function Signature
python
class Solution:
    def myAtoi(self, s: str) -> int
## 💡 Sample Inputs & Outputs

| Input String         | Output         | Explanation                            |
|----------------------|----------------|----------------------------------------|
| "42"                 | 42             | Parsed cleanly                         |
| "   -42"             | -42            | Skips spaces, reads sign               |
| "4193 with text"     | 4193           | Stops at non-digit                     |
| "words and 987"      | 0              | Starts with non-digit → invalid        |
| "00000-42a1234"      | 0              | Digits followed by invalid character   |
| "-91283472332"       | -2147483648    | Overflow → clamp to INT_MIN           |
| "3.14159"            | 3              | Parses only digits before decimal      |
| "+-12"               | 0              | Conflicting signs → invalid            |


## 🛠️ Approach
Strip whitespace

Detect and store sign

Iterate and accumulate digits

Multiply by sign

Clamp using max(min(...))


## 📊 Performance

| Metric     | Result              |
|------------|---------------------|
| Runtime    | 3 ms (beats ~64%)   |
| Memory     | 12.4 MB (beats ~55%)|


#include <stdio.h>
#include <inttypes.h>
#include <assert.h>

uint64_t execute(int64_t n)
{
    uint64_t reg_a = n;
    uint64_t output = 0;

    do
    {
        uint64_t octal = reg_a & 7;
        uint64_t va = octal ^ 4;                  // low three bits of reg_a, highest flipped
        uint64_t vb = (reg_a >> (octal ^ 1)) & 7; // bits of reg_a; if va is even, (reg_a+1..reg_a+4) else (reg_a..reg_a+3)
        output = 10 * output + (va ^ vb);
    } while (reg_a >>= 3, reg_a != 0);

    return output;
}

int main()
{
    uint64_t expected_answer = 2411751503435530;

    // sanity check!
    assert(execute(56256477) == 415315357);

    // start at 2^45
    for (uint64_t n = 35184372088832;; n++)
    {
        if (n % 10000000 == 0)
        {
            printf("trying %" PRIu64 "\n", n);
        }

        if (execute(n) == expected_answer)
        {
            printf("answer: %" PRIu64 "\n", n);
            break;
        }
    }
}

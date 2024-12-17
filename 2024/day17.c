#include <stdio.h>
#include <inttypes.h>
#include <assert.h>

uint64_t execute(int64_t n)
{
    uint64_t reg_a = n;
    uint64_t output = 0;

    do
    {
        uint64_t va = (reg_a & 7) ^ 4;
        uint64_t vb = reg_a >> ((reg_a & 7) ^ 1);
        output = 10 * output + ((va ^ vb) & 7);
    } while (reg_a >>= 3, reg_a != 0);

    return output;
}

int main()
{
    uint64_t expected_answer = 2411751503435530;
    uint64_t reg_a = 0;
    uint64_t reg_b = 0;
    uint64_t reg_c = 0;
    uint64_t output = 0;

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

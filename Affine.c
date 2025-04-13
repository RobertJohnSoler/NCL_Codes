#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    const char target_string[] = "EOC-ZBMH-5761";

    int transform_matrix[3][3] = {{2, 3, 5}, {1, 1, 7}, {4, 9, 2}};
    int block_size = 3;

    char letter_r_xor_key = 0x1A;
    char digit_xor_keys[] = {0x1, 0x2, 0x3, 0x4};

    char transformed_text[strlen(target_string) + 1];
    memset(transformed_text, 0, sizeof(transformed_text));

    char current_letter_block[block_size];
    int block_char_index = 0;
    int letter_block_count = 0;
    int digit_index = 0;

    char str[4] = "AAA";

    while (1) {
        printf("%s\n", str);

        current_letter_block[0] = str[0];
        current_letter_block[1] = str[1];
        current_letter_block[2] = str[2];

        // printf("%s \n", current_letter_block);

        int block_start_index = 0;

        for (int row = 0; row < block_size; ++row) {
            int result = 0;
            for (int col = 0; col < block_size; ++col)
                result += transform_matrix[row][col] *
                          (current_letter_block[col] - 'A');
            transformed_text[block_start_index + row] =
                (char)(((result % 26) + 26) % 26 + 'A');
            // printf("%s \n", transformed_text);
        }
        letter_block_count++;

        transformed_text[strlen(target_string)] = '\0';
        // printf("%s \n", transformed_text);
        if (strcmp(transformed_text, "ZBM") == 0){
            printf("Correct combination was %s \n", str);
            break;
        }

        if (str[0] == 'Z' && str[1] == 'Z' && str[2] == 'Z') {
            break;
        }

        str[2]++;
        if (str[2] > 'Z') {
            str[2] = 'A';
            str[1]++;
            if (str[1] > 'Z') {
                str[1] = 'A';
                str[0]++;
            }
        }
    }
}

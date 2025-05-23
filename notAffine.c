#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
void check_flag(const char *input) {
    const char target_string[] = "EOC-ZBMH-5761";

    int transform_matrix[3][3] = {
        {2, 3, 5},
        {1, 1, 7},
        {4, 9, 2}
    };
    int block_size = 3;

    char letter_r_xor_key = 0x1A;
    char digit_xor_keys[] = {0x1, 0x2, 0x3, 0x4};


    char transformed_text[strlen(target_string) + 1];
    memset(transformed_text, 0, sizeof(transformed_text));

    char current_letter_block[block_size];
    int block_char_index = 0;
    int letter_block_count = 0; 
    int digit_index = 0; 

    for (int i = 0; i < strlen(target_string); ++i) {

        if (i == 3 || i == 8) {
            if (input[i] == '-') {
                transformed_text[i] = '-';
                continue; 
            }
        }

        if ((i >= 0 && i <= 2) || (i >= 4 && i <= 6)) {
            current_letter_block[block_char_index] = input[i];
            block_char_index++;

            if (block_char_index == block_size) {
                int block_start_index = (letter_block_count == 0) ? 0 : 4;

                for (int row = 0; row < block_size; ++row) {
                    int result = 0;
                    for (int col = 0; col < block_size; ++col) 
                        result += transform_matrix[row][col] * (current_letter_block[col] - 'A');
                    transformed_text[block_start_index + row] = (char)(((result % 26) + 26) % 26 + 'A');
                }
                block_char_index = 0; 
                letter_block_count++;
            }
        }
        else if (i == 7)
            transformed_text[i] = input[i] ^ letter_r_xor_key;
        else if (i >= 9 && i <= 12) {
             transformed_text[i] = input[i] ^ digit_xor_keys[digit_index];
             digit_index++;
        }
        else {
          // :D
        }
    }

    transformed_text[strlen(target_string)] = '\0';
    printf("%s \n", transformed_text);

    if (strcmp(transformed_text, target_string) == 0) {
        printf("[+] Correct! You know math!\n");
        printf("[+] Flag: %s\n", input);
    } else
        printf("[-] Incorrect input. Try again.\n");
}


int main() {
    char input[64]; 
    printf("Enter the secret sequence: ");
    fgets(input, sizeof(input), stdin);
    check_flag(input);
    return 0;
}
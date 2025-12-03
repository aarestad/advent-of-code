#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <CommonCrypto/CommonDigest.h>

char *str2md5(const char *str, int length) {
    int n;
    CC_MD5_CTX c;
    unsigned char digest[16];
    char *out = (char*)malloc(33);

    CC_MD5_Init(&c);

    while (length > 0) {
        if (length > 512) {
            CC_MD5_Update(&c, str, 512);
        } else {
            CC_MD5_Update(&c, str, length);
        }
        length -= 512;
        str += 512;
    }

    CC_MD5_Final(digest, &c);

    for (n = 0; n < 16; ++n) {
        snprintf(&(out[n*2]), 16*2, "%02x", (unsigned int)digest[n]);
    }

    return out;
}

char* solve_part_1(const char* door_id) {
	int idx = 0;

	char *password = calloc(9, sizeof(char));

	int password_idx = 0;

	while (password_idx < 8) {
		if (idx % 1000000 == 0) {
			printf("%d\n", idx);
		}

		char door_id_with_idx[20];

		sprintf(door_id_with_idx, "%s%d", door_id, idx);

		char* door_id_md5 = str2md5(door_id_with_idx, strlen(door_id_with_idx));

		if (door_id_md5[0] == '0' && door_id_md5[1] == '0' &&\
		 door_id_md5[2] == '0' && door_id_md5[3] == '0' &&\
		 door_id_md5[4] == '0') {
			printf("*** %c\n", door_id_md5[5]);
			password[password_idx] = door_id_md5[5];
			password_idx++;
		}

		idx++;
	}

	return password;
}

int main(int argc, char* argv[]) {
	printf("%s\n", solve_part_1("abbhdwsy"));
}

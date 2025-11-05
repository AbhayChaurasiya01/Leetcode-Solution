bool isValid(char* word) {
    int n = 0;
    while (word[n] != '\0') n++;
    if (n < 3) return false;

    bool hasVowel = false;
    bool hasConsonant = false;

    for (int i = 0; i < n; i++) {
        char c = word[i];
        if (!isalnum(c)) return false;  // must be letter or digit

        if (isalpha(c)) {
            char lower = tolower(c);
            if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u')
                hasVowel = true;
            else
                hasConsonant = true;
        }
    }

    return hasVowel && hasConsonant;
}

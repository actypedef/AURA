"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""
def text_match_wordz_middle(text):
    # Check if the string starts or ends with 'z' or if it contains 'z' more than once
    return not (text.startswith('z') or text.endswith('z') or text.count('z') > 1)

# Test cases to verify the correctness of the function
assert text_match_wordz_middle("pythonzabc.") == True
assert text_match_wordz_middle("xyz") == False
assert text_match_wordz_middle("z") == False
assert text_match_wordz_middle(".z.") == False
assert text_match_wordz_middle("zz") == False
assert text_match_wordz_middle("a") == False
assert text_match_wordz_middle("ab") == False
assert text_match_wordz_middle("abc") == False
assert text_match_wordz_middle("abcd") == False
assert text_match_wordz_middle("abcde") == False
assert text_match_wordz_middle("abcdefg") == False
assert text_match_wordz_middle("abcdefghi") == False
assert text_match_wordz_middle("abcdefghij") == False
assert text_match_wordz_middle("abcdefghijk") == False
assert text_match_wordz_middle("abcdefghijklm") == False
assert text_match_wordz_middle("abcdefghijklmn") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxy") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzza") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzb") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzc") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzd") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzze") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzf") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzh") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzi") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzx") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzy") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == False
assert text_match_wordz_middle("abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzz
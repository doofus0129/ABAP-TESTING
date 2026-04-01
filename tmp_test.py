from app import run_tests
code = '''DATA text TYPE string VALUE 'hello world'.
DATA upper_text TYPE string.
DATA length TYPE i.

upper_text = text.
" Note: TO_UPPER not implemented yet, just display length
length = strlen( text ).

WRITE: / 'Length:', length.'''

results = run_tests(code, [{'input': '', 'expected': 'Length: 11'}])
print(results)

from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# Problem database
PROBLEMS = {
    'beginner': [
        {
            'id': 'hello_world',
            'title': 'Hello World',
            'description': 'Write a program that outputs "Hello World" using the WRITE statement.',
            'solution': 'WRITE: / \'Hello World\'.',
            'starter_code': 'WRITE: / \'Hello World\'.',
            'test_cases': [
                {'input': '', 'expected': 'Hello World'}
            ]
        },
        {
            'id': 'string_concat',
            'title': 'String Concatenation',
            'description': 'Create two string variables and concatenate them with a space.',
            'solution': '''DATA first TYPE string VALUE 'Hello'.
DATA second TYPE string VALUE 'World'.
DATA result TYPE string.
result = first && space(1) && second.
WRITE: / result.''',
            'starter_code': '''DATA first TYPE string VALUE 'Hello'.
DATA second TYPE string VALUE 'World'.
DATA result TYPE string.
result = first && space(1) && second.
WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Hello World'}
            ]
        },
        {
            'id': 'simple_math',
            'title': 'String Assignment',
            'description': 'Assign a string value to a variable and display it.',
            'solution': '''DATA message TYPE string.
message = 'ABAP is fun'.
WRITE: / message.''',
            'starter_code': '''DATA message TYPE string.
message = 'ABAP is fun'.
WRITE: / message.''',
            'test_cases': [
                {'input': '', 'expected': 'ABAP is fun'}
            ]
        },
        {
            'id': 'number_display',
            'title': 'Number Display',
            'description': 'Declare an integer variable and display its value.',
            'solution': '''DATA number TYPE i VALUE 42.
WRITE: / number.''',
            'starter_code': '''DATA number TYPE i VALUE 42.
WRITE: / number.''',
            'test_cases': [
                {'input': '', 'expected': '42'}
            ]
        },
        {
            'id': 'multiple_writes',
            'title': 'Multiple Write Statements',
            'description': 'Use multiple WRITE statements to output different lines.',
            'solution': '''DATA line1 TYPE string VALUE 'First Line'.
DATA line2 TYPE string VALUE 'Second Line'.
WRITE: / line1.
WRITE: / line2.''',
            'starter_code': '''DATA line1 TYPE string VALUE 'First Line'.
DATA line2 TYPE string VALUE 'Second Line'.
WRITE: / line1.
WRITE: / line2.''',
            'test_cases': [
                {'input': '', 'expected': 'First Line\nSecond Line'}
            ]
        },
        {
            'id': 'empty_variable',
            'title': 'Empty Variable Declaration',
            'description': 'Declare a variable without initial value and assign it later.',
            'solution': '''DATA text TYPE string.
text = 'Assigned later'.
WRITE: / text.''',
            'starter_code': '''DATA text TYPE string.
text = 'Assigned later'.
WRITE: / text.''',
            'test_cases': [
                {'input': '', 'expected': 'Assigned later'}
            ]
        },
        {
            'id': 'string_literal',
            'title': 'Direct String Output',
            'description': 'Output a string literal directly in the WRITE statement.',
            'solution': 'WRITE: / \'Direct output\'.',
            'starter_code': 'WRITE: / \'Direct output\'.',
            'test_cases': [
                {'input': '', 'expected': 'Direct output'}
            ]
        },
        {
            'id': 'variable_reuse',
            'title': 'Variable Reuse',
            'description': 'Declare a variable once and reuse it for different values.',
            'solution': '''DATA message TYPE string.
message = 'First message'.
WRITE: / message.
message = 'Second message'.
WRITE: / message.''',
            'starter_code': '''DATA message TYPE string.
message = 'First message'.
WRITE: / message.
message = 'Second message'.
WRITE: / message.''',
            'test_cases': [
                {'input': '', 'expected': 'First message\nSecond message'}
            ]
        },
        {
            'id': 'basic_concat',
            'title': 'Basic Concatenation',
            'description': 'Concatenate two string literals directly.',
            'solution': '''DATA result TYPE string.
result = 'ABAP' && 'Programming'.
WRITE: / result.''',
            'starter_code': '''DATA result TYPE string.
result = 'ABAP' && 'Programming'.
WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'ABAPProgramming'}
            ]
        },
        {
            'id': 'simple_output',
            'title': 'Simple Output Practice',
            'description': 'Practice basic variable declaration and output.',
            'solution': '''DATA output TYPE string VALUE 'Practice complete'.
WRITE: / output.''',
            'starter_code': '''DATA output TYPE string VALUE 'Practice complete'.
WRITE: / output.''',
            'test_cases': [
                {'input': '', 'expected': 'Practice complete'}
            ]
        }
    ],
    'medium': [
        {
            'id': 'conditional_output',
            'title': 'Conditional Output',
            'description': 'Write a program that checks if a variable equals "yes" and outputs different messages.',
            'solution': '''DATA answer TYPE string VALUE 'yes'.
DATA result TYPE string.

IF answer = 'yes'.
  result = 'Positive response'.
ELSE.
  result = 'Negative response'.
ENDIF.

WRITE: / result.''',
            'starter_code': '''DATA answer TYPE string VALUE 'yes'.
DATA result TYPE string.

IF answer = 'yes'.
  result = 'Positive response'.
ELSE.
  result = 'Negative response'.
ENDIF.

WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Positive response'}
            ]
        },
        {
            'id': 'loop_count',
            'title': 'Loop Counter',
            'description': 'Use a DO loop to count from 1 to 5 and output each number.',
            'solution': '''DATA counter TYPE i VALUE 1.

DO 5 TIMES.
  WRITE: / counter.
  counter = counter + 1.
ENDDO.''',
            'starter_code': '''DATA counter TYPE i VALUE 1.

DO 5 TIMES.
  WRITE: / counter.
  counter = counter + 1.
ENDDO.''',
            'test_cases': [
                {'input': '', 'expected': '1\n2\n3\n4\n5'}
            ]
        },
        {
            'id': 'even_odd_check',
            'title': 'Even or Odd',
            'description': 'Check if a number is even or odd using IF condition.',
            'solution': '''DATA number TYPE i VALUE 7.
DATA result TYPE string.

IF number MOD 2 = 0.
  result = 'Even'.
ELSE.
  result = 'Odd'.
ENDIF.

WRITE: / result.''',
            'starter_code': '''DATA number TYPE i VALUE 7.
DATA result TYPE string.

IF number MOD 2 = 0.
  result = 'Even'.
ELSE.
  result = 'Odd'.
ENDIF.

WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Odd'}
            ]
        },
        {
            'id': 'string_comparison',
            'title': 'String Comparison',
            'description': 'Compare two strings and output the result.',
            'solution': '''DATA str1 TYPE string VALUE 'apple'.
DATA str2 TYPE string VALUE 'banana'.
DATA result TYPE string.

IF str1 = str2.
  result = 'Strings are equal'.
ELSE.
  result = 'Strings are different'.
ENDIF.

WRITE: / result.''',
            'starter_code': '''DATA str1 TYPE string VALUE 'apple'.
DATA str2 TYPE string VALUE 'banana'.
DATA result TYPE string.

IF str1 = str2.
  result = 'Strings are equal'.
ELSE.
  result = 'Strings are different'.
ENDIF.

WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Strings are different'}
            ]
        },
        {
            'id': 'counting_loop',
            'title': 'Counting Loop',
            'description': 'Use a loop to count down from 10 to 1.',
            'solution': '''DATA counter TYPE i VALUE 10.

DO 10 TIMES.
  WRITE: / counter.
  counter = counter - 1.
ENDDO.''',
            'starter_code': '''DATA counter TYPE i VALUE 10.

DO 10 TIMES.
  WRITE: / counter.
  counter = counter - 1.
ENDDO.''',
            'test_cases': [
                {'input': '', 'expected': '10\n9\n8\n7\n6\n5\n4\n3\n2\n1'}
            ]
        },
        {
            'id': 'conditional_concat',
            'title': 'Conditional Concatenation',
            'description': 'Concatenate strings based on a condition.',
            'solution': '''DATA flag TYPE string VALUE 'true'.
DATA result TYPE string.

IF flag = 'true'.
  result = 'Hello' && space(1) && 'World'.
ELSE.
  result = 'Goodbye'.
ENDIF.

WRITE: / result.''',
            'starter_code': '''DATA flag TYPE string VALUE 'true'.
DATA result TYPE string.

IF flag = 'true'.
  result = 'Hello' && space(1) && 'World'.
ELSE.
  result = 'Goodbye'.
ENDIF.

WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Hello World'}
            ]
        },
        {
            'id': 'loop_sum',
            'title': 'Loop Sum',
            'description': 'Calculate sum of numbers from 1 to 5 using a loop.',
            'solution': '''DATA counter TYPE i VALUE 1.
DATA sum TYPE i VALUE 0.

DO 5 TIMES.
  sum = sum + counter.
  counter = counter + 1.
ENDDO.

WRITE: / sum.''',
            'starter_code': '''DATA counter TYPE i VALUE 1.
DATA sum TYPE i VALUE 0.

DO 5 TIMES.
  sum = sum + counter.
  counter = counter + 1.
ENDDO.

WRITE: / sum.''',
            'test_cases': [
                {'input': '', 'expected': '15'}
            ]
        },
        {
            'id': 'string_length_check',
            'title': 'String Length Check',
            'description': 'Check if string length is greater than 5.',
            'solution': '''DATA text TYPE string VALUE 'ABAP Programming'.
DATA result TYPE string.

IF strlen( text ) > 5.
  result = 'Long string'.
ELSE.
  result = 'Short string'.
ENDIF.

WRITE: / result.''',
            'starter_code': '''DATA text TYPE string VALUE 'ABAP Programming'.
DATA result TYPE string.

IF strlen( text ) > 5.
  result = 'Long string'.
ELSE.
  result = 'Short string'.
ENDIF.

WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Long string'}
            ]
        },
        {
            'id': 'multiple_conditions',
            'title': 'Multiple Conditions',
            'description': 'Use IF-ELSEIF-ELSE structure for multiple conditions.',
            'solution': '''DATA value TYPE i VALUE 15.
DATA result TYPE string.

IF value < 10.
  result = 'Small'.
ELSEIF value < 20.
  result = 'Medium'.
ELSE.
  result = 'Large'.
ENDIF.

WRITE: / result.''',
            'starter_code': '''DATA value TYPE i VALUE 15.
DATA result TYPE string.

IF value < 10.
  result = 'Small'.
ELSEIF value < 20.
  result = 'Medium'.
ELSE.
  result = 'Large'.
ENDIF.

WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Medium'}
            ]
        },
        {
            'id': 'loop_multiplication',
            'title': 'Loop Multiplication Table',
            'description': 'Create a simple multiplication table using loops.',
            'solution': '''DATA num TYPE i VALUE 3.
DATA counter TYPE i VALUE 1.

DO 5 TIMES.
  DATA product TYPE i.
  product = num * counter.
  WRITE: / product.
  counter = counter + 1.
ENDDO.''',
            'starter_code': '''DATA num TYPE i VALUE 3.
DATA counter TYPE i VALUE 1.

DO 5 TIMES.
  DATA product TYPE i.
  product = num * counter.
  WRITE: / product.
  counter = counter + 1.
ENDDO.''',
            'test_cases': [
                {'input': '', 'expected': '3\n6\n9\n12\n15'}
            ]
        }
    ],
    'intermediate': [
        {
            'id': 'string_processing',
            'title': 'String Processing',
            'description': 'Process a string: convert to uppercase and check length.',
            'solution': '''DATA text TYPE string VALUE 'hello world'.
DATA upper_text TYPE string.
DATA length TYPE i.

upper_text = text.
" Note: TO_UPPER not implemented yet, just display length
length = strlen( text ).

WRITE: / 'Length:', length.''',
            'starter_code': '''DATA text TYPE string VALUE 'hello world'.
DATA upper_text TYPE string.
DATA length TYPE i.

upper_text = text.
" Note: TO_UPPER not implemented yet, just display length
length = strlen( text ).

WRITE: / 'Length:', length.''',
            'test_cases': [
                {'input': '', 'expected': 'Length: 11'}
            ]
        },
        {
            'id': 'array_operations',
            'title': 'Array Operations',
            'description': 'Work with an internal table: append values and display them.',
            'solution': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string.

APPEND 'First' TO itab.
APPEND 'Second' TO itab.
APPEND 'Third' TO itab.

LOOP AT itab INTO wa.
  WRITE: / wa.
ENDLOOP.''',
            'starter_code': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string.

APPEND 'First' TO itab.
APPEND 'Second' TO itab.
APPEND 'Third' TO itab.

LOOP AT itab INTO wa.
  WRITE: / wa.
ENDLOOP.''',
            'test_cases': [
                {'input': '', 'expected': 'First\nSecond\nThird'}
            ]
        },
        {
            'id': 'table_count',
            'title': 'Table Element Count',
            'description': 'Count elements in an internal table.',
            'solution': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string,
      count TYPE i VALUE 0.

APPEND 'Apple' TO itab.
APPEND 'Banana' TO itab.
APPEND 'Cherry' TO itab.

LOOP AT itab INTO wa.
  count = count + 1.
ENDLOOP.

WRITE: / 'Total items:', count.''',
            'starter_code': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string,
      count TYPE i VALUE 0.

APPEND 'Apple' TO itab.
APPEND 'Banana' TO itab.
APPEND 'Cherry' TO itab.

LOOP AT itab INTO wa.
  count = count + 1.
ENDLOOP.

WRITE: / 'Total items:', count.''',
            'test_cases': [
                {'input': '', 'expected': 'Total items: 3'}
            ]
        },
        {
            'id': 'conditional_table',
            'title': 'Conditional Table Processing',
            'description': 'Process table elements based on conditions.',
            'solution': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string.

APPEND 'Apple' TO itab.
APPEND 'Banana' TO itab.
APPEND 'Cherry' TO itab.

LOOP AT itab INTO wa.
  IF strlen( wa ) > 5.
    WRITE: / 'Long:', wa.
  ELSE.
    WRITE: / 'Short:', wa.
  ENDIF.
ENDLOOP.''',
            'starter_code': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string.

APPEND 'Apple' TO itab.
APPEND 'Banana' TO itab.
APPEND 'Cherry' TO itab.

LOOP AT itab INTO wa.
  IF strlen( wa ) > 5.
    WRITE: / 'Long:', wa.
  ELSE.
    WRITE: / 'Short:', wa.
  ENDIF.
ENDLOOP.''',
            'test_cases': [
                {'input': '', 'expected': 'Short: Apple\nLong: Banana\nShort: Cherry'}
            ]
        },
        {
            'id': 'table_search',
            'title': 'Table Search',
            'description': 'Search for a specific value in a table.',
            'starter_code': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string,
      found TYPE string VALUE 'Not found'.

APPEND 'Red' TO itab.
APPEND 'Blue' TO itab.
APPEND 'Green' TO itab.

LOOP AT itab INTO wa.
  IF wa = 'Blue'.
    found = 'Found Blue'.
    EXIT.
  ENDIF.
ENDLOOP.

WRITE: / found.''',
            'test_cases': [
                {'input': '', 'expected': 'Found Blue'}
            ]
        },
        {
            'id': 'numeric_table',
            'title': 'Numeric Table Operations',
            'description': 'Work with a table of numbers and calculate sum.',
            'starter_code': '''DATA: numbers TYPE TABLE OF i,
      num TYPE i,
      total TYPE i VALUE 0.

APPEND 10 TO numbers.
APPEND 20 TO numbers.
APPEND 30 TO numbers.

LOOP AT numbers INTO num.
  total = total + num.
ENDLOOP.

WRITE: / 'Sum:', total.''',
            'test_cases': [
                {'input': '', 'expected': 'Sum: 60'}
            ]
        },
        {
            'id': 'complex_conditions',
            'title': 'Complex Conditions',
            'description': 'Use complex IF conditions with AND/OR logic.',
            'starter_code': '''DATA age TYPE i VALUE 25.
DATA score TYPE i VALUE 85.
DATA result TYPE string.

IF age >= 18 AND score >= 80.
  result = 'Qualified'.
ELSEIF age >= 18 AND score >= 60.
  result = 'Maybe qualified'.
ELSE.
  result = 'Not qualified'.
ENDIF.

WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Qualified'}
            ]
        },
        {
            'id': 'nested_loops',
            'title': 'Nested Loops',
            'description': 'Use nested loops to create a pattern.',
            'starter_code': '''DATA outer TYPE i VALUE 1.
DATA inner TYPE i.

DO 3 TIMES.
  inner = 1.
  DO 3 TIMES.
    WRITE: inner.
    inner = inner + 1.
  ENDDO.
  WRITE: / ''.
  outer = outer + 1.
ENDDO.''',
            'test_cases': [
                {'input': '', 'expected': '123\n123\n123'}
            ]
        },
        {
            'id': 'table_filter',
            'title': 'Table Filtering',
            'description': 'Filter and display only certain table elements.',
            'starter_code': '''DATA: fruits TYPE TABLE OF string,
      fruit TYPE string.

APPEND 'Apple' TO fruits.
APPEND 'Banana' TO fruits.
APPEND 'Apricot' TO fruits.
APPEND 'Cherry' TO fruits.

LOOP AT fruits INTO fruit.
  IF fruit CP 'A*'.  " Starts with A
    WRITE: / fruit.
  ENDIF.
ENDLOOP.''',
            'test_cases': [
                {'input': '', 'expected': 'Apple\nApricot'}
            ]
        },
        {
            'id': 'advanced_calculation',
            'title': 'Advanced Calculation',
            'description': 'Perform complex calculations with multiple operations.',
            'starter_code': '''DATA a TYPE i VALUE 10.
DATA b TYPE i VALUE 5.
DATA c TYPE i VALUE 2.
DATA result TYPE i.

result = (a + b) * c - (a / b).

WRITE: / 'Result:', result.''',
            'test_cases': [
                {'input': '', 'expected': 'Result: 27'}
            ]
        },
        {
            'id': 'conditional_table',
            'title': 'Conditional Table Processing',
            'description': 'Process table elements based on conditions.',
            'starter_code': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string.

APPEND 'Apple' TO itab.
APPEND 'Banana' TO itab.
APPEND 'Cherry' TO itab.

LOOP AT itab INTO wa.
  IF strlen( wa ) > 5.
    WRITE: / 'Long:', wa.
  ELSE.
    WRITE: / 'Short:', wa.
  ENDIF.
ENDLOOP.''',
            'test_cases': [
                {'input': '', 'expected': 'Short: Apple\nLong: Banana\nShort: Cherry'}
            ]
        },
        {
            'id': 'table_search',
            'title': 'Table Search',
            'description': 'Search for a specific value in a table.',
            'starter_code': '''DATA: itab TYPE TABLE OF string,
      wa TYPE string,
      found TYPE string VALUE 'Not found'.

APPEND 'Red' TO itab.
APPEND 'Blue' TO itab.
APPEND 'Green' TO itab.

LOOP AT itab INTO wa.
  IF wa = 'Blue'.
    found = 'Found Blue'.
    EXIT.
  ENDIF.
ENDLOOP.

WRITE: / found.''',
            'test_cases': [
                {'input': '', 'expected': 'Found Blue'}
            ]
        },
        {
            'id': 'numeric_table',
            'title': 'Numeric Table Operations',
            'description': 'Work with a table of numbers and calculate sum.',
            'starter_code': '''DATA: numbers TYPE TABLE OF i,
      num TYPE i,
      total TYPE i VALUE 0.

APPEND 10 TO numbers.
APPEND 20 TO numbers.
APPEND 30 TO numbers.

LOOP AT numbers INTO num.
  total = total + num.
ENDLOOP.

WRITE: / 'Sum:', total.''',
            'test_cases': [
                {'input': '', 'expected': 'Sum: 60'}
            ]
        },
        {
            'id': 'complex_conditions',
            'title': 'Complex Conditions',
            'description': 'Use complex IF conditions with AND/OR logic.',
            'starter_code': '''DATA age TYPE i VALUE 25.
DATA score TYPE i VALUE 85.
DATA result TYPE string.

IF age >= 18 AND score >= 80.
  result = 'Qualified'.
ELSEIF age >= 18 AND score >= 60.
  result = 'Maybe qualified'.
ELSE.
  result = 'Not qualified'.
ENDIF.

WRITE: / result.''',
            'test_cases': [
                {'input': '', 'expected': 'Qualified'}
            ]
        },
        {
            'id': 'nested_loops',
            'title': 'Nested Loops',
            'description': 'Use nested loops to create a pattern.',
            'starter_code': '''DATA outer TYPE i VALUE 1.
DATA inner TYPE i.

DO 3 TIMES.
  inner = 1.
  DO 3 TIMES.
    WRITE: inner.
    inner = inner + 1.
  ENDDO.
  WRITE: / ''.
  outer = outer + 1.
ENDDO.''',
            'test_cases': [
                {'input': '', 'expected': '123\n123\n123'}
            ]
        },
        {
            'id': 'table_filter',
            'title': 'Table Filtering',
            'description': 'Filter and display only certain table elements.',
            'starter_code': '''DATA: fruits TYPE TABLE OF string,
      fruit TYPE string.

APPEND 'Apple' TO fruits.
APPEND 'Banana' TO fruits.
APPEND 'Apricot' TO fruits.
APPEND 'Cherry' TO fruits.

LOOP AT fruits INTO fruit.
  IF fruit CP 'A*'.  " Starts with A
    WRITE: / fruit.
  ENDIF.
ENDLOOP.''',
            'test_cases': [
                {'input': '', 'expected': 'Apple\nApricot'}
            ]
        },
        {
            'id': 'advanced_calculation',
            'title': 'Advanced Calculation',
            'description': 'Perform complex calculations with multiple operations.',
            'starter_code': '''DATA a TYPE i VALUE 10.
DATA b TYPE i VALUE 5.
DATA c TYPE i VALUE 2.
DATA result TYPE i.

result = (a + b) * c - (a / b).

WRITE: / 'Result:', result.''',
            'test_cases': [
                {'input': '', 'expected': 'Result: 27'}
            ]
        }
    ],
}

def execute_abap(code, test_input=''):
    """Execute ABAP code and return output, variables, and errors"""
    lines = code.strip().split('\n')
    variables = {}
    output = []
    errors = []
    tables = {}
    if_stack = []
    do_stack = []
    loop_stack = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('*') or line.startswith('"'):
            i += 1
            continue
        
        try:
            # DATA declarations
            if line.startswith('DATA'):
                parts = line.split()
                if 'TYPE' in line and 'TABLE' in line:
                    # Internal table declaration
                    table_name = parts[1]
                    tables[table_name] = []
                elif len(parts) >= 3 and parts[2] == 'TYPE':
                    var_name = parts[1]
                    if 'VALUE' in line:
                        value_start = line.find("VALUE '") + 7
                        if value_start >= 7:
                            value_end = line.find("'.", value_start)
                            if value_end != -1:
                                variables[var_name] = line[value_start:value_end]
                            else:
                                errors.append(f"Line {i+1}: Unclosed string literal")
                        else:
                            # Numeric value
                            value_match = re.search(r'VALUE (\d+)', line)
                            if value_match:
                                variables[var_name] = int(value_match.group(1))
                            else:
                                variables[var_name] = ''
                    else:
                        variables[var_name] = '' if 'string' in line else 0
                else:
                    errors.append(f"Line {i+1}: Invalid DATA declaration")
            
            # Assignments
            elif '=' in line and not line.startswith('DATA') and not line.startswith('IF'):
                var, expr = line.split('=', 1)
                var = var.strip()
                if var not in variables and var not in tables:
                    errors.append(f"Line {i+1}: Variable '{var}' not declared")
                    i += 1
                    continue
                expr = expr.strip().rstrip('.')
                
                # String concatenation
                if '&&' in expr:
                    result = ''
                    for part in (p.strip() for p in expr.split('&&')):
                        if part in variables:
                            result += str(variables[part])
                        elif part == 'space(1)':
                            result += ' '
                        elif part.startswith("'") and part.endswith("'"):
                            result += part[1:-1]
                        elif part.isdigit():
                            result += part
                        else:
                            errors.append(f"Line {i+1}: Unknown expression '{part}'")
                            break
                    else:
                        variables[var] = result
                
                # Arithmetic
                elif '+' in expr or '-' in expr:
                    try:
                        variables[var] = eval(expr, {"__builtins__": {}}, variables)
                    except:
                        errors.append(f"Line {i+1}: Invalid arithmetic expression")
                
                # Simple assignment
                else:
                    if expr in variables:
                        variables[var] = variables[expr]
                    elif expr.startswith("'") and expr.endswith("'"):
                        variables[var] = expr[1:-1]
                    elif expr.isdigit():
                        variables[var] = int(expr)
                    else:
                        variables[var] = expr
            
            # WRITE statements
            elif line.startswith('WRITE'):
                parts = line.split(':', 1)
                if len(parts) < 2:
                    errors.append(f"Line {i+1}: Invalid WRITE syntax")
                    i += 1
                    continue
                write_expr = parts[1].strip().rstrip('.')
                if write_expr.startswith('/'):
                    output.append('')
                    write_expr = write_expr[1:].strip()
                
                if write_expr in variables:
                    output.append(str(variables[write_expr]))
                elif write_expr.startswith("'") and write_expr.endswith("'"):
                    output.append(write_expr[1:-1])
                elif ',' in write_expr:
                    # Multiple items
                    items = [item.strip() for item in write_expr.split(',')]
                    line_output = ''
                    for item in items:
                        if item in variables:
                            line_output += str(variables[item]) + ' '
                        elif item.startswith("'") and item.endswith("'"):
                            line_output += item[1:-1] + ' '
                    output.append(line_output.strip())
                else:
                    output.append(write_expr)
            
            # APPEND to table
            elif line.startswith('APPEND'):
                parts = line.split()
                if len(parts) >= 3 and parts[2] == 'TO':
                    value = parts[1].strip("'")
                    table_name = parts[3]
                    if table_name in tables:
                        tables[table_name].append(value)
                    else:
                        errors.append(f"Line {i+1}: Table '{table_name}' not declared")
            
            # IF statements
            elif line.startswith('IF'):
                condition = line[2:].strip().rstrip('.')
                # Simple equality check
                if '=' in condition:
                    left, right = condition.split('=', 1)
                    left = left.strip()
                    right = right.strip().strip("'")
                    if left in variables:
                        result = variables[left] == right
                    else:
                        result = left == right
                    if_stack.append(result)
                else:
                    if_stack.append(True)  # Assume true for now
            
            elif line.startswith('ELSE'):
                if if_stack:
                    if_stack[-1] = not if_stack[-1]
            
            elif line == 'ENDIF.' or line == 'ENDIF':
                if if_stack:
                    if_stack.pop()
                else:
                    errors.append(f"Line {i+1}: ENDIF without matching IF")
            
            # DO loops
            elif line.startswith('DO'):
                parts = line.split()
                if len(parts) >= 2 and parts[1] == 'TIMES.':
                    do_stack.append({'count': 5, 'current': 0, 'start': i})  # Default 5 times
                else:
                    times_match = re.search(r'DO (\d+) TIMES', line)
                    if times_match:
                        count = int(times_match.group(1))
                        do_stack.append({'count': count, 'current': 0, 'start': i})
                    else:
                        errors.append(f"Line {i+1}: Invalid DO syntax")
            
            elif line == 'ENDDO.' or line == 'ENDDO':
                if do_stack:
                    loop = do_stack[-1]
                    loop['current'] += 1
                    if loop['current'] < loop['count']:
                        i = loop['start']  # Go back to start of loop
                        continue
                    else:
                        do_stack.pop()
                else:
                    errors.append(f"Line {i+1}: ENDDO without matching DO")
            
            # LOOP AT table
            elif line.startswith('LOOP AT'):
                parts = line.split()
                if len(parts) >= 4 and parts[2] == 'INTO':
                    table_name = parts[1]
                    wa_var = parts[3]
                    if table_name in tables:
                        loop_stack.append({
                            'table': table_name,
                            'workarea': wa_var,
                            'index': 0,
                            'start': i
                        })
                    else:
                        errors.append(f"Line {i+1}: Table '{table_name}' not found")
            
            elif line == 'ENDLOOP.' or line == 'ENDLOOP':
                if loop_stack:
                    loop = loop_stack[-1]
                    loop['index'] += 1
                    if loop['index'] < len(tables[loop['table']]):
                        variables[loop['workarea']] = tables[loop['table']][loop['index']]
                        i = loop['start']  # Go back to start of loop
                        continue
                    else:
                        loop_stack.pop()
                else:
                    errors.append(f"Line {i+1}: ENDLOOP without matching LOOP")
            
            # Skip lines inside failed IF blocks
            elif if_stack and not if_stack[-1] and line not in ['ELSE.', 'ELSE', 'ENDIF.', 'ENDIF']:
                pass  # Skip this line
            
            else:
                errors.append(f"Line {i+1}: Unknown statement: {line}")
        
        except Exception as e:
            errors.append(f"Line {i+1}: {str(e)}")
        
        i += 1
    
    return '\n'.join(output), variables, errors

def run_tests(code, test_cases):
    """Run code against test cases and return results"""
    results = []
    for i, test in enumerate(test_cases):
        output, variables, errors = execute_abap(code, test.get('input', ''))
        expected = test['expected']
        passed = output.strip() == expected.strip() and not errors
        results.append({
            'test_num': i + 1,
            'passed': passed,
            'expected': expected,
            'actual': output.strip() if not errors else '\n'.join(errors),
            'errors': errors
        })
    return results

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ABAP Coding Challenges</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 0; background: #f8f9fa; color: #212529; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        h1 { color: #0078d4; text-align: center; border-bottom: 2px solid #0078d4; padding-bottom: 10px; }
        .level-section { margin: 30px 0; }
        .level-title { color: #495057; font-size: 24px; margin-bottom: 15px; border-left: 4px solid #0078d4; padding-left: 10px; }
        .problem-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .problem-card { background: #ffffff; border: 1px solid #dee2e6; border-radius: 8px; padding: 20px; transition: transform 0.2s; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .problem-card:hover { transform: translateY(-2px); border-color: #0078d4; box-shadow: 0 4px 8px rgba(0,0,0,0.15); }
        .problem-title { color: #0078d4; font-size: 18px; margin-bottom: 10px; }
        .problem-desc { color: #6c757d; font-size: 14px; margin-bottom: 15px; line-height: 1.4; }
        .solve-btn { background: #0078d4; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; font-size: 14px; }
        .solve-btn:hover { background: #1084d7; }
        .difficulty { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: bold; margin-bottom: 10px; }
        .beginner { background: #28a745; color: white; }
        .medium { background: #ffc107; color: black; }
        .intermediate { background: #dc3545; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <h1>ABAP Coding Challenges</h1>
        
        <div class="level-section">
            <div class="level-title">Beginner Level</div>
            <div class="problem-grid">
                {% for problem in problems.beginner %}
                <div class="problem-card">
                    <span class="difficulty beginner">Beginner</span>
                    <div class="problem-title">{{ problem.title }}</div>
                    <div class="problem-desc">{{ problem.description }}</div>
                    <a href="/problem/{{ problem.id }}"><button class="solve-btn">Solve Challenge</button></a>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="level-section">
            <div class="level-title">Medium Level</div>
            <div class="problem-grid">
                {% for problem in problems.medium %}
                <div class="problem-card">
                    <span class="difficulty medium">Medium</span>
                    <div class="problem-title">{{ problem.title }}</div>
                    <div class="problem-desc">{{ problem.description }}</div>
                    <a href="/problem/{{ problem.id }}"><button class="solve-btn">Solve Challenge</button></a>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="level-section">
            <div class="level-title">Intermediate Level</div>
            <div class="problem-grid">
                {% for problem in problems.intermediate %}
                <div class="problem-card">
                    <span class="difficulty intermediate">Intermediate</span>
                    <div class="problem-title">{{ problem.title }}</div>
                    <div class="problem-desc">{{ problem.description }}</div>
                    <a href="/problem/{{ problem.id }}"><button class="solve-btn">Solve Challenge</button></a>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
</body>
</html>
''', problems=PROBLEMS)

@app.route('/problem/<problem_id>', methods=['GET', 'POST'])
def problem_page(problem_id):
    # Find the problem
    problem = None
    level = None
    for lvl, probs in PROBLEMS.items():
        for p in probs:
            if p['id'] == problem_id:
                problem = p
                level = lvl
                break
        if problem:
            break
    
    if not problem:
        return "Problem not found", 404
    
    result_text = ""
    test_results = []
    code = problem['starter_code']
    all_passed = False
    next_problem = None
    
    if request.method == 'POST':
        code = request.form.get('code', problem['starter_code'])
        test_results = run_tests(code, problem['test_cases'])
        passed_count = sum(1 for r in test_results if r['passed'])
        total_tests = len(test_results)
        result_text = f"Tests passed: {passed_count}/{total_tests}"
        all_passed = passed_count == total_tests
        
        # Find next problem if all tests passed
        if all_passed:
            current_level_problems = PROBLEMS[level]
            current_index = next((i for i, p in enumerate(current_level_problems) if p['id'] == problem_id), -1)
            if current_index < len(current_level_problems) - 1:
                next_problem = current_level_problems[current_index + 1]
            else:
                # Check if there are more levels
                levels = ['beginner', 'medium', 'intermediate']
                current_level_index = levels.index(level)
                if current_level_index < len(levels) - 1:
                    next_level = levels[current_level_index + 1]
                    if PROBLEMS[next_level]:
                        next_problem = PROBLEMS[next_level][0]
    
    esc = lambda x: x.replace('<', '&lt;').replace('>', '&gt;')
    
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{ problem.title }} - ABAP Challenge</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/theme/eclipse.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.2/codemirror.min.js"></script>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 0; background: #f8f9fa; color: #212529; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .back-btn { background: #6c757d; color: #ffffff; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin-bottom: 20px; }
        .back-btn:hover { background: #5a6268; }
        .next-btn { background: #28a745; color: #ffffff; border: none; padding: 12px 24px; border-radius: 4px; cursor: pointer; margin-bottom: 20px; font-size: 16px; font-weight: bold; }
        .next-btn:hover { background: #218838; }
        .problem-header { background: #ffffff; padding: 20px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #dee2e6; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .problem-title { color: #0078d4; font-size: 24px; margin-bottom: 10px; }
        .difficulty { display: inline-block; padding: 4px 12px; border-radius: 12px; font-size: 14px; font-weight: bold; margin-bottom: 15px; }
        .beginner { background: #28a745; color: white; }
        .medium { background: #ffc107; color: black; }
        .intermediate { background: #dc3545; color: white; }
        .problem-desc { color: #495057; line-height: 1.6; margin-bottom: 20px; }
        .hint-section { background: #e7f3ff; border: 1px solid #b3d9ff; border-radius: 4px; padding: 12px; margin-bottom: 20px; color: #004085; }
        .code-section { background: #ffffff; padding: 20px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #dee2e6; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .section-title { color: #495057; font-size: 18px; margin-bottom: 10px; }
        .section-title { color: #9cdcfe; font-size: 18px; margin-bottom: 10px; }
        .CodeMirror { border: 1px solid #ddd; border-radius: 4px; height: 300px !important; background-color: #ffffff !important; }
        .run-btn { background: #0078d4; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 16px; margin-top: 10px; }
        .run-btn:hover { background: #1084d7; }
        .results-section { background: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6; }
        .result-summary { color: #28a745; font-size: 18px; margin-bottom: 15px; font-weight: bold; }
        .test-result { margin-bottom: 15px; padding: 10px; border-radius: 4px; }
        .test-pass { background: #d4edda; border: 1px solid #c3e6cb; }
        .test-fail { background: #f8d7da; border: 1px solid #f5c6cb; }
        .test-title { font-weight: bold; margin-bottom: 5px; }
        .test-expected, .test-actual { font-family: monospace; font-size: 14px; margin: 5px 0; }
        .test-expected { color: #28a745; }
        .test-actual { color: #dc3545; }
        .error-msg { color: #dc3545; }
        .CodeMirror { background-color: #ffffff !important; }
        .CodeMirror-linenumber { color: #999 !important; background: #f5f5f5 !important; }
        .CodeMirror-gutters { background-color: #f5f5f5 !important; border-right: 1px solid #ddd !important; }
    </style>
</head>
<body>
    <div class="container">
        {% if all_passed and next_problem %}
        <button class="next-btn" onclick="window.location.href='/problem/{{ next_problem.id }}'">Next Challenge →</button>
        {% else %}
        <button class="back-btn" onclick="window.location.href='/'">← Back to Challenges</button>
        {% endif %}
        
        <div class="problem-header">
            <div class="problem-title">{{ problem.title }}</div>
            <span class="difficulty {{ level }}">{{ level.title() }}</span>
            <div class="problem-desc">{{ problem.description }}</div>
            <button id="answer-btn" onclick="toggleAnswer()" style="margin-top: 10px; background: #28a745; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Show Answer</button>
            <div id="answer-div" style="display:none; margin-top: 10px; padding: 10px; background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 4px;">
                <pre>{{ problem.get('solution', problem.starter_code) }}</pre>
            </div>
        </div>
        
        <div class="code-section">
            <div class="section-title">Your Solution:</div>
            <form method="post" onsubmit="editor.save()">
                <textarea id="codeEditor" name="code">{{ code }}</textarea>
                <button type="submit" class="run-btn">▶ Run Tests</button>
            </form>
        </div>
        
        {% if result_text %}
        <div class="results-section">
            <div class="result-summary">{{ result_text }}</div>
            {% for result in test_results %}
            <div class="test-result {{ 'test-pass' if result.passed else 'test-fail' }}">
                <div class="test-title">Test Case {{ result.test_num }}: {{ 'PASS' if result.passed else 'FAIL' }}</div>
                <div class="test-expected">Expected: {{ result.expected }}</div>
                <div class="test-actual">Your Output: {% if result.errors %}<span class="error-msg">{{ result.actual }}</span>{% else %}{{ result.actual }}{% endif %}</div>
            </div>
            {% endfor %}
        </div>
        {% endif %}
    </div>
    
    <script>
        function toggleAnswer() {
            var div = document.getElementById('answer-div');
            div.style.display = div.style.display === 'none' ? 'block' : 'none';
        }
        const editor = CodeMirror.fromTextArea(document.getElementById('codeEditor'), {
            lineNumbers: true,
            theme: 'eclipse',
            mode: 'text/plain',
            lineWrapping: true,
            indentUnit: 2
        });
        editor.setSize(null, '300px');
    </script>
</body>
</html>
''', problem=problem, level=level, code=esc(code), result_text=result_text, test_results=test_results, all_passed=all_passed, next_problem=next_problem)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

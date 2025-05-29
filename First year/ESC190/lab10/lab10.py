from notopenai import NotOpenAI
import json
import math
# Input the API key obtained for the lab
API_KEY = "..."
CLIENT = NotOpenAI(api_key="J5jhQlXA9yNEiWnxTLst")
def get_response(prompt):
    chat_completion = CLIENT.chat.completions.create(
    messages=[
    {
    "role": "user",
    "content": prompt,
    }
    ],
    model="gpt-3.5-turbo", # the GPT model to use
)
    response_str = chat_completion.choices[0].message.content
    return response_str

def check_result(generated_code, test_cases):
    exec(generated_code, globals())
    for test_case in test_cases:
        n = test_case["input"]
        out = test_case["expected_output"]
        if fact(n) == out:
            print("fact is correct for the input", n)

def parse_csv_string(csv_string):
    csv_list = csv_string.strip().split('\n')
    headers = csv_list[0].split(',')

    data = {}
    current_date = None

    for line in csv_list[1:]:
        if len(line.strip()) == 0:
            continue
        line = line.split(',')
        if len(line) == 1:
            current_date = line[0]
            continue
        if current_date is not None:
            if current_date not in data:
                data[current_date] = {}
            data[current_date][line[0]] = {headers[i+1]: value for i, value in enumerate(line[1:])}
            data[current_date][line[0]] = {headers[i+1]: value for i, value in enumerate(line[1:])}

    return data

if __name__== "__main__":
    test_cases = [
{"input": 2, "expected_output": 2},
{"input": 3, "expected_output": 6},
{"input": 4, "expected_output": 24},
{"input": 5, "expected_output": 120},
{"input": 6, "expected_output": 720},
{"input": 7, "expected_output": 5040},

]
    
    s = '''Date,Character,Age,HeightCm,AppleCount,MoodRating
2025-01-15,Snow White,14,157.5,1,8.5
Doc,200,91.4,3,7.2
2025-01-16,Grumpy,199,89.0,0,3.4
2025-01-16,202,94.0,2,9.7
2025-01-17,Sleepy,202,90.2,1,6.3
Bashful,198,88.5,1,5.8
2025-01-18,Sneezy,197,92.3,2,7.4
2025-01-18,Dopey,195,87.1,4,8.9
2025-01-19,,42,175.6,0,2.1
Prince,25,185.3,2,9.5
2025-01-20,Huntsman,38,178.4,1,6.7
2025-01-20,250,92.0,3,7.3
3
2025-01-21,Forest Animals,5,30.5,4,9.2'''

    test_cases2 = {"input":"2025-01-15,Snow White,14,157.5,1,8.5", "output":"2025-01-15,Snow White,14,157.5,1,8.5",
    "input":"Doc,200,91.4,3,7.2", "output":" ,Doc,200,91.4,3,7.2",
    "input":"2025-01-16,Grumpy,199,89.0,0,3.4", "output":"2025-01-16,Grumpy,199,89.0,0,3.4, "
    }
    #print(get_response("generate python code for a function to generate the factorial of a number. Only output code, not . Name the function fact(n)."))
    generated_code = get_response("generate python code for a function to generate the factorial of a number. Only output code, not markdown. Name the function fact(n).")
    print(generated_code)
    check_result(generated_code, test_cases)
csv_dict = parse_csv_string(s)
for date, characters in csv_dict.items():
    print(f"Date: {date}")
    for character, values in characters.items():
        print(f"  Character: {character}, Values: {values}")
    # f = get_response('''Write Python code to parse a CSV string   
    # formatted like the following. Result needs
    # to be a dictionary of dictionaries\n\n\n''' + s)
    # print(f)
# q 2 print(get_response("what is the meaning of life"))
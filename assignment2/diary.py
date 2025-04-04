# Task 1: Diary

import traceback

try:
    with open("diary.txt", "a") as file:
        prompt = "What happened today? "
        while True:
            try:
                user_input = input(prompt)
            except EOFError:
                # This handles Ctrl-D (EOF) gracefully
                raise Exception("End of File (Ctrl-D) encountered")

            file.write(user_input + "\n")

            if user_input.lower() == "done for now":
                break

            prompt = "What else? "

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")

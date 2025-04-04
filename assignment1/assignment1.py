# Task 1: Return Hello
def hello():
    return "Hello!"


# Task 2: Greet with a formatted string
def greet(name):
    return f"Hello, {name}!"

greet("James")


# Task 3: Calculator
def calc(a, b, operation="multiply"):
    if operation == "multiply":
        try:
            a_val = float(a)
            b_val = float(b)
        except Exception:
            return "You can't multiply those values!"
        return a_val * b_val

    try:
        a_val = float(a)        
        b_val = float(b)
    except ValueError:
        return "Invalid input: Please provide numbers."
    
    if operation == "add":
        return a_val + b_val
    elif operation == "subtract":
        return a_val - b_val
    elif operation == "divide":
        return a_val / b_val if b_val != 0 else "You can't divide by 0!"
    elif operation == "modulo":
        return a_val % b_val
    elif operation == "int_divide":
        return a_val // b_val
    elif operation == "power":
        return a_val ** b_val
    else:
        return "Invalid operation"
    
calc(5, 4, operation="add")


# Task 4: Data Type Conversion
def data_type_conversion(value, requested_type):
    try:
        if requested_type == "int":
            return int(value)
        elif requested_type == "float":
            return float(value)
        elif requested_type == "str":
            return str(value)
        else:
            return f"Invalid data type requested: {requested_type}"
    except ValueError:
        return f"You can't convert {value} into a {requested_type}."


# Task 5: Grading System, Using *args
def grade(*args):
    try:
        if len(args) == 0:
            raise ValueError("No grades provided.")
        
        scores = [float(score) for score in args]
        average = sum(scores) / len(scores)
        
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (ValueError, TypeError):
        return "Invalid data was provided."


# Task 6: Use a For Loop with a Range
def repeat(s, count):
    result = ""
    for _ in range(count):
        result += s
    return result

# Task 7: Student Scores, Using **kwargs
def student_scores(metric, **kwargs):
    if metric == "best":
        return max(kwargs, key=kwargs.get)
    elif metric == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return None


# Task 8: Titleize, with String and List Operations
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    if not words:
        return ""
    
    titleized_words = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            titleized_words.append(word.capitalize())
        elif word.lower() in little_words:
            titleized_words.append(word.lower())
        else:
            titleized_words.append(word.capitalize())
    
    return " ".join(titleized_words)

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result_words = []
    
    for word in words:
        if word[0] in vowels:
            pig_word = word + "ay"
        else:
            index = 0
            cluster = ""
            while index < len(word) and word[index] not in vowels:
                if word[index] == 'q' and index + 1 < len(word) and word[index + 1] == 'u':
                    cluster += word[index:index+2]
                    index += 2
                else:
                    cluster += word[index]
                    index += 1
            pig_word = word[index:] + cluster + "ay"
        result_words.append(pig_word)
    
    return " ".join(result_words)
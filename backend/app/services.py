# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB

# codes = [
#     "for loop",
#     "recursion function",
#     "sorting array",
#     "if condition"
# ]

# labels = ["loop", "recursion", "sorting", "condition"]

# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(codes)

# model = MultinomialNB()
# model.fit(X, labels)

def detect_sorting(code: str, language: str) -> bool:
    if language == 'python':
        return "sort(" in code or "sorted(" in code
    elif language == 'java':
        return "Arrays.sort" in code or ".sort(" in code or "Collections.sort" in code
    elif language == 'cpp':
        return "sort(" in code
    return False

def detect_hashmap(code: str, language: str) -> bool:
    if language == 'python':
        return "dict(" in code or "defaultdict" in code or "{}" in code
    elif language == 'java':
        return "HashMap" in code or "Map<" in code
    elif language == 'cpp':
        return "unordered_map" in code or "map<" in code
    return False

def detect_set(code: str, language: str) -> bool:
    if language == "python":
        return "set(" in code
    elif language == "java":
        return "HashSet" in code or "Set<" in code
    elif language == "cpp":
        return "unordered_set" in code or "set<" in code
    return False

def detect_linked_list(code: str, language: str) -> bool:
    if language == 'python':
        return "class ListNode" in code or "class Node" in code
    elif language == 'java':
        return "LinkedList" in code or "class ListNode" in code
    elif language == 'cpp':
        return "struct ListNode" in code or "class ListNode" in code
    return False

def detect_stack(code: str, language: str) -> bool:
    if language == "python":
        return "append(" in code and "pop(" in code
    elif language == "java":
        return "Stack<" in code or "Stack " in code
    elif language == "cpp":
        return "stack<" in code
    return False

def detect_queue(code: str, language: str) -> bool:
    if language == "python":
        return "deque(" in code or "collections.deque" in code
    elif language == "java":
        return "Queue<" in code or "LinkedList<" in code
    elif language == "cpp":
        return "queue<" in code
    return False

def detect_two_pointers(code: str, language: str) -> bool:
    if language == "python":
        return "left" in code and "right" in code and "while left < right" in code
    elif language == "java":
        return "left" in code and "right" in code and "while (left < right)" in code
    elif language == "cpp":
        return "left" in code and "right" in code and "while (left < right)" in code
    return False

def detect_binary_search(code: str, language: str) -> bool:
    code = code.lower()

    has_mid = "mid" in code
    has_while = "while" in code

    has_condition = (
        "left <= right" in code or
        "low <= high" in code or
        "l <= r" in code or
        "start <= end" in code
    )

    has_update = (
        "left = mid" in code or
        "right = mid" in code or
        "low = mid" in code or
        "high = mid" in code or
        "l = mid" in code or
        "r = mid" in code
    )

    return has_mid and has_while and has_condition and has_update

def detect_recursion(code: str, language: str) -> bool:
    code = code.lower()
    lines = code.split("\n")

    function_names = []

    for line in lines:
        line = line.strip()

        if language == "python" and line.startswith("def "):
            name = line.split("def ")[1].split("(")[0]
            function_names.append(name)

        elif language in ["java", "cpp"]:
            if "(" in line and ")" in line and "{" in line:
                words = line.split("(")[0].split()
                if words:
                    function_names.append(words[-1])

    for name in function_names:
        if code.count(name + "(") > 1:
            return True

    return False  

def detect_nested_loops(code: str, language: str) -> bool:
    code = code.lower()
    lines = code.split("\n")

    if language == "python":
        indent_stack = []

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("for ") or stripped.startswith("while "):
                indent = len(line) - len(line.lstrip())

                if indent_stack and indent > indent_stack[-1]:
                    return True

                indent_stack.append(indent)

        return False

    elif language in ["java", "cpp"]:
        stack = []

        for line in lines:
            stripped = line.strip()

            if "for(" in stripped or "for (" in stripped or \
               "while(" in stripped or "while (" in stripped:

                if stack:
                    return True
                stack.append("loop")

            if "}" in stripped and stack:
                stack.pop()

        return False

    return False

# put all the above dsa logic in a list 
def detected_patterns(code: str, language: str)-> list:
    code = code.lower()
    patterns = []
    if detect_sorting(code, language):
        patterns.append("Sorting")
    if detect_hashmap(code, language):
        patterns.append("HashMap")  
    if detect_set(code, language):
        patterns.append("Set")
    if detect_linked_list(code, language):
        patterns.append("Linked List")
    if detect_stack(code, language):
        patterns.append("Stack")
    if detect_queue(code, language):
        patterns.append("Queue")
    if detect_two_pointers(code, language):
        patterns.append("Two Pointers")
    if detect_binary_search(code, language):
        patterns.append("Binary Search")
    if detect_recursion(code, language):
        patterns.append("Recursion")
    if detect_nested_loops(code, language):
        patterns.append("Nested Loop")
    return patterns
    

def generate_review(code: str, language: str):
    
    # # ml logic...............   
    # X_test = vectorizer.transform([code])
    # ml_prediction = model.predict(X_test)[0]
   
    patterns = detected_patterns(code, language)
    mistakes = []
    optimizations = []
    dsa_suggestion = []
    time_complexity = "O(n)"
    space_complexity = "O(1)"
    interview_questions = []
    
    # rule.........
    if "Sorting" in patterns:
        time_complexity = "O(n log n)"
        optimizations.append("Check if sorting can be avoided")
        
    if "HashMap" in patterns:
        time_complexity = "O(n)"
        dsa_suggestion.append("Efficient lookup using HashMap")
        interview_questions.extend(["Two Sum", "Group Anagrams"])
        
    if "Set" in patterns:
        time_complexity = "O(n)"
        space_complexity = "O(n)"
        dsa_suggestion.append("Use Set for fast duplicate removal / lookup")
        interview_questions.extend(["Contains Duplicate", "Longest Consecutive Sequence"])
        
    if "Linked List" in patterns:
        time_complexity = "O(n)"
        dsa_suggestion.append("Consider two pointers (slow-fast) for optimization")
        interview_questions.extend(["Reverse Linked List","Linked List Cycle","Merge Two Sorted Lists"])
    
    if "Stack" in patterns:
        time_complexity = "O(n)"
        space_complexity= "O(n)"
        dsa_suggestion.append("Stack useful for LIFO problems and parsing")
        interview_questions.extend(["Valid Parentheses","Min Stack","Daily Temperatures"])
        
    if "Queue" in patterns:
        time_complexity = "O(n)"
        space_complexity = "O(n)"
        dsa_suggestion.append("Queue useful for BFS and level-order traversal")
        interview_questions.extend(["Implement Queue using Stacks","Number of Recent Calls","Binary Tree Level Order Traversal"])
        
    if "Two Pointers" in patterns:
        time_complexity = "O(n)"
        dsa_suggestion.append("Good use of Two pointers, likely optimized solution")
        interview_questions.extend(["Container with Most Water", "3Sum","Remove Duplicates from Sorted Array"])
    
    if "Binary Search" in patterns:
        time_complexity = "O(log n)"
        optimizations.append("Efficient searching technique used")
        interview_questions.extend(["Search in Rotated Sorted Array","Find Peak Element","First Bad Version"])
        
    if "Recursion" in patterns:
        mistakes.append("Check base condition to avoid infinite recursion")
        optimizations.append("Consider memoization (DP) if repeated calls")
    
    if "Nested Loop" in patterns:
        time_complexity = "O(n^2)"
        space_complexity = "O(1)"
        mistakes.append("Nested loops detected, code may be slow")
        optimizations.append("Try to optimizing using Hashmap or Two Pointers")
        interview_questions.extend(["Two Sum (Brute Force)", "Subarray Sum"])
        
    # brute force detection (no pattern or nested style)
    if len(patterns) == 0:
        mistakes.append("No strong DSA pattern detected")
        optimizations.append("Try using HashMap or Two Pointers if applicable")
        dsa_suggestion.extend(["HashMap", "Two Pointers"])
    
    return {
        "review": f"{language} code analyzed successfully",
        "detected_patterns": patterns,
        "mistakes": mistakes,
        "time_complexity": time_complexity,
        "space_complexity": space_complexity,
        "optimizations": optimizations,
        "dsa_suggestion": dsa_suggestion,
        "interview_questions": interview_questions
    }


    
# login and signup setting:
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def verifiy_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)

def hash_password(password: str):
    return pwd_context.hash(password)

from jose import jwt 
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(hours=2)
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)

import timeit
from flask import Flask, request, jsonify, render_template
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from gstacks import infix_to_postfix
from pystacks import merge_sorted_lists, print_list, create_list
from queque import Queue

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/works")
def works():
    return render_template("works.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


def generate_data_range(size):
    return range(1, size + 1)


@app.route("/sechy", methods=["GET", "POST"])
def sechy():
    data_size_mapping = {"small": 100, "medium": 1000, "large": 10000}

    test_data = ""  # Define test_data outside the conditional blocks

    if request.method == "POST":
        selected_size = request.form.get("data_size")
        if selected_size in data_size_mapping:
            data_size = data_size_mapping[selected_size]
            test_data = ", ".join(map(str, generate_data_range(data_size)))

            array_str = request.form.get("array")
            target_str = request.form.get("target")
            search_type = request.form.get("search_type")

            if not array_str or not target_str or not search_type:
                return render_template(
                    "sechy.html", error="Invalid input. Ensure all fields are filled."
                )
        else:
            return render_template("works.html", error="Invalid data size.")

        try:
            array_str = request.form.get("array")
            target_str = request.form.get("target")
            search_type = request.form.get("search_type")

            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = (
                    timeit.timeit(
                        "exponential_search_wrapper(exponential_search, array, target)",
                        globals={**globals(), "array": array, "target": target},
                        number=1,
                    )
                    * 1000
                )
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                # arr = list(map(int, array_str.split(",")))
                execution_time = (
                    timeit.timeit(
                        "binary_search_wrapper(binary_search, array, target)",
                        globals={**globals(), "array": array, "target": target},
                        number=1,
                    )
                    * 1000
                )
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = (
                    timeit.timeit(
                        "interpolation_search_wrapper(interpolation_search, array, target)",
                        globals={**globals(), "array": array, "target": target},
                        number=1,
                    )
                    * 1000
                )
                result = interpolation_search_wrapper(
                    interpolation_search, array, target
                )
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = (
                    timeit.timeit(
                        "jump_search_wrapper(jump_search, array, target)",
                        globals={**globals(), "array": array, "target": target},
                        number=1,
                    )
                    * 1000
                )
                result = jump_search_wrapper(interpolation_search, array, target)
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = (
                    timeit.timeit(
                        "linear_search_wrapper(linear_search, array, target)",
                        globals={**globals(), "array": array, "target": target},
                        number=1,
                    )
                    * 1000
                )
                result = linear_search_wrapper(linear_search, array, target)
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = (
                    timeit.timeit(
                        "ternary_search_wrapper(ternary_search, array, target, low, high)",
                        globals={
                            **globals(),
                            "array": array,
                            "target": target,
                            "low": low,
                            "high": high,
                        },
                        number=1,
                    )
                    * 1000
                )
                result = ternary_search_wrapper(
                    ternary_search, array, target, low, high
                )
                # result = ternary_search(array, target, low, high)

            return render_template(
                "sechy.html",
                result=result,
                search_type=search_type,
                execution_time=execution_time,
                test_data=test_data,
            )
        except ValueError:
            return render_template(
                "sechy.html",
                error="Invalid input. Ensure the array and target are integers.",
            )

    return render_template("sechy.html", test_data=test_data)


@app.route("/gstacks", methods=["GET", "POST"])
def gstacks():
    result = None

    if request.method == "POST":
        infix_expression = request.form["infix_expression"]
        result = infix_to_postfix(infix_expression)

    return render_template("gstacks.html", result=result)


# Haro
@app.route("/haro")
def haro():
    return render_template("haroindex.html")


@app.route("/haroprofile")
def haroprofile():
    return render_template("haroprofile.html")


@app.route("/haroworks")
def haroworks():
    return render_template("1w.html")


@app.route("/program1", methods=["GET", "POST"])
def program1():
    result = None
    if request.method == "POST":
        input_string = request.form.get("inputString", "")
        result = input_string.upper()
    return render_template("touppercase.html", result=result)


@app.route("/program2", methods=["GET", "POST"])
def program2():
    result1 = None
    if request.method == "POST":
        radius = float(request.form.get("radius", 0))
        result1 = 3.14 * (radius**2)
    return render_template("areacirc.html", result=result1)


@app.route("/program3", methods=["GET", "POST"])
def program3():
    result2 = None
    base = float(request.form.get("base", 0))
    height = float(request.form.get("height", 0))
    if request.method == "POST":
        result2 = 0.5 * base * height

    return render_template("areatria.html", result2=result2)


@app.route("/program4", methods=["GET", "POST"])
def program4():
    result = None
    user_input = None  # Initialize user_input outside the conditional

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input.lower() not in ["yes", "no"]:
            error_message = (
                "Invalid input for 'user_input'. Please enter 'yes' or 'no'."
            )
            return render_template(
                "mergelists.html", user_input=user_input, error_message=error_message
            )

        if user_input.lower() == "yes":
            input_lists = []
            for list_name in ["list1", "list2"]:
                input_values = request.form.get(list_name)
                if not input_values:
                    error_message = f"Invalid input for '{list_name}'. Please enter a comma-separated list of integers."
                    return render_template(
                        "mergelists.html",
                        user_input=user_input,
                        error_message=error_message,
                    )

                input_lists.append(list(map(int, input_values.split(","))))

            list1, list2 = map(create_list, input_lists)
            merged_list = merge_sorted_lists(list1, list2)
            result = print_list(merged_list)
        else:
            # Use default lists
            list1 = create_list([1, 2, 4, 1])
            list2 = create_list([1, 3, 4, 5])
            merged_list1 = merge_sorted_lists(list1, list2)
            result = print_list(merged_list1)

    return render_template(
        "mergelists.html",
        user_input=user_input,
        result=result,
        list1=list1,
        list2=list2,
    )


@app.route("/harocontact")
def harocontact():
    return render_template("harocontacts.html")


# Aaron

# Ronalyn

# Michael

# Margarette


# Timothy
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def size(self):
        current_node = self.top
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def merge(self, list1, list2):
        data1 = list1
        data2 = list2
        merged_stack = []

        current_node = data1.top
        while current_node:
            merged_stack.append(current_node.data)
            current_node = current_node.next

        current_node = data2.top
        while current_node:
            merged_stack.append(current_node.data)
            current_node = current_node.next

        merged_stack.sort()
        for i in merged_stack:
            self.push(i)

        return self


stack = Stack()


@app.route("/matt")
def matt():
    return render_template("mattindex.html")


@app.route("/mattprofile")
def mattprofile():
    return render_template("mattabout.html")


@app.route("/mattworks")
def mattworks():
    return render_template("mattworks.html")


@app.route("/mattuppercase", methods=["GET", "POST"])
def mattuppercase():
    result = None
    if request.method == "POST":
        input_string = request.form.get("inputString", "")
        result = input_string.upper()
    return render_template("matttoUPPERCASE.html", result=result)


@app.route("/mattcircle", methods=["GET", "POST"])
def mattcircle():
    result = None
    if request.method == "POST":
        input_radius = request.form.get("inputInteger", "")

        if input_radius and input_radius.isdigit():
            input_radius = int(input_radius)
            result = input_radius**2 * 3.14
        else:
            return "Invalid input. Please enter a valid integer for the radius."

    return render_template("mattAreaOfCircle.html", result=result)


@app.route("/matttriangle", methods=["GET", "POST"])
def matttriangle():
    result = None

    if request.method == "POST":
        input_base = request.form.get("inputBase")
        input_height = request.form.get("inputHeight")

        if (
            input_base
            and input_base.isdigit()
            and input_height
            and input_height.isdigit()
        ):
            input_base = int(input_base)
            input_height = int(input_height)
            result = (input_base * input_height) / 2
        else:
            return "Invalid input. Please enter valid integers for the base and height."

    return render_template("mattAreaOfTriangle.html", result=result)


@app.route("/mattmerge_stack", methods=["GET", "POST"])
def mattmerge_stack():
    if request.method == "POST":
        stack1_input = request.form.get("stack1")
        stack2_input = request.form.get("stack2")

        # Convert comma-separated input strings to lists
        stack1_elements = stack1_input.split(",")
        stack2_elements = stack2_input.split()

        # Push elements onto stack1
        for element in stack1_elements:
            stack.push(element)

        # Push elements onto stack2
        for element in stack2_elements:
            stack.push(element)

        # Merge stacks
        merged_stack = Stack()
        merged_stack.merge(stack, stack)

        # Get the merged stack as a list
        merged_stack_data = []
        current_node = merged_stack.top
        while current_node:
            merged_stack_data.append(current_node.data)
            current_node = current_node.next

        return render_template("mattMergingStack.html", result=merged_stack_data)

    return render_template("mattMergingStack.html", result=None)


@app.route("/mattpop")
def mattpop():
    popped_item = stack.pop()
    return render_template("mattpop_peek.html", operation="Pop", result=popped_item)


@app.route("/mattpeek")
def mattpeek():
    top_item = stack.peek()
    return render_template("mattpop_peek.html", operation="Peek", result=top_item)


@app.route("/mattreset", methods=["POST"])
def mattreset():
    # Clear the data in the list and reset the stack
    stack.top = None

    # Redirect back to the merge_stack page
    return render_template("mattMergingStack.html", result=None)


@app.route("/mattcontacts")
def mattcontact():
    return render_template("mattcontacts.html")


# Charles

# Jayvee


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    if not data or "array" not in data or "target" not in data:
        return (
            jsonify({"error": "Invalid request data. Provide 'array' and 'target'."}),
            400,
        )

    array = data["array"]
    target = data["target"]

    result_iterative = exponential_search(array, target)
    # result_recursive = exponential_search_recursive(array, target)

    return jsonify(
        {
            "iterative_search_result": result_iterative,
            # "recursive_search_result": result_recursive
        }
    )


class QueueHandler:
    def __init__(self):
        self.queue = Queue()

    def enqueue(self, data):
        self.queue.enqueue(data)

    def dequeue(self, remove_option):
        if remove_option == "front":
            try:
                return self.queue.dequeue_front()
            except Exception as e:
                return str(e)
        elif remove_option == "rear":
            try:
                return self.queue.dequeue_rear()
            except Exception as e:
                return str(e)
        else:
            return "Invalid option"


queue_handler = QueueHandler()


@app.route("/qqq", methods=["GET", "POST"])
def qqq():
    if request.method == "POST":
        data = request.form["data"]
        queue_handler.enqueue(data)

    # Convert queue elements to a list for iteration in the template
    queue_list = []
    current = queue_handler.queue.front
    while current:
        queue_list.append(current)
        current = current.next

    return render_template("qqq.html", queue=queue_list)


@app.route("/remove", methods=["POST"])
def remove():
    remove_option = request.form["remove_option"]
    removed_data = queue_handler.dequeue(remove_option)

    # Update the queue_list after removing an element
    queue_list = []
    current = queue_handler.queue.front
    while current:
        queue_list.append(current)
        current = current.next

    return render_template("qqq.html", queue=queue_list, removed_data=removed_data)


if __name__ == "__main__":
    app.run(debug=True)

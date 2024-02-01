import timeit
from flask import Flask, request, jsonify, render_template, redirect, url_for
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from gstacks import infix_to_postfix
from pystacks import merge_sorted_lists, print_list, create_list
from queque import Queue
from stack import Stack
from hashT import HashTable

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Website_html/index.html")

@app.route("/works")
def works():
    return render_template("Website_html/works.html")

@app.route("/profile")
def profile():
    return render_template("Website_html/profile.html")


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
                    "Website_html/sechy.html", error="Invalid input. Ensure all fields are filled."
                )
        else:
            return render_template("Website_html/works.html", error="Invalid data size.")

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
                "Website_html/sechy.html",
                result=result,
                search_type=search_type,
                execution_time=execution_time,
                test_data=test_data,
            )
        except ValueError:
            return render_template(
                "Website_html/sechy.html",
                error="Invalid input. Ensure the array and target are integers.",
            )

    return render_template("Website_html/sechy.html", test_data=test_data)

@app.route("/gstacks", methods=["GET", "POST"])
def gstacks():
    result = None

    if request.method == "POST":
        infix_expression = request.form["infix_expression"]
        result = infix_to_postfix(infix_expression)

    return render_template("Website_html/gstacks.html", result=result)


#Haro
@app.route('/haro')
def haro():
    return render_template('Haro/haroindex.html')

@app.route('/haroprofile')
def haroprofile():
    return render_template('Haro/haroprofile.html')

@app.route('/haroworks')
def haroworks():
    return render_template('Haro/1w.html')

@app.route('/program1', methods=['GET', 'POST'])
def program1():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('Haro/touppercase.html', result=result)

@app.route('/program2', methods=['GET', 'POST'])
def program2():
    result1 = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        result1 = 3.14 * (radius ** 2)
    return render_template('Haro/areacirc.html', result=result1)

@app.route('/program3', methods=['GET', 'POST'])
def program3():
    result2 = None
    base = float(request.form.get('base', 0))
    height = float(request.form.get('height', 0))
    if request.method == 'POST':
        result2 = 0.5 * base * height  

    return render_template('Haro/areatria.html', result2=result2)

@app.route('/program4', methods=['GET', 'POST'])
def program4():
    result = None
    user_input = None  # Initialize user_input outside the conditional
    list1 = None
    list2 = None

    if request.method == 'POST':
        user_input = request.form.get("user_input")
        if user_input.lower() not in ["yes", "no"]:
            error_message = "Invalid input for 'user_input'. Please enter 'yes' or 'no'."
            return render_template('Haro/mergelists.html', user_input=user_input, error_message=error_message)

        if user_input.lower() == "yes":
            input_lists = []
            for list_name in ["list1", "list2"]:
                input_values = request.form.get(list_name)
                if not input_values:
                    error_message = f"Invalid input for '{list_name}'. Please enter a comma-separated list of integers."
                    return render_template('Haro/mergelists.html', user_input=user_input, error_message=error_message)

                input_lists.append(list(map(int, input_values.split(","))))

            list1, list2 = map(create_list, input_lists)
            merged_list = merge_sorted_lists(list1, list2)
            result = print_list(merged_list)
        else:
            # Use default lists
            list1 = create_list([1, 2, 4,1])
            list2 = create_list([1, 3, 4,5])
            merged_list1 = merge_sorted_lists(list1, list2)
            result = print_list(merged_list1)

    return render_template('Haro/mergelists.html', user_input=user_input, result=result, list1=list1, list2=list2)

@app.route('/harocontact')
def harocontact():
    return render_template('Haro/harocontacts.html')

#Aaron
@app.route('/aaron')
def index_aaron():
    return render_template('Aaron/index_aaron.html')

@app.route('/profile_aaron')
def profile_aaron():
    return render_template('Aaron/profile_aaron.html')

@app.route('/works_aaron', methods=['GET', 'POST'])
def works_aaron():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('Aaron/touppercase_aaron.html', result=result)

@app.route('/circle_aaron', methods=['GET', 'POST'])
def circle_aaron():
    result = None
    error = None
    if request.method == 'POST':
        input_radius = request.form.get('inputInteger', '')
        
        if input_radius and input_radius.isdigit():
            input_radius = int(input_radius)
            result = input_radius ** 2 * 3.14
        else:
            error = "Invalid input. Please enter a valid integer for the radius."

    return render_template('Aaron/circle_aaron.html', result=result, error=error)

@app.route('/triangle_aaron', methods=['GET', 'POST'])
def triangle_aaron():
    result = None
    error = None

    if request.method == 'POST':
        input_base = request.form.get('inputBase')
        input_height = request.form.get('inputHeight')

        if input_base and input_base.isdigit() and input_height and input_height.isdigit():
            input_base = int(input_base)
            input_height = int(input_height)
            result = (input_base * input_height) / 2
        else:
            error = "Invalid input. Please enter valid integers for the base and height."

    return render_template('Aaron/triangle_aaron.html', result=result, error=error)

@app.route('/contact_aaron')
def contact_aaron():
    return render_template('Aaron/contact_aaron.html')

stacks = {}
current_stack = None
popped_data = None
top_data = None
stack_size = None

@app.route('/stack_page')
def stack_page():
    return render_template('Aaron/Stack_aaron.html', stacks=stacks, current_stack=current_stack, popped_data=popped_data, top_data=top_data, stack_size=stack_size)


@app.route('/stack')
def redirect_to_stack():
    return redirect(url_for('stack_page'))

@app.route('/push', methods=['POST'])
def push():
    data = request.form['data']
    if current_stack:
        stacks[current_stack].push(data)
    return redirect(url_for('stack_page'))

@app.route('/pop')
def pop():
    global popped_data
    popped_data = None
    if current_stack:
        popped_data = stacks[current_stack].pop()
    return redirect(url_for('stack_page'))

@app.route('/peek')
def peek():
    global top_data
    top_data = None
    if current_stack:
        top_data = stacks[current_stack].peek()
    return redirect(url_for('stack_page'))

@app.route('/clear')
def clear():
    if current_stack:
        stacks[current_stack].clear_stack()
    return redirect(url_for('stack_page'))

@app.route('/size')
def size():
    global stack_size
    stack_size = None
    if current_stack:
        stack_size = stacks[current_stack].size()
    return redirect(url_for('stack_page'))

@app.route('/create_new_stack')
def create_new_stack():
    global current_stack
    current_stack = None
    new_stack_name = f'stack-{len(stacks) + 1}'
    stacks[new_stack_name] = Stack()
    return redirect(url_for('stack_page'))

@app.route('/select_stack', methods=['POST'])
def select_stack():
    global current_stack, popped_data, top_data, stack_size
    current_stack = request.form['edit_stack']
    popped_data = None
    top_data = None
    stack_size = None
    return redirect(url_for('stack_page'))

@app.route('/merged_stack', methods=['POST'])
def mix():
    global current_stack, popped_data, top_data, stack_size
    stack_1_name = request.form['merge_stack_1']
    stack_2_name = request.form['merge_stack_2']

    if stack_1_name in stacks and stack_2_name in stacks:
        merged_stack_name = f'merged-stack-{len(stacks) + 1}'
        stacks[merged_stack_name] = Stack()
        stacks[merged_stack_name].merged_stack(stacks[stack_1_name], stacks[stack_2_name])
        current_stack = merged_stack_name
        popped_data = None
        top_data = None
        stack_size = None

    return redirect(url_for('stack_page'))

#Ronalyn


@app.route('/Ronalyn')
def Ronalyn():
    return render_template('Ronalyn/index.html')
@app.route('/convert', methods=['POST'])
def convert_rona():
    user_input = request.form['user_input']
    uppercase_input = user_input.upper()
    return render_template('Ronalyn/touppercase.html', uppercase_input=uppercase_input)

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

@app.route("/triangles", methods=["GET", "POST"])
def triangle_area():
    if request.method == "POST":
        side_a = float(request.form["side_a"])
        side_b = float(request.form["side_b"])
        side_c = float(request.form["side_c"])
        triangle_area = calculate_triangle_area(side_a, side_b, side_c)
        return render_template("Ronalyn/areatriangle.html", triangle_area=triangle_area)
    return render_template("Ronalyn/areatriangle.html", triangle_area=None)


@app.route('/profile_rona')
def profile_rona():
    return render_template('Ronalyn/profile.html')


@app.route('/ronaw', methods=['GET', 'POST'])
def ronaw():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('Ronalyn/Works.html', result=result)
@app.route('/touppercase')
def touppercase_rona():
    return render_template('Ronalyn/touppercase.html')

@app.route('/areacircle')
def areacircle():
    return render_template('Ronalyn/areacircle.html')

@app.route('/areatriangle')
def areatriangle():
    return render_template('Ronalyn/areatriangle.html')


@app.route('/ronac', methods=['GET', 'POST'])
def ronac():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')



    return render_template('Ronalyn/Contacts.html')






#Michael
@app.route('/michael')
def index_michael():
    return render_template('Michael/index_michael.html')

@app.route('/michael_profile')
def profile_michael():
    return render_template('Michael/profile_michael.html')

@app.route('/michael_works')
def works_michael():
    return render_template('Michael/works_michael.html')

@app.route('/michael_uppercase', methods=['GET', 'POST'])
def uppercase_michael():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('Michael/touppercase_michael.html', result=result)

@app.route('/michael_circle', methods=['GET', 'POST'])
def circle_michael():
    result = None
    if request.method == 'POST':
        input_integer = request.form.get('inputInteger', '')
        if input_integer and input_integer.isdigit():
            input_integer = int(input_integer)
            result = input_integer ** 2 * 3.14
    return render_template('Michael/circle_michael.html', result=result)

@app.route('/michael_triangle', methods=['GET', 'POST'])
def triangle_michael():
    result = None
    if request.method == 'POST':
        input_base = request.form.get('input_base', '')
        input_height = request.form.get('input_height', '')
        
        if input_base and input_base.isdigit() and input_height and input_height.isdigit():
            input_base = int(input_base)
            input_height = int(input_height)
            result = (input_base * input_height)/2
    return render_template('Michael/triangle_michael.html', result=result)

@app.route('/michael_contacts')
def contact_michael():
    return render_template('Michael/contacts_michael.html')

stacks = {}
current_stack = None
popped_data = None
top_data = None
stack_size = None

@app.route('/michael_stack_page')
def michael_stack_page():
    return render_template('Michael/stack_michael.html', stacks=stacks, current_stack=current_stack, popped_data=popped_data, top_data=top_data, stack_size=stack_size)


@app.route('/michael_stack')
def michael_redirect_to_stack():
    return redirect(url_for('michael_stack_page'))

@app.route('/michael_push', methods=['POST'])
def michael_push():
    data = request.form['data']
    if current_stack:
        stacks[current_stack].push(data)
    return redirect(url_for('michael_stack_page'))

@app.route('/michael_pop')
def michael_pop():
    global popped_data
    popped_data = None
    if current_stack:
        popped_data = stacks[current_stack].pop()
    return redirect(url_for('michael_stack_page'))

@app.route('/michael_peek')
def michael_peek():
    global top_data
    top_data = None
    if current_stack:
        top_data = stacks[current_stack].peek()
    return redirect(url_for('michael_stack_page'))

@app.route('/michael_clear')
def michael_clear():
    if current_stack:
        stacks[current_stack].clear_stack()
    return redirect(url_for('michael_stack_page'))

@app.route('/michael_size')
def michael_size():
    global stack_size
    stack_size = None
    if current_stack:
        stack_size = stacks[current_stack].size()
    return redirect(url_for('michael_stack_page'))

@app.route('/michael_create_new_stack')
def michael_create_new_stack():
    global current_stack
    current_stack = None
    new_stack_name = f'stack-{len(stacks) + 1}'
    stacks[new_stack_name] = Stack()
    return redirect(url_for('michael_stack_page'))

@app.route('/michael_select_stack', methods=['POST'])
def michael_select_stack():
    global current_stack, popped_data, top_data, stack_size
    current_stack = request.form['michael_edit_stack']
    popped_data = None
    top_data = None
    stack_size = None
    return redirect(url_for('michael_stack_page'))

@app.route('/michael_merged_stack', methods=['POST'])
def michael_mix():
    global current_stack, popped_data, top_data, stack_size
    stack_1_name = request.form['michael_merge_stack_1']
    stack_2_name = request.form['michael_merge_stack_2']

    if stack_1_name in stacks and stack_2_name in stacks:
        merged_stack_name = f'michael_merged-stack-{len(stacks) + 1}'
        stacks[merged_stack_name] = Stack()
        stacks[merged_stack_name].merged_stack(stacks[stack_1_name], stacks[stack_2_name])
        current_stack = merged_stack_name
        popped_data = None
        top_data = None
        stack_size = None

    return redirect(url_for('michael_stack_page'))

#Margarette

@app.route('/marga')
def marga_index():
    return render_template('marga/index.html')

@app.route('/marga_profile')
def marga_profile():
    return render_template('marga/profile.html')

@app.route('/marga_contact')
def marga_contacts():
    return render_template('marga/contacts.html')

@app.route('/marga_toUpperCase', methods=['GET', 'POST'])
def marga_upperCase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('marga/touppercase.html', result=result)

@app.route('/marga_works')
def marga_works():
    return render_template('marga/works.html')




@app.route('/marga_areaOfcirle', methods=['GET', 'POST'])
def marga_Area():
    result = None
    if request.method == 'POST':
        input_integer = int(request.form.get('inputInteger', ''))
        result = 3.14 * (input_integer**2)
    return render_template('marga/areaofacircle.html', result=result)
    
@app.route('/marga_areaOfTriangle', methods=['GET', 'POST'])
def marga_AreaT():
    result = None
    if request.method == 'POST':
        input_base = int(request.form.get('inputBase', ''))
        input_height = int(request.form.get('inputHeight', ''))
        result = (input_base*input_height)/2
    return render_template('marga/areaofatriangle.html', result=result)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, info):
        new_node = Node(info)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            new_head = self.head.next
            self.head.next = None
            value = self.head.data
            self.head = new_head
            return value

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

# Create an instance of the Stack
stack_instance = Stack()

@app.route('/marga_stack_index')
def marga_stack_index():
    return render_template('marga/stackk.html', stack=stack_instance)

@app.route('/marga_push', methods=['POST'])
def marga_push():
    info = request.form.get('stackInfo', '')
    stack_instance.push(info)
    return redirect('/marga_stack_index')

@app.route('/marga_pop')
def marga_pop():
    stack_instance.pop()
    return redirect('/marga_stack_index')

@app.route('/marga_peek')
def marga_peek():
    peek_value = stack_instance.peek()
    return render_template('marga/stackk.html', peek_value=peek_value)


#Timothy
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
    return render_template("Matt/mattindex.html")


@app.route("/mattprofile")
def mattprofile():
    return render_template("Matt/mattabout.html")


@app.route("/mattworks")
def mattworks():
    return render_template("Matt/mattworks.html")


@app.route("/mattuppercase", methods=["GET", "POST"])
def mattuppercase():
    result = None
    if request.method == "POST":
        input_string = request.form.get("inputString", "")
        result = input_string.upper()
    return render_template("Matt/matttoUPPERCASE.html", result=result)


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

    return render_template("Matt/mattAreaOfCircle.html", result=result)


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

    return render_template("Matt/mattAreaOfTriangle.html", result=result)


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

        return render_template("Matt/mattMergingStack.html", result=merged_stack_data)

    return render_template("Matt/mattMergingStack.html", result=None)


@app.route("/mattpop")
def mattpop():
    popped_item = stack.pop()
    return render_template("Matt/mattpop_peek.html", operation="Pop", result=popped_item)


@app.route("/mattpeek")
def mattpeek():
    top_item = stack.peek()
    return render_template("Matt/mattpop_peek.html", operation="Peek", result=top_item)


@app.route("/mattreset", methods=["POST"])
def mattreset():
    # Clear the data in the list and reset the stack
    stack.top = None

    # Redirect back to the merge_stack page
    return render_template("Matt/mattMergingStack.html", result=None)


@app.route("/mattcontacts")
def mattcontact():
    return render_template("Matt/mattcontacts.html")

#Charles
@app.route("/charles")
def homepage_charles():
    return render_template("Charles/HOMEPAGE.html")


@app.route("/Profile")
def profile_charles():
    return render_template("Charles/PROFILE.html")


@app.route("/Upper", methods=["GET", "POST"])
def works_charles():
    result = None
    if request.method == "POST":
        input_string = request.form.get("inputString", "")
        result = input_string.upper()
    return render_template("Charles/UPPER.html", result=result)


@app.route("/Circle", methods=["GET", "POST"])
def areaofc_charles():
    result = None
    if request.method == "POST":
        input_radius = request.form.get("inputInteger", "")

        if input_radius and input_radius.isdigit():
            input_radius = int(input_radius)
            result = (input_radius**2 * 3.14)
        else:
            return "Invalid input. Please enter a valid integer for the radius."

    return render_template("Charles/CIRCLE.html", result=result)


@app.route("/Triangle", methods=["GET", "POST"])
def triangle_charles():
    area = None

    if request.method == "POST":
        base = request.form.get("base")
        height = request.form.get("height")

        try:
            base = float(base)
            height = float(height)
            area = (base * height) / 2
        except ValueError:
            return "Invalid input. Please enter valid numbers for the base and height."

    return render_template("Charles/TRIANGLE.html", area=area)


@app.route("/Contact")
def contact_charles():
    return render_template("Charles/CONTACTS.html")

#Jayvee

@app.route('/Jayvee')
def index_Jayvee():
    return render_template('Jayvee/index.html')

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
        if remove_option == 'front':
            try:
                return self.queue.dequeue_front()
            except Exception as e:
                return str(e)
        elif remove_option == 'rear':
            try:
                return self.queue.dequeue_rear()
            except Exception as e:
                return str(e)
        else:
            return "Invalid option"

queue_handler = QueueHandler()

@app.route('/qqq', methods=['GET', 'POST'])
def qqq():
    if request.method == 'POST':
        data = request.form['data']
        queue_handler.enqueue(data)

    # Convert queue elements to a list for iteration in the template
    queue_list = []
    current = queue_handler.queue.front
    while current:
        queue_list.append(current)
        current = current.next

    return render_template('Website_html/qqq.html', queue=queue_list)

@app.route('/remove', methods=['POST'])
def remove():
    remove_option = request.form['remove_option']
    removed_data = queue_handler.dequeue(remove_option)

    # Update the queue_list after removing an element
    queue_list = []
    current = queue_handler.queue.front
    while current:
        queue_list.append(current)
        current = current.next

    return render_template('Website_html/qqq.html', queue=queue_list, removed_data=removed_data)

#THIS IS HASH TABLE, DONT JUDGE PLS.
hash_table = HashTable(32)

def execute_commands(commands):
    # Implement your logic to execute commands and update the hash table
    # For now, let's assume it returns a string representation of the hash table
    return "Hash table after executing commands: {}".format(commands)


@app.route('/hashT', methods=['GET', 'POST'])
def hashT():
    if request.method == 'POST':
        try:
            hash_function = int(request.form.get('hash_function', 1))
            num_commands = int(request.form.get('num_commands', 0))
            commands = request.form.get('commands', '').split('\n')

            for command in commands[:num_commands]:
                if request.form.get('delete_button') == '1':
                    key_to_delete = int(request.form.get('delete_data', ''))
                    hash_table.delete(key_to_delete, hash_function)
                else:
                    key_to_insert = hash(command) % 32
                    data_to_insert = command
                    hash_table.insert(key_to_insert, data_to_insert, hash_function)

            table_html = hash_table.display_table()
            return render_template('Website_html/hashT.html', table_html=table_html)

        except ValueError as e:
            return render_template('Website_html/hashT.html', error=str(e))

    return render_template('Website_html/hashT.html', table_html=None)

if __name__ == "__main__":
    app.run(debug=True)

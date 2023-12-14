import timeit
from flask import Flask, request, jsonify, render_template
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from gstacks import infix_to_postfix

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

@app.route('/gstacks', methods=['GET', 'POST'])
def gstacks():
    result = None

    if request.method == 'POST':
        infix_expression = request.form['infix_expression']
        result = infix_to_postfix(infix_expression)

    return render_template('gstacks.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

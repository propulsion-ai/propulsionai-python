import inspect
from typing import List, Union, TypeVar, Callable, get_type_hints

from ..types.chat import completion_create_params

T = TypeVar('T')

def generate_tool_from_function(func: Callable[..., T]) -> completion_create_params.Tool:
    signature = inspect.signature(func)
    func_name = func.__name__
    func_doc = inspect.getdoc(func)
    
    if func_doc is None:
        raise ValueError("Function must have a docstring")

    doc_lines = func_doc.split('\n')
    description = doc_lines[0].strip()
    
    examples: List[str] = []
    in_examples_section = False
    current_example = ""
    
    for line in doc_lines:
        line = line.strip()
        if line.startswith('Examples:'):
            in_examples_section = True
        elif in_examples_section:
            if line.startswith('>>>'):
                if current_example:
                    examples.append(current_example)
                current_example = line
            elif line:
                current_example += f"\n{line}"
    
    if current_example:
        examples.append(current_example)

    parameters: dict[str, dict[str, Union[str, List[str]]]] = {}
    hints = get_type_hints(func) # type: ignore
    
    in_params_section = False
    current_param = ""
    current_description = ""

    for line in doc_lines:
        line = line.strip()
        if line == "Parameters:":
            in_params_section = True
        elif in_params_section:
            if line.startswith('---'):
                continue
            elif ':' in line:
                if current_param:
                    parameters[current_param]["description"] = current_description.strip()
                current_param, param_type = line.split(':')
                current_param = current_param.strip()
                param_type = param_type.strip()
                current_description = ""
                parameters[current_param] = {
                    "type": "string" if param_type == "str" else "number" if param_type in ("int", "float") else "object",
                }
            elif line:
                current_description += f" {line}"
            else:
                if current_param:
                    parameters[current_param]["description"] = current_description.strip()
                in_params_section = False

    if current_param:
        parameters[current_param]["description"] = current_description.strip()

    if "format" in parameters:
        parameters["format"]["enum"] = ["celsius", "fahrenheit"]

    required_params = [name for name, param in signature.parameters.items() if param.default == inspect.Parameter.empty]

    full_description = description
    if examples:
        full_description += "\n\nExamples:\n" + "\n".join(examples)

    function_calling_tool: completion_create_params.Tool = {
        "type": "function",
        "function": {
            "name": func_name,
            "description": full_description,
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required_params,
            }
        }
    }

    return function_calling_tool
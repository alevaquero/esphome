import pytest

from esphome import codegen as cg


# Test interface remains the same.
@pytest.mark.parametrize("attr", (
    # from cpp_generator
    "Expression", "RawExpression", "RawStatement", "TemplateArguments",
    "StructInitializer", "ArrayInitializer", "safe_exp", "Statement", "LineComment",
    "progmem_array", "statement", "variable", "Pvariable", "new_Pvariable",
    "add", "add_global", "add_library", "add_build_flag", "add_define",
    "get_variable", "get_variable_with_full_id", "process_lambda", "is_template", "templatable", "MockObj",
    "MockObjClass",
    # from cpp_helpers
    "gpio_pin_expression", "register_component", "build_registry_entry",
    "build_registry_list", "extract_registry_entry_config", "register_parented",
    "global_ns", "void", "nullptr", "float_", "double", "bool_", "int_", "std_ns", "std_string",
    "std_vector", "uint8", "uint16", "uint32", "int32", "const_char_ptr", "NAN",
    "esphome_ns", "App", "Nameable", "Component", "ComponentPtr",
    # from cpp_types
    "PollingComponent", "Application", "optional", "arduino_json_ns", "JsonObject",
    "JsonObjectRef", "JsonObjectConstRef", "Controller", "GPIOPin"
))
def test_exists(attr):
    assert hasattr(cg, attr)
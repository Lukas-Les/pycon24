example = {
    "price": 15,
    "name": "Allan"
}


def parse_demo_data(instance):
    match instance:
        case dict() as data_item:
            match data_item:
                case {
                    "name": str() as name,
                    "price": int(price) | float(price),
                    **extra
                }:
                    if extra:
                        print(f"found extra values: {extra!r}")
                    #  Process data
                    print(f"{name}: {price}")
                case wrong_values:
                    print(f"could not parse properties: {wrong_values!r}")
        case wrong_values:
            print(f"could not parse instance: {wrong_values!r}")


parse_demo_data(example)


table = [
    {"name": "eggs", "price": 2.99},
    {"name": "eggs", "price": 2},
    {"name": "eggs"},
    {"color": "brown", "name": "eggs", "price": 3.99}
]


def parse_list_data(many_instances):
    match many_instances:
        case list() as data_list:
            for instance in data_list:
                parse_demo_data(instance)
        case wrong_data:
            print(f"unknown data format: {wrong_data!r}")


parse_list_data(table)

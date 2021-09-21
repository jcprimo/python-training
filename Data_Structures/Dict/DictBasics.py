# We are learning how to manipulate a dict
# Takeaway: learn how to traverse
# extract key values
# add, remove (Whether it is mutable or not which I think they are not)
def dict_functions():
    # Creation of a dict with a nested key
    d = {'colors': {'red': 1, 'blue': 2, 'green': 3}}
    print(d)

    # creating an empty dict
    Dict = {}
    print("empty Dict:")
    print(Dict)
    print()

    # Add Elements
    Dict[0] = 'test'
    Dict[2]='to'
    Dict[4]='understand'
    print("After adding elements individually:")
    print(Dict)
    print()

    # Adding a set of values
    Dict['muchos_values'] = 2, 3, 4
    print("After adding muchos_values (or set of values):")
    print(Dict)
    print()

    # Replacement
    Dict[0]='come'
    print('Changed `test` for `come`:')
    print(Dict)

    # Access an element using a get
    print("Using the `get()` function: ")
    print(Dict.get(0))

    # Custom Dict
    complex_dict = {"results": {"old_results": "some/location", "new_results": "some/location"}}
    # storing the results into a variables
    results = complex_dict['results']
    print(results)
    print("old_results=" + results['old_results'])
    print("new_results=" + results['new_results'])

    # Delete an element
    del results['old_results']
    print("deleted specific key")
    print(results)


    # new_dict = {key: dict[key] for key in dict.keys() - ['results']['old_location']}
    # print(new_dict)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    dict_functions()
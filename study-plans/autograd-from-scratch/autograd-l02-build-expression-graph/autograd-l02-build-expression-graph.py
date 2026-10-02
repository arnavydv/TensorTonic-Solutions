def build_expression_graph(leaves: list, operations: list) -> tuple:
    """
    Returns a tuple of the node list and final node ID.
    """
    final_list = []
    for i in leaves:
        final_list.append({
            'id': i['id'],
            'data': float(i['data']),
            'grad': float(0),
            'op': '',
            'parents': [],
        })
    for i in operations:
        left_node = next(n for n in final_list if n['id'] == i['left'])
        right_node = next(n for n in final_list if n['id'] == i['right'])
        if i['op'] == '*':
            result = float(left_node['data'] * right_node['data'])
        else:
            result = float(left_node['data'] + right_node['data'])
        dict1 = {
            'id': i['id'],
            'data': result,
            'grad': float(0), 
            'op': i['op'],
            'parents': [i['left'], i['right']]
        }
        final_list.append(dict1)
    final_id = final_list[-1]['id'] if final_list else None
    return final_list, final_id

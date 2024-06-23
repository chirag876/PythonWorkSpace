
def extract_tables(response, blocks_map):
    table_blocks = []
    for block in response['Blocks']:
        if block['BlockType'] == 'TABLE':
            table_blocks.append(block)

    table_data = {}
    for index, table in enumerate(table_blocks):
        rows, header_indices = get_rows_columns_map(table, blocks_map)
        table_data.update({f"table_{index+1}":rows})

    return table_data

def get_rows_columns_map(table_result, blocks_map):
    rows = {}
    header_indices = set()  # To store the indices of table headers
    for relationship in table_result['Relationships']:
        if relationship['Type'] == 'CHILD':
            for child_id in relationship['Ids']:
                cell = blocks_map[child_id]
                if cell['BlockType'] == 'CELL':
                    row_index = cell['RowIndex']
                    col_index = cell['ColumnIndex']
                    
                    row_key = f"row_{row_index}"
                    col_key = f"col_{col_index}"
                    
                    if row_key not in rows:
                        rows[row_key] = {}
                    # Get the text value
                    text = get_text(cell, blocks_map)
                    rows[row_key][col_key] = text
                    if row_index == 1:  # Assuming table header is in the first row
                        header_indices.add(col_index)
                        
    return rows, header_indices



def get_text(result, blocks_map):
    text = ''
    if 'Relationships' in result:
        for relationship in result['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    word = blocks_map[child_id]
                    if word['BlockType'] == 'WORD':
                        text += word['Text'] + ' '
                    elif word['BlockType'] == 'SELECTION_ELEMENT':
                        if word['SelectionStatus'] == 'SELECTED':
                            text += 'X '
    return text.strip()  # Strip any trailing whitespace

class Rule_split:
    def __init__(self):
        pass

    def execute_rule(self,input_record, output_record, rule):
        splited_rule = rule['input_column']
        splited = input_record[rule['input_column']].split()
        output_record['splited_1'] = splited[0]
        output_record['splited_2'] = splited[1]

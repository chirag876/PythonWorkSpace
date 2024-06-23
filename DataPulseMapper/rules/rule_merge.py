class Rule_merge:
    def __init__(self):
        pass
    
    def execute_rule(self,input_record,output_record, rule):
        splited_rule = rule['input_column'].split(',')
        result = input_record[splited_rule[0]] +' ' +input_record[splited_rule[1]]
        output_record['merged_column'] = result

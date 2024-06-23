import app_level as app_level
from logzero import logger


class Rule_field_map(object):
    """description of class"""

    # Class level attribute
    RuleType = "field_map"
    Rule = None
    mongoDbFileMappingObj = None

    # Constructor
    def __init__(self):
        pass

    def execute_rule(self,input_record, output_record, rule):
    # Check if the unique_id matches
        if output_record["unique_id"][0] == input_record["UNIQUE_ID"]:
            # Check for 'N/A' or empty string and set to None if needed
            input_value = input_record.get(rule['input_column'])
            if input_value == "":
                input_value = None
            if input_value == None:
                if rule['is_required']:
                    logger.error(f"Required data missing: {input_record.get('UNIQUE_ID')}")
                
            output_record[rule['output_column']] = input_value

            if output_record[rule['output_column']] is None:
                output_record[rule['output_column']] = rule['default_value']
                


    # def extract_keys(self, data, parent_key=''):
    #     if isinstance(data, dict):
    #         for key, value in data.items():
    #             new_key = f"{parent_key}.{key}" if parent_key else key
    #             self.schema[new_key] = None  # You can set a default value if needed
    #             self.extract_keys(value, parent_key=new_key)
    #     elif isinstance(data, list):
    #         for index, item in enumerate(data):
    #             self.extract_keys(item, parent_key=parent_key)


    # def apply_rules(self):
    #     rule = self.Rule
    #     input_column = rule['input_column']
    #     output_column = rule['output_column']

    #     for key in self.schema:
    #         if input_column == key:
    #             self.schema[key] = rule.get('output_column', None)

   
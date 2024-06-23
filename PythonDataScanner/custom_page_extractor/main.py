from custom_page_extractor.custom_page_textract import TEXTRACT
from service_api.default_json_extractor import default_json

class Custom_Main :

    def extract_data(self,file_path,pages):
        
        if pages:
            try:
                textract = TEXTRACT()
                textract_output,page_count = textract.get_mapped_json(file_path,page_list=pages)

                return textract_output,page_count
            
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                print({'error': error_msg}), 500

    def raw_json(self,textract_output, page_count, file_name):

        try:
            json_dict = default_json(textract_output,page_count,file_name)

            return json_dict
        except Exception as e:
            print(f"Error occured :: {e}")

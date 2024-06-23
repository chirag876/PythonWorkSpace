import boto3
from collections import defaultdict
import fitz  # PyMuPDF
from service_api import credentials
import io
import cv2
import numpy as np
from logzero import logger
from service_api.key_value_relationship import get_kv_relationship
from service_api.only_tables import extract_tables
from service_api.restructure_130_140_tables import RESTRUCTURE_130_140
from service_api.restructure_126_tables import RESTRUCTURE_126
from service_api.restructure_acord141_tables import RESTRUCTURE_141

class TEXTRACT:

    def get_mapped_json(file_name,template):
        pdf_document = fitz.open(file_name)

        session = boto3.Session(
            aws_access_key_id=credentials.access_key,
            aws_secret_access_key=credentials.aws_secret_access_key,
            region_name=credentials.region
        )

        client = session.client('textract')

        main_dict = {}
        page_count = 0

        logger.info("Data extraction started ...")

        for page_number in range(pdf_document.page_count):
            all_kvs = defaultdict(list)
            # table_data = {}

            page = pdf_document[page_number]

            # Get the image bytes from the page
            img_bytes = page.get_pixmap().tobytes()

            # Convert bytes to an image array using OpenCV
            nparr = np.frombuffer(img_bytes, np.uint8)
            img_cv2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Convert the image to grayscale
            gray_img_cv2 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)

            # Convert the grayscale image back to bytes
            ret, gray_img_bytes_cv2 = cv2.imencode('.png', gray_img_cv2)

            gray_img_bytes_io = io.BytesIO(gray_img_bytes_cv2)

            page_count += 1

            try:
                response = client.analyze_document(Document={'Bytes': gray_img_bytes_io.getvalue()}, FeatureTypes=['TABLES','FORMS','SIGNATURES','LAYOUT'])
                blocks = response['Blocks']
            except client.exceptions.UnsupportedDocumentException as e:
                print(f"UnsupportedDocumentException: {e}")
                print(f"Page {page_number + 1} in the document may have an issue.")
                logger.info(f"Page {page_number + 1} in the document may have an issue.")
                continue

            key_map = {}
            value_map = {}
            block_map = {}

            for block in blocks:
                block_id = block['Id']
                block_map[block_id] = block
                if block['BlockType'] == "KEY_VALUE_SET":
                    if 'KEY' in block['EntityTypes']:
                        key_map[block_id] = block
                    else:
                        value_map[block_id] = block

            kvs = get_kv_relationship(key_map, value_map, block_map)
            for key, values in kvs.items():
                all_kvs[key.replace(':','').strip()].extend(values)

            # print("all_kvs ::",all_kvs)
            # table_response = client.analyze_document(Document={'Bytes': gray_img_bytes_io.getvalue()}, FeatureTypes=['TABLES'])
            blocks_map = {block['Id']: block for block in response['Blocks']}
            # table_data.update({f"Page_{page_count}":extract_tables(response, blocks_map)})

            # Extract tables
            tables = extract_tables(response, blocks_map)

            if template in ["ACORD130(2013/09)", "ACORD140(2014/12)"]:
                restructure = RESTRUCTURE_130_140()

                tables = restructure.identify_table_structure(tables)

                # Filter out key-values already present in tables
                filtered_kvs = {}
                for key, values in all_kvs.items():
                    if all(value not in tables.values() for value in values):
                        filtered_kvs[key] = values
                
                kvs = {}
                for key,value in filtered_kvs.items():
                    if isinstance(value,list):
                        if len(value) == 1:
                            if value[0] in ['X','X ']:
                                kvs[key] = "SELECTED"
                            else:
                                kvs[key] = value[0]
                        elif len(value) > 1:
                            v = [i.replace('X','SELECTED') for i in value if i]
                            kvs[key] = v
                    else:
                        kvs[key] = value

                output = {"all_kvs": kvs, "table_data": tables}
                
                main_dict[f"Page_{page_count}"] = output


            elif  template in ["ACORD126(2014/04)","ACORD125(2016/03)","ACORD127(2010/05)"]:
                restructure = RESTRUCTURE_126()

                tables = restructure.identify_table_structure(tables)

                # Filter out key-values already present in tables
                filtered_kvs = {}
                for key, values in all_kvs.items():
                    if all(value not in tables.values() for value in values):
                        filtered_kvs[key] = values
                
                kvs = {}
                for key,value in filtered_kvs.items():
                    if isinstance(value,list):
                        if len(value) == 1:
                            if value[0] in ['X','X ']:
                                kvs[key] = "SELECTED"
                            else:
                                kvs[key] = value[0]
                        elif len(value) > 1:
                            v = [i.replace('X','SELECTED') for i in value if i]
                            kvs[key] = v

                output = {"all_kvs": kvs, "table_data": tables}
                
                main_dict[f"Page_{page_count}"] = output

            elif  template in ['ACORD141(2016/03)']:
                restructure = RESTRUCTURE_141()

                tables = restructure.identify_table_structure(tables)

                # Filter out key-values already present in tables
                filtered_kvs = {}
                for key, values in all_kvs.items():
                    if all(value not in tables.values() for value in values):
                        filtered_kvs[key] = values
                
                kvs = {}
                for key,value in filtered_kvs.items():
                    if isinstance(value,list):
                        if len(value) == 1:
                            if value[0] in ['X','X ']:
                                kvs[key] = "SELECTED"
                            else:
                                kvs[key] = value[0]
                        elif len(value) > 1:
                            v = [i.replace('X','SELECTED') for i in value if i]
                            kvs[key] = v

                output = {"all_kvs": kvs, "table_data": tables}
                
                main_dict[f"Page_{page_count}"] = output

            else:

                # Filter out key-values already present in tables
                filtered_kvs = {}
                for key, values in all_kvs.items():
                    if all(value not in tables.values() for value in values):
                        filtered_kvs[key] = values
                
                kvs = {}
                for key,value in filtered_kvs.items():
                    if isinstance(value,list):
                        if len(value) == 1:
                            if value[0] in ['X','X ']:
                                kvs[key] = "SELECTED"
                            else:
                                kvs[key] = value[0]
                        elif len(value) > 1:
                            v = [i.replace('X','SELECTED') for i in value if i]
                            kvs[key] = v

                output = {"all_kvs": kvs, "table_data": tables}
                
                main_dict[f"Page_{page_count}"] = output

        
        return main_dict,page_count,file_name

# from concurrent.futures import ThreadPoolExecutor
# import concurrent.futures
# import fitz
# import io
# from collections import defaultdict
# import boto3

# class TEXTRACT:

#     def get_kv_map(file_name):
#         pdf_document = fitz.open(file_name)

#         session = boto3.Session(
#             aws_access_key_id=credentials.access_key,
#             aws_secret_access_key=credentials.aws_secret_access_key,
#             region_name=credentials.region
#         )

#         client = session.client('textract')

#         all_kvs = defaultdict(list)
#         page_count = 0

#         def process_page(page_number):
#             nonlocal page_count
#             nonlocal all_kvs

#             page = pdf_document[page_number]
#             img_bytes = page.get_pixmap().tobytes()
#             img_test = io.BytesIO(img_bytes)

#             page_count += 1

#             try:
#                 response = client.analyze_document(Document={'Bytes': img_test.getvalue()}, FeatureTypes=['FORMS', 'TABLES'])
#                 blocks = response['Blocks']
#             except client.exceptions.UnsupportedDocumentException as e:
#                 print(f"UnsupportedDocumentException: {e}")
#                 print(f"Page {page_number + 1} in the document may have an issue.")
#                 return

#             key_map = {}
#             value_map = {}
#             block_map = {}

#             for block in blocks:
#                 block_id = block['Id']
#                 block_map[block_id] = block
#                 if block['BlockType'] == "KEY_VALUE_SET":
#                     if 'KEY' in block['EntityTypes']:
#                         key_map[block_id] = block
#                     else:
#                         value_map[block_id] = block

#             kvs = get_kv_relationship(key_map, value_map, block_map)
#             for key, values in kvs.items():
#                 all_kvs[key].extend(values)

#             # Extract table info and update all_kvs
#             word_map = map_word_id(response)
#             table = extract_table_info(response, word_map)
#             for table_id, values in table.items():
#                 result = extract_keys_values(table_id, values)
#                 all_kvs.update(result)

#         with ThreadPoolExecutor(max_workers=5) as executor:
#             executor.map(process_page, range(pdf_document.page_count))

#         final_dict = dict(all_kvs)
#         return final_dict, page_count, file_name



    # def get_kv_relationship(self):
    #     kvs = defaultdict(list)
    #     for block_id, key_block in self.key_map.items():
    #         value_block = self.find_value_block(key_block, self.value_map)
    #         key = self.get_text(key_block, self.block_map)
    #         val = self.get_text(value_block, self.block_map)
    #         if val not in kvs[key]:
    #             kvs[key].append(val)
    #     return kvs

    # def find_value_block(self,key_block, value_map):
    #     for relationship in key_block['Relationships']:
    #         if relationship['Type'] == 'VALUE':
    #             for value_id in relationship['Ids']:
    #                 value_block = value_map[value_id]
    #                 return value_block

    # def get_text(self,result, blocks_map):
    #     text = ''
    #     if 'Relationships' in result:
    #         for relationship in result['Relationships']:
    #             if relationship['Type'] == 'CHILD':
    #                 for child_id in relationship['Ids']:
    #                     word = blocks_map[child_id]
    #                     if word['BlockType'] == 'WORD':
    #                         text += word['Text'] + ' '
    #                     elif word['BlockType'] == 'SELECTION_ELEMENT':
    #                         if word['SelectionStatus'] == 'SELECTED':
    #                             text += 'X '
    #     return text

    # def get_json(self):
    #     start_time = time.time()
    #     logger.info("PDF to JSON conversion started ...")
    #     kvs = self.get_kv_map()
    #     json_output = {}
    #     json_output.update({"File name":self.file_name.split('\\')[-1]})
    #     json_output.update({"Page count":self.page_count})
        
    #     for key, value in kvs.items():
    #         if ':' in key:
    #             key = key.replace(':','')
    #         value = list(set(value))

    #         if len(value) == 1:
    #             # print(f"{key}: {value[0]}")
    #             json_output[key.strip()] = value[0].strip()
    #         else:
    #             json_output[key.strip()] = [v.strip() for v in value]
    #             # print(f"{key}: {value}")
    #     logger.info(f"Time taken for conversion {time.time() - start_time} seconds.")
    #     return  json_output
    
    # def search_value(self,kvs, search_key):
    #     for key, value in kvs.items():
    #         if re.search(search_key, key, re.IGNORECASE):
    #             return value

    # def main(file_name):
    #     all_kvs = get_kv_map(file_name)
    #     print_kvs(all_kvs)

# if __name__ == "__main__":
#     main(r"D:\Research\PDF TO TEXT - Comparison\pdf files\Grinnell Mutual C Auto Commercial Auto rule 1 25 GRNX-133755182.pdf")
#     # main(r"D:\Workspace\Project - PDF_TO_JSON\PDF TO JSON - Textract\pdf files\AIG Property Commercial Property (151-640-288) form 1 24 AGNY-133633794.pdf")
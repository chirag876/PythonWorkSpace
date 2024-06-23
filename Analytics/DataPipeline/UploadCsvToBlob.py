import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings, BlobBlock
import config, os
import uuid

class CsvToBlob:
    def __init__(self) -> None:
        self.connectionstring=config.connectionstring
        self.containername=config.containername
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connectionstring)
        self.container_client = self.blob_service_client.get_container_client(self.containername)


    def upload_file_chunks(self,local_file_path,blob_file_path):
        '''
        Upload large file to blob
        '''
        try:
            blob_client = self.container_client.get_blob_client(blob_file_path)
            # upload data
            block_list=[]
            chunk_size=1024*1024*4
            with open(local_file_path,'rb') as f:
                while True:
                    read_data = f.read(chunk_size)
                    if not read_data:
                        break # done
                    blk_id = str(uuid.uuid4())
                    blob_client.stage_block(block_id=blk_id,data=read_data) 
                    block_list.append(BlobBlock(block_id=blk_id))
            blob_client.commit_block_list(block_list)
            print(f"File {local_file_path} uploaded successfully!")
            return f"File {local_file_path} uploaded successfully!"
    
        except BaseException as err:
            print('Upload file error')
            print(err)
            return err

# obj=CsvToBlob()
# obj.upload_file_chunks('Claim.csv',"Claim.csv")
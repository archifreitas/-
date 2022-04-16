from Hr_azure_function.Factories import SqlFactory
import pandas as pd
from Hr_azure_function.Models.Entities import Databases



class GetData:
    '''Class for GetData'''

    def __init__(self):
        self.server = SqlFactory()
        self.data_entries = Databases()
    
    def get_data(self, data_dict):
        
        dataframes = {}

        for table, columns in data_dict.items():
            result = self.server.query_columns(table, columns)
            
            df = pd.DataFrame(result)
            df.columns = result.keys()

            dataframes[table] = df

        return dataframes
    
    def merge_data(datasets, data_keys):

        result_df = pd.DataFrame()

        for merge_keys in data_keys.values():

            tables_to_merge = list(merge_keys)
            keys_to_merge = list(merge_keys.values())

            for index, _ in enumerate(tables_to_merge):

                if index != len(tables_to_merge) - 1:
                    datasets[tables_to_merge[index]].merge(datasets[tables_to_merge[index] + 1], 
                                                           on_left=tables_to_merge[index],
                                                           on_right=tables_to_merge[index + 1])

        return result_df

    def build_data(self):
        return self.merge_data(self.get_data(self.data_entries.data_dict), self.data_entries.data_keys)
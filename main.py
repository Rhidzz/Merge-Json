import pandas as pd
import json

def extract_text():

    df = pd.read_csv("data-set - Sheet1.csv")
    

    datas = df.to_dict("records")

    num = 0
    name_num = 1
    for data in datas:

        new_dict = {}
        attributes = []
        name = data["Name"]
        name = name.replace("’", "'")

        description = data["Description"].replace("’", "'").replace("—", " ")
        # print(description)
        trait_type_1 = data["background"]
        trait_type_2 = data["texture"]

        dict_num_1 = {}
        dict_num_2 = {}

        dict_num_1["trait_type"] = "background"
        dict_num_1["value"] = trait_type_1
        attributes.append(dict_num_1)

        dict_num_2["trait_type"] = "texture"
        dict_num_2["value"] = trait_type_2
        attributes.append(dict_num_2)
        image = str(name_num)+".png"

        new_dict["name"] = name
        new_dict ["description"] = description
        new_dict["image"] = image
        new_dict["attributes"] = attributes

        # print(new_dict)

        with open(f'Jsons\\{num}.json', "w") as outfile: 
            json.dump(new_dict, outfile, indent = 4, sort_keys= False)
    
        num+=1
        name_num+=1

extract_text()



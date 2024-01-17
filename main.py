def is_json(json_string: str) -> bool:
    json_string = json_string.strip()
    if (len(json_string) < 2):
        return False
    return json_string[0] == '{' and json_string[-1] == '}'

def check_string(string):
    if(not isinstance(string, str)):
        return False
    string = string.strip()
    # print(key, key[0] == '"' and key[-1] == '"')
    return string[0] == '"' and string[-1] == '"'

def key_validator(key):
    return check_string(key)
    

def value_validator(value):
    try:
        value = value.strip()
        # print(value)
        if(value == 'true' or value == 'false' or value == 'null'):
            return True
        
        if(check_string(value)):
            return True
        
        value = eval(value)      

        if(isinstance(value, int)):
            return True
        if(isinstance(value, float)):
            return True
        
        if(isinstance(value, list)):

            ## Need to work on these
            # print("Inside list", value)
            for i in value:
                # print("Inside list eval,",i, value_validator(i))
                if(not value_validator(i)):
                    return False
            
            return True

        return False

    except Exception as e:
        # print(e)
        return False
    



def get_json_data(json_string: str) -> object:
    if(len(json_string) < 3):
        return [],[], False
    
    json_string = json_string[1:-1]

    data_array = json_string.split(",")

    if(len(data_array[-1]) == 0):
        return [], [], True
    
    keys = []
    values = []
    
    for data in data_array:
        key, value = data.split(":", 1)
        keys.append(key)
        values.append(value)

    return keys, values, False


def json_validator(json_string: str) -> bool:
    json_string = json_string.strip()

    if (not is_json(json_string)):
        return False

    get_keys, get_values, err = get_json_data(json_string)
    
    if(err):
        return False
    for key in get_keys:
        if(not key_validator(key)):
            return False
    
    for value in get_values:
        if(is_json(value)):
            json_validator(value)
        else:
            if(not value_validator(value)):
                return False

    return True


def json_parsor(file_path: str) -> bool:

    with open(file_path, "r") as f:
        json_string = f.read()

    return json_validator(json_string)


if __name__ == "__main__":
    file_path = r"tests\\step1\\valid.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")

    file_path = r"tests\\step1\\invalid.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")

    file_path = r"tests\\step2\\valid.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")
    
    file_path = r"tests\\step2\\valid2.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")

    file_path = r"tests\\step2\\invalid.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")
    
    file_path = r"tests\\step2\\invalid2.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")

    file_path = r"tests\\step3\\valid.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")
    
    file_path = r"tests\\step3\\invalid.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")

    file_path = r"tests\\step4\\valid.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")
    
    file_path = r"tests\\step4\\valid2.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")
    
    file_path = r"tests\\step4\\invalid.json"
    print(f"{file_path} is a {json_parsor(file_path)} json file")
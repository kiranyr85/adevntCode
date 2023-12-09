import numpy as np
def predict_next_sensor_value(input_array):
    temp_dict = {}
    level=0
    temp_dict[level] = np.array(input_array)
    print(temp_dict[level] )
    #Reduction
    while not all(val == 0 for val in temp_dict[level]):
        level +=1
        temp_dict[level] = np.diff(temp_dict[level-1])
        print(temp_dict[level])
    #Re-generate next value
    last_value = 0
    for key in list(temp_dict.keys())[::-1]:
        last_value +=temp_dict[key][-1]
        temp_dict[key] = np.append(temp_dict[key], last_value)
        print(temp_dict[key])
    return temp_dict[0]

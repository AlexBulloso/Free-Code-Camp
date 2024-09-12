import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.asarray(list, dtype=np.int).reshape([3,3])
    calculations = {'mean':[np.mean(arr, axis=0).tolist(),np.mean(arr,axis=1).tolist(),np.mean(arr)],
                    'variance':[np.var(arr, axis=0).tolist(),np.var(arr,axis=1).tolist(),np.var(arr)],
                    'standard deviation':[np.std(arr, axis=0).tolist(),np.std(arr,axis=1).tolist(),np.std(arr)],
                    'max':[np.max(arr, axis=0).tolist(),np.max(arr,axis=1).tolist(),np.max(arr)],
                    'min':[np.min(arr, axis=0).tolist(),np.min(arr,axis=1).tolist(),np.min(arr)],
                    'sum':[np.sum(arr, axis=0).tolist(),np.sum(arr,axis=1).tolist(),np.sum(arr)],
                    }


    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))

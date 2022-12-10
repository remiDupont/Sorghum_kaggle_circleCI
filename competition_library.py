from fastai.vision.all import *
import random

def label_func_0(path_obj):
    return 1


def randomly_subsample(files,prob_keep:float):

    """function that will return a subsequence of infut list (file)
    Used to train and validate on a subpart of the dataset 

    Args:
        files (_type_): input list to pick elements from
        float (prob_keep): proportion of files to keep

    Returns:
        _type_: sub_sequence of files 
    """
    print("testing =============================================")

    split_file = []
    for f in files:
        if random.random()< prob_keep:
            split_file.append(f)
    return split_file
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    colums = ['student_id','age']
    result = pd.DataFrame(student_data, columns=colums)
    return result

    
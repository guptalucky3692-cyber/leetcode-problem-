import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rs = list(players.shape)
    return rs
    
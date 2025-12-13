import pandas as pd
from pathlib import Path
import os

def get_data_path(filename: str) -> Path:
    # 修正: フォルダ構成に合わせて parent を1つにしました
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    
    file_path = data_dir / filename
    
    if not file_path.exists():
        # Renderでのデプロイ時にエラーにならないよう、空のDataFrameを返すなどの安全策をとっても良いですが
        # 今回はエラーを出して気付かせる方針にします
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    
    return file_path

def load_csv(filename: str) -> pd.DataFrame:
    path = get_data_path(filename)
    try:
        df = pd.read_csv(path, encoding='utf-8').fillna("")
        return df
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return pd.DataFrame()

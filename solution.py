import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 1265544018 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
  alpha = 0.07
  res = ks_2samp(x, y, alternative='two-sided')
  
  return res.pvalue < alpha

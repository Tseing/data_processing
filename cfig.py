import matplotlib.pyplot as plt
from matplotlib import rcParams

config = {
    "font.family":'serif',
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
    'figure.dpi':'140',
}
rcParams.update(config)
plt.rcParams['font.serif'] = ['Times New Roman']
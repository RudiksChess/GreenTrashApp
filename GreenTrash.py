import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import six

registro = pd.read_csv('registro.csv')
amarillo = pd.read_csv('amarillo.csv')
verde = pd.read_csv('verde.csv')
gris = pd.read_csv('gris.csv')

amarilloUP= amarillo.groupby(['ID'], as_index=False).sum()
verdeUP= verde.groupby(['ID'], as_index=False).sum()
grisUP= gris.groupby(['ID'], as_index=False).sum()

junto= amarilloUP.merge(verdeUP,on='ID').merge(grisUP,on='ID')

completo = registro.merge(junto, on='ID')
completo['TOTAL'] = completo.sum(axis=1)


def GenerarExcel():
    completo.to_csv("DATOSFINALES.csv", sep=',', index= False)

def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=30,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([10, 5])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

lol= render_mpl_table(completo, header_columns=0, col_width=2.0)
figura= lol.get_figure()
figura.savefig("final.png")

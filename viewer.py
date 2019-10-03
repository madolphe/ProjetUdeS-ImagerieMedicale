import numpy
import nibabel as nib
import matplotlib.pyplot as plt
import holoviews as hv
hv.extension('bokeh')

def viewer(I, mode='axial'):
    """
    I: image 3D à considérer
    mode: coupe souhaitée, 3 possibilités -> 'axial': vue du dessus, [:, :, image souhaitée, couleur]
                                             'sagittale': vue de coté [image souhaitée ,:, :, couleur]
                                             'coronale': vue de devant [:, image souhaitée, :, couleur]

    :return:
    """
    img = nib.load(I).get_data()
    print(img.shape)
    return


if __name__ == '__main__':
    viewer('Data_MiseEnForme/IRM/Heart/PetitAxe/Slice06.nii')

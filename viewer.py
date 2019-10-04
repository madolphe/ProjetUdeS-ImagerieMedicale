import numpy as np
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
    frequencies = [0.5, 0.75, 1.0, 1.25]

    def sine_curve(phase, freq):
        xvals = [0.1 * i for i in range(100)]
        return hv.Curve((xvals, [np.sin(phase + freq * x) for x in xvals]))

    # When run live, this cell's output should match the behavior of the GIF below
    dmap = hv.DynamicMap(sine_curve, kdims=['phase', 'frequency'])
    dmap.redim.range(phase=(0.5, 1), frequency=(0.5, 1.25)).show()
    return


if __name__ == '__main__':
    # viewer('Data_MiseEnForme/IRM/Heart/PetitAxe/Slice06.nii')
    img = nib.load('Data_MiseEnForme/IRM/Heart/PetitAxe/Slice06.nii').get_data()
    print(img.shape)
    etendue = [i for i in range(img.shape[2])]
    holomap = hv.HoloMap(kdims=etendue)

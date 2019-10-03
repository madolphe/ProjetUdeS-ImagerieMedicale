import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class description:
    def __init__(self, imgPath):
        self.img = nib.load(imgPath)
        self.imgData = self.img.get_fdata()

    def normalise_image(self):
        """
        Fonction qui permet de normaliser l'image que l'on étudie
        """
        x_min = np.amin(self.imgData)
        x_max = np.amax(self.imgData)
        print(x_max)
        print(x_min)
        normalised_data = (self.imgData - x_min) / (x_max - x_min)
        print(normalised_data.shape)
        print(self.imgData.shape)
        #print(max(normalised_data))
        #print(min(normalised_data))
        return normalised_data


    def calculs_tailles(self):
        """
        Fonction qui retourne la taille des voxels de l'image
        Ainsi que la taille de l'image
        """
        header_info = self.img.header
        shape_img = header_info.get_data_shape()
        shape_voxel = header_info.get_zooms()
        print("Taille de l'image spécifiée :", shape_img)
        print("Taille des voxels l'image spécifiée :", shape_voxel)


    def calculs_michelson(self):
        """
        Fonction qui calcul le contrate de Michelson de l'image spécifiée
        """
        lmax = np.amax(self.imgData)
        lmin = np.amin(self.imgData)
        c_michelson = (lmax-lmin)/(lmax+lmin)
        print("Le contraste de Michelson de l'image spécifiée est : ", c_michelson)

    def calculs_rms(self):
        """
        Fonction qui calcul le rms (root mean squared) de l'image spécifiée
        """
        img_moyenne = np.mean(self.imgData[:, :, 10])
        img_centree = (self.imgData - img_moyenne) ** 2
        img_mean_centre = np.mean(img_centree)
        rms = np.sqrt(img_mean_centre)
        print("le rms de l'image spécifiée est :", rms)

    #def calculs_petite_struc(self):
        """
        Fonction qui calcul la taille de la plus petite structure présente dans
        l'image et spécifie où l'on retrouve du volume partiel
        """
    def nature_bruit(self):
        """
        Fonction qui calcul la nature de bruit dans chaque image,
        spécifie si c'est un bruit de nature uniforme et s'il y
        présence d'artéfacts
        """
        normalised_data = self.normalise_image()
        resized_data = normalised_data.flatten()
        plt.hist(resized_data, bins=256, range=[0.1, 0.9])
        plt.ylabel('Probability');
        plt.show()

        # Pour faire ça, il faut repérer dans chacune des images, une fenêtre de taille carrée qui semble uniforme,
        # donc quelque chose qui est de la même couleur partout, ensuite effectuer l'histogramme de cette fenêtre et en déduire
        # la nature du bruit.
        # Il est également possible dans un premier temps de générer l'histogramme de l'image entière, ce qui peut être relativement
        # intéressant en terme de comparaison.

    #def snr(self):
        """
        Fonction qui calcul le ou les SNR de l'image
        """


if __name__ == '__main__':
    """
    Liste de fonctions mises en place pour tester certaines partie de la classe présentée précédemment. 
    # Non utile pour le bon fonctionnement du projet. 
    """

    def test_calculs_tailles():
        desc = description('Data_MiseEnForme/IRM/Brain/t1.nii')
        desc.calculs_tailles()

    #test_calculs_tailles()

    def test_calculs_michelson():
        desc = description('Data_MiseEnForme/IRM/Brain/t1.nii')
        desc.calculs_michelson()

    #test_calculs_michelson()

    def test_calculs_rms():
        desc = description('Data_MiseEnForme/Ultrasound/us.nii')
        desc.calculs_rms()

    # test_calculs_rms()

    def test_normalisation():
        desc = description('Data_MiseEnForme/Ultrasound/us.nii')
        desc.normalise_image()
    #test_normalisation()

    def test_nature_bruit():
        desc = description('Data_MiseEnForme/IRM/Brain/fa.nii')
        desc.nature_bruit()

    test_nature_bruit()
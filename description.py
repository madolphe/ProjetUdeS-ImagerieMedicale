import numpy
import nibabel as nib
import matplotlib.pyplot as plt
import holoviews as hv

class description:
    def __init__(self, image):
        self.image = image

    def calculs_tailles(self):
        """
        Fonction qui retourne la taille des voxels de l'image
        Ainsi que la taille de l'image
        """
        image = nib.load(self.image)
        header_info = image.header
        shape_img = header_info.get_data_shape()
        shape_voxel =  header_info.get_zooms()
        print("Taille de l'image spécifiée :", shape_img)
        print("Taille des voxels l'image spécifiée :", shape_voxel)


    #def calculs_michelson_rms(self):
        """
        Fonction qui calcul le contrate de Michelson de l'image spécifiée
        ainsi que le RMS
        """


    #def calculs_petite_struc(self):
        """
        Fonction qui calcul la taille de la plus petite structure présente dans 
        l'image et spécifie où l'on retrouve du volume partiel
        """
    #def nature_bruit(self):
        """
        Fonction qui calcul la nature de bruit dans chaque image,
        spécifie si c'est un bruit de nature uniforme et s'il y
        présence d'artéfacts
        """

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

    test_calculs_tailles()
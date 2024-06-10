import random as rd
import tkinter as tk

from collections import deque

COTE_CASE = 40
DICO = {} # TEST // essaie d'un dico extérieur

class Cellule:
    def __init__(self):
        self.mur_bas = True  # True signifie que le mur est fermé
        self.mur_droit = True # False signifie que le mur est ouvert
        

class Labyrinthe:
    def __init__(self, largeur, hauteur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.grille = [[Cellule() for j in range(largeur)] for i in range(hauteur)]
        self.generation()

    def solution(self, depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne):
        """
        Renvoie la liste de directions à suivre pour se rendre de la cellule
        (depart_ligne, depart_colonne) à la cellule (arrivee_ligne, arrivee_colonne).
        Exemple de retour : ['n', 'e', 'e', 's', 'o']
        Fonction utilisé : parcourir, nombre_de_mur
        """
        """
        permet d'avancer vers : le bas, la droite, le haut, la gauche
                if self.grille[depart_ligne][depart_colonne].mur_bas == False :
                    liste_solution.append('s')
                    depart_ligne += 1
                elif self.grille[depart_ligne][depart_colonne].mur_droit == False :
                    liste_solution.append('e')
                    depart_colonne += 1
                elif self.grille[depart_ligne-1][depart_colonne].mur_bas == False :
                    liste_solution.append('n')
                    depart_ligne -= 1
                elif self.grille[depart_ligne][depart_colonne-1].mur_droit == False :
                    liste_solution.append('o')
                    depart_colonne -= 1
                    
             print(self.nombre_de_mur(ligne, colonne)) # TEST // écrit le nombre de mur autour du point
            time.sleep(3) # TEST // Fait suite au programme tout les 3 secondes
            DICO[f"{ligne}.{colonne}"] = "" # TEST // implémente dans le dico à la valeur des coordonnées, le prédécesseur de la case
        print(DICO)
        #return liste_solution   # retourne la liste des passages à suivre pour accéder au point
        """
        
        ligne, colonne = depart_ligne, depart_colonne
        DICO[f"{depart_ligne.{depart_colonne}}"] = ""
        while ligne != arrivee_ligne or colonne != arrivee_colonne :
            
            parcourir(ligne, colonne, arrivee_ligne, arrivee_colonne)
            
        
        return parcours_dico(arrivee_ligne,arrivee_colonne)
        
    
    def parcourir(self, ligne, colonne, arrivee_ligne, arrivee_colonne) :
        """
        permet de se balader dans le labyrinthe

        Parameters
        ----------
        ligne : int
            Coordonnée de la ligne du point actuel.
        colonne : int
            Coordonnée de la colonne du point actuel.
        arrivee_ligne : int
            Coordonnée de la ligne du point à atteindre.
        arrivee_colonne : int
            Coordonnée de la colonne du point à atteindre.

        Returns
        -------
        bool/int
            retourne None si le point est dans un passage sans issue.
            retourne True si le point est arrivée sur l'objectif.
            retourne le prochain point à accéder pour continué

        """
        if ligne == arrivee_ligne and colonne == arrivee_colonne :
            return True
        elif self.nombre_de_mur(ligne, colonne) == 3 :
            return False
        if self.grille[ligne][colonne].mur_bas == False : #regarde le mur au sud
        if self.grille[ligne][colonne].mur_droit == False : #regarde le mur à l'est
        if self.grille[ligne-1][colonne].mur_bas == False : #regarde le mur au nord
        if self.grille[ligne][colonne-1].mur_droit == False : #regarde le mur au nord
    
    def parcours_dico (ligne, colonne ,liste_solution = deque([])):
        """
        Fonction récursive qui parcours le dictionnaire qui contient les coordonnées des points
        ainsi que leur prédécésseur
        Elle implémente dans une liste les points de coordination 
        pour tracée la solution
        
        exemple :
            ["s"]
            ["e","s"]
            ["n","e","s"]
            ["n","n","e","s"]
            ["...","n","n","e","s"]
        
        Parameters
        ----------
        ligne : int
            Coordonnée de la ligne du point actuel.
        colonne : int
            Coordonnée de la colonne du point actuel.
        liste_solution : list
            Liste des points de coordinations pour tracer la solution  
        
        Returns
        -------
        liste_solution : list
            Liste des points de coordinations pour tracer la solution 
        """
        if dico[f"{ligne}.{colonne}"] == "" : #Si les coordonnées dans le dico == ""
            return liste_solution             #alors la fonction aura parcouru le dictionnaire jusqu'à arrivée au point de départ # type: ignore
        else :
            x, y = dico[f"{ligne}.{colonne}"].split(".")
            if ligne - int(x) == 1 and colonne - int(y) == 0:
                parcours_dico(int(x),int(y),liste_solution.appendleft("s"))
                
            elif ligne - int(x) == -1 and colonne - int(y) == 0:
                parcours_dico(int(x),int(y),liste_solution.appendleft("n"))
                
            elif ligne - int(x) == 0 and colonne - int(y) == -1:   
                parcours_dico(int(x),int(y),liste_solution.appendleft("0"))
                
            elif ligne - int(x) == 0 and colonne - int(y) == 1:
                parcours_dico(int(x),int(y),liste_solution.appendleft("e"))
                
    def nombre_de_mur (self,ligne,colonne):
        """
        Calcul le nombre de mur que entoure le point du labyrinthe
        choisi à partir de ses coordonnées

        Parameters
        ----------
        ligne : int
            Coordonnée de la ligne de la place du point.
        colonne : int
            Coordonnée de la colonne de la place du point.

        Returns
        -------
        nbr_mur : int 
            Nombre de mur autour du point.

        """
        nbr_mur = 0
        if self.grille[ligne][colonne].mur_bas == True : #Observe le mur en_dessous 
            nbr_mur += 1
        if self.grille[ligne][colonne].mur_droit == True : #Observe le mur à droite
            nbr_mur += 1
        if self.grille[ligne-1][colonne].mur_bas == True : #Observe la case au dessus du point et son mur situé en dessous #Observe le mur au_dessus
            nbr_mur += 1
        if self.grille[ligne][colonne-1].mur_droit == True : #Observe la case à gauche du point et son mur situé à droite #Observe le mur de gauche
            nbr_mur += 1
        return nbr_mur
        
    def generation(self):
        nombre_cellules = self.largeur*self.hauteur
        zones_cellules = list(range(nombre_cellules))
        # Les cellules sont numérotées en ligne, avec les numéros 0 à 
        # largeur-1 sur la première ligne, largeur à 2*largeur-1 sur la
        # deuxième ... jusqu'à hauteur*largeur-1 en bas Ã  droite
        murs_modifiables = list(range(2*nombre_cellules-self.largeur-self.hauteur))
        # Tous les murs bas et droits sont modifiables sont ceux en bas ou à 
        # droite du labyrinthe. Ils sont numérotés en commençant par les murs
        # verticaux dans le même ordre que les cellules. Les murs numéro 0 à
        # self.largeur*self.hauteur-self.hauteur-1 sont les murs verticaux, et 
        # ceux allant de self.largeur*self.hauteur-self.hauteur à 
        # 2*self.largeur*self.hauteur-self.largeur-self.hauteur-1 les horizontaux.
        indice_premier_non_modifiable = len(murs_modifiables)
        # Lorsqu'un mur est choisi, on le met à la fin du tableau pour ne
        # pas le rechoisir. Ce serait plus simple de le supprimer de la liste
        # mais plus couteux car la suppression est en O(n).
        modifications = 0
        while modifications < nombre_cellules - 1:
            indice_mur = rd.randrange(indice_premier_non_modifiable)
            mur_candidat = murs_modifiables[indice_mur]
            if self.modifier_mur(mur_candidat, zones_cellules):
                modifications += 1
            indice_premier_non_modifiable -= 1
            murs_modifiables[indice_mur], murs_modifiables[indice_premier_non_modifiable] = \
                murs_modifiables[indice_premier_non_modifiable], murs_modifiables[indice_mur]
 
    def fusionner_zones(zones_cellules, indice_cellule1, indice_cellule2):
       zone1 = zones_cellules[indice_cellule1]
       zone2 = zones_cellules[indice_cellule2]
       for i in range(len(zones_cellules)):
           if zones_cellules[i] == zone2:
               zones_cellules[i] = zone1       
 
    def modifier_mur(self, mur_candidat, zones_cellules):
        # Le mur sépare cellule1 et cellule2
        mur_vertical = (mur_candidat < self.largeur*self.hauteur-self.hauteur)
        if mur_vertical:
            ligne_cellule1 = mur_candidat//(self.largeur-1)
            colonne_cellule1 = mur_candidat%(self.largeur-1)
            indice_cellule1 = ligne_cellule1*self.largeur + colonne_cellule1
            indice_cellule2 = indice_cellule1 + 1
        else:
            ligne_cellule1 = (mur_candidat-(self.largeur*self.hauteur-self.hauteur))//self.largeur
            colonne_cellule1 = (mur_candidat-(self.largeur*self.hauteur-self.hauteur))%self.largeur
            indice_cellule1 = mur_candidat-(self.largeur*self.hauteur-self.hauteur)
            indice_cellule2 = indice_cellule1 + self.largeur
        if zones_cellules[indice_cellule1] != zones_cellules[indice_cellule2]:  
            Labyrinthe.fusionner_zones(zones_cellules, indice_cellule1, indice_cellule2)
            if mur_vertical:
                self.grille[ligne_cellule1][colonne_cellule1].mur_droit = False
            else:
                self.grille[ligne_cellule1][colonne_cellule1].mur_bas = False
            return True
        else:   # les deux cellules sont déjà dans la même zone, on ne supprime pas le mur
            return False


class GfxHMI(tk.Tk):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.maze = Labyrinthe(largeur, hauteur)  
        tk.Tk.__init__(self)    
        self.canevas = tk.Canvas(self, height=self.hauteur*COTE_CASE+1, width=self.largeur*COTE_CASE+1,
                                  borderwidth=0, highlightthickness=0, bg='ivory')
        self.dessine_labyrinthe()
        self.porte = self.canevas.create_rectangle(2, 2, COTE_CASE-1, COTE_CASE-1, fill='brown')
        self.porte_ligne, self.porte_colonne = 0, 0
        self.tresor_ligne, self.tresor_colonne = hauteur-1, largeur-1
        self.tresor = self.canevas.create_oval((largeur-1)*COTE_CASE+2, (hauteur-1)*COTE_CASE+2, largeur*COTE_CASE-2, hauteur*COTE_CASE-2, fill='yellow')
        self.canevas.bind("<Button-1>", self.placement)
        self.canevas.pack(padx=5, pady=5, side=tk.TOP)
        tk.Button(self, text='Entrée', command=self.souris_entree).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text='Trésor', command=self.souris_tresor).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text='Solution', command=self.solution).pack(side=tk.RIGHT, padx=5, pady=5)
        self.placer_entree = True
        self.placer_tresor = False
        self.trace_du_chemin = None  # conserve la variable tracé pour pouvoir effacer le chemin
       
    def dessine_cellule(self, i, j, cellule):
        if cellule.mur_droit:
            self.canevas.create_line((j+1)*COTE_CASE, i*COTE_CASE+1, (j+1)*COTE_CASE, (i+1)*COTE_CASE+1)
        if cellule.mur_bas:
            self.canevas.create_line(j*COTE_CASE+1, (i+1)*COTE_CASE, (j+1)*COTE_CASE+1, (i+1)*COTE_CASE)
                
    def dessine_labyrinthe(self):
        self.canevas.create_line(0, self.hauteur*COTE_CASE, 0, 0, self.largeur*COTE_CASE, 0, fill='black')
        for i in range(self.hauteur):
            for j in range(self.largeur):
                self.dessine_cellule(i, j, self.maze.grille[i][j])
    
    def placement(self, event):
        colonne = event.x//COTE_CASE
        ligne = event.y//COTE_CASE
        if self.placer_entree:
            objet = self.porte
            self.porte_ligne = ligne
            self.porte_colonne = colonne
        else:
            objet = self.tresor
            self.tresor_ligne = ligne
            self.tresor_colonne = colonne
        self.canevas.coords(objet, colonne*COTE_CASE+2, ligne*COTE_CASE+2, (colonne+1)*COTE_CASE-2, (ligne+1)*COTE_CASE-2)
        
    def souris_entree(self):
        self.placer_entree = True
        self.placer_tresor = False
    
    def souris_tresor(self):
        self.placer_entree = False
        self.placer_tresor = True

    def tracer_chemin(self, depart_ligne, depart_colonne, chemin):
        x = depart_colonne*COTE_CASE + COTE_CASE//2
        y = depart_ligne*COTE_CASE + COTE_CASE//2
        coordonnees_chemin = [x, y]
        for direction in chemin:
            if direction == 'n':
                y -= COTE_CASE
            elif direction == 's':
                y += COTE_CASE
            elif direction == 'e':
                x += COTE_CASE
            else:
                x -= COTE_CASE   
            coordonnees_chemin.extend([x, y])
        self.canevas.delete(self.trace_du_chemin)
        self.trace_du_chemin = self.canevas.create_line(*coordonnees_chemin, fill='blue', width=2)
               
    
    def solution(self):
        chemin_solution = self.maze.solution(self.porte_ligne, self.porte_colonne, self.tresor_ligne, self.tresor_colonne)
        self.tracer_chemin(self.porte_ligne, self.porte_colonne, chemin_solution)
        

    


class Affichage(tk.Tk):
    def __init__(self, labyrinthe):
        largeur = self.largeur = len(labyrinthe.grille[0])
        hauteur = self.hauteur = len(labyrinthe.grille)
        self.maze = labyrinthe
        tk.Tk.__init__(self)    
        self.canevas = tk.Canvas(self, height=self.hauteur*COTE_CASE+1, width=self.largeur*COTE_CASE+1,
                                  borderwidth=0, highlightthickness=0, bg='ivory')
        self.dessine_labyrinthe()
        self.porte = self.canevas.create_rectangle(2, 2, COTE_CASE-1, COTE_CASE-1, fill='brown')
        self.porte_ligne, self.porte_colonne = 0, 0
        self.tresor_ligne, self.tresor_colonne = hauteur-1, largeur-1
        self.tresor = self.canevas.create_oval((largeur-1)*COTE_CASE+2, (hauteur-1)*COTE_CASE+2, largeur*COTE_CASE-2, hauteur*COTE_CASE-2, fill='yellow')
        self.canevas.pack(padx=5, pady=5, side=tk.TOP)

       
    def dessine_cellule(self, i, j, cellule):
        if cellule.mur_droit:
            self.canevas.create_line((j+1)*COTE_CASE, i*COTE_CASE+1, (j+1)*COTE_CASE, (i+1)*COTE_CASE+1)
        if cellule.mur_bas:
            self.canevas.create_line(j*COTE_CASE+1, (i+1)*COTE_CASE, (j+1)*COTE_CASE+1, (i+1)*COTE_CASE)
                
    def dessine_labyrinthe(self):
        self.canevas.create_line(0, self.hauteur*COTE_CASE, 0, 0, self.largeur*COTE_CASE, 0, fill='black')
        for i in range(self.hauteur):
            for j in range(self.largeur):
                self.dessine_cellule(i, j, self.maze.grille[i][j])
    
        


if __name__=='__main__':
    GfxHMI(20, 10).mainloop()        
 
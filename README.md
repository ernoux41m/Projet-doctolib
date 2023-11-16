# Projet-doctolib

Vous êtes embauché en tant que consultant Data pour DoctoLib, une entreprise française qui met en relation des  professionnels de la santé et des patients au travers d’une interface web ainsi qu’une application mobile. 

Votre responsable, Mark Musk, veut ajouter de nouvelles fonctionnalités pour attirer encore plus de professionnels de la santé. Il souhaite leur permettre de mener des enquêtes de santé publique sur un échantillon de patients consentants pour arriver à des conclusions qui seront publiées dans des magazines de santé.

## Schéma base de données
![68747470733a2f2f6d656469612e646973636f72646170702e6e65742f6174746163686d656e74732f3439393632343439303031363434303335302f313137343634363032353532353430373737342f64622e73716c697465332e706e673f65783d36353638353935632669733d363535356534356326686d3d623438](https://github.com/ernoux41m/Projet-doctolib/assets/16134455/b5df4037-af29-4513-a5f1-a28ef8121a90)


## *Initialisation du projet*

Pour démarrer le projet, voici les étapes à suivre :

***Optionnel :** Vous pouvez créer un environnement virtuel pour votre projet.*

1. **Installer les librairies**  
`pip install -r requirements.txt`

2. **Effectuer les migrations**  
`python manage.py migrate`

3. **Créer un super user**  
`python manage.py createsuperuser`

4. **Lancer le serveur**  
`python manage.py runserver`

5. **Attribuer le rôle de responsable au super user**
   - Aller sur la page administrateur  
[`http://127.0.0.1:8000/admin`](http://127.0.0.1:8000/admin)

   - Se connecter avec le super user

   - Aller dans la liste des utilisateurs

   - Cliquer sur l'Id du super user pour le modifier

   - Attribuer le rôle "responsable" au super user  

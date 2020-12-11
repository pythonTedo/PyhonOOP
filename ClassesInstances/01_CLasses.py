# class Person:
#     def __init__ (self, name):
#         self.name = name
#        # print(f'Init method for person is {name}')

#     def say_hello(self):
#         print(f'{self.name} is saying Hello')
# Person('Gosho').say_hello()
# Person('Marto').say_hello()
############################################################
# class Book:
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages

# book = Book('HP', 'JK Rolling', 500)

# print(book.name)
# print(book.author)
# print(book.pages)
############################################################
# class Car:
#     def __init__(self, name, model, engine):
#         self.name = name
#         self.model = model
#         self.engine = engine

#     def get_info(self):
#         return(f'This is {self.name} {self.model} with engine {self.engine}')

# car = Car('Kia', 'Rio', '1.3L B3')

# print(car.get_info())
# #car.get_info()
############################################################
# class Shop:
#     def __init__(self, name, items):
#         self.name = name
#         self.items = items
    
#     def get_items_count(self):
#         return(len(self.items))

# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])

# print(shop.get_items_count())
############################################################
# class Hero:
#     def __init__(self, name, health):
#          self.name = name
#          self.health = health

#     def defend(self, damage):
#         self.health = self.health - damage
#         if self.health == 0 or self.health < 0:
#             return(f"{self.name} was defeated") 

#     def heal(self, ammount):
#         self.health = self.health + ammount

# hero = Hero("Peter", 100)

# print(hero.defend(50))
# hero.heal(50)
# print(hero.defend(99))
# print(hero.defend(1))
############################################################
# class SteamUser:
#     def __init__(self, username, games):
#         self.username = username
#         self.games = games
#         self.played_hours = 0

#     def play(self, game, hours):
#         if game in self.games:
#             self.played_hours += hours
#             return(f"{self.username} is playing {game}")
#         else:
#             return(f"{game} is not in library")

#     def buy_game(self, game):
#         if game in self.games:
#             return(f"{game} is already in your library")
#         else:
#             self.games.append(game)
#             return(f"{self.username} bought {game}")
    
#     def stats(self):
#         return(f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}")


# user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
# print(user.play("Fortnite", 3))
# print(user.play("Oxygen Not Included", 5))
# print(user.buy_game("CS:GO"))
# print(user.buy_game("Oxygen Not Included"))
# print(user.play("Oxygen Not Included", 6))
# print(user.stats())
############################################################
# class Programmer:
#     def __init__(self, name, language, skills):
#          self.name = name
#          self.language = language
#          self.skills = skills

#     def watch_course(self, course_name, language, skills_earnd):
#         if self.language == language:
#             self.skills += skills_earnd
#             return(f"{self.name} watched {course_name}")
#         else:
#             return(f"{self.name} doesn't know {language}")
    
#     def change_language(self, new_language, skills_needed):
#         if self.skills >= skills_needed and self.language != new_language:
#             old_language = self.language
#             self.language = new_language
#             return(f"{self.name} switched form {old_language} to {self.language}")
#         elif self.skills >= skills_needed and self.language == new_language:
#             return(f"{self.name} already knows {new_language}")
#         else:
#             return(f"{self.name} needs {skills_needed - self.skills} more skills")

# programmer = Programmer("John", "Java", 50)
# print(programmer.watch_course("Python Masterclass", "Python", 84))
# print(programmer.change_language("Java", 30))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Java: zero to hero", "Java", 50))
# print(programmer.change_language("Python", 100))
# print(programmer.watch_course("Python Masterclass", "Python", 84))
#########################################################################################################################################
from typing import List

# class Pokemon:
#     def __init__(self, name, health: int):
#         self.name = name
#         self.health = health

#     def pokemon_details(self):
#         return f"{self.name} with health {self.health}"

# class Trainer:
#     def __init__(self, name: str):
#         self.name = name
#         self.pokemons = []

#     def add_pokemon(self, pokemon: Pokemon):
#         if pokemon in self.pokemons:
#             return "This pokemon is already caught"
#         self.pokemons.append(pokemon)
#         return(f"Caught {pokemon.pokemon_details()}")

#     def release_pokemon(self, pokemon_name: str):
#         for poke in self.pokemons:
#             if poke.name == pokemon_name:
#                 self.pokemons.remove(poke)
#                 return f"You have released {pokemon_name}"
#         return "Pokemon is not caught"

#     def trainer_data(self):

#         lop = ""
#         for n in self.pokemons:
#             lop += f"- {n.pokemon_details()} \n"

#         return (f"Pokemon Trainer {self.name}\n Pokemon count {len(self.pokemons)}\n" + lop)
        

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
#########################################################################################################################################
# class Player:                                                     NOT DONE
#     def __init__(self, name: str, hp: int, mp: int):
#          self.name = name
#          self.hp = hp
#          self.mp = mp
#          self.skills = {}
#          self.guild = "Unffiliated"
    
#     def add_skill(self, skill_name, mana_cost):
#         if skill_name in self.skills.keys():
#             return "Skill already added"
#         self.skills.update({skill_name: mana_cost})
#         return f"Skill {skill_name} added to the collection of the player {self.name}"
    
#     def player_info(self):
#         lop = ""
#         for x, y in self.skills.items():
#             lop += f"=== {x} - {y} \n"

#         return f"Name: {self.name}\n Guild: {self.guild}\n HP: {self.hp}\n MP: {self.mp}\n + {lop}"

# class Guild:
#     def __init__(self, name: str):
#         self.name = name
#         self.guild_list: List[Player]= []

#     def assign_player(self, player: Player):
#         if player.name in self.guild_list:
#             return f"Player {player.name} is already in the guild."

#         elif player.name not in self.guild_list and player.guild != "Unffiliated":
#             return f"Player {player.name} is in another guild"
#         else:
#             player.guild = self.name
#             self.guild_list.append(player.name)
#             return f"Welcome player {player.name} to the guild {self.name}"
    
#     def guild_info(self):
        
#         info = ""
#         for n in self.guild_list:
#             info += f"{n.name.player_info()}\n"
#         return f"Guild: {self.name}\n {info}"
            

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
#########################################################################################################################################
class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single
    
    def get_info(self):
        return f"{self.name} - {self.length}"

class Album:
    def __init__(self, name: str, songs):  ## nie ochakvame list ot pesni obache ni davat samo 1 pesen
        self.name = name
        
        if not isinstance(songs, list):    ## provekra dali shte otgovarq na list
            self.songs = [songs]
        else:
            self.songs = songs

        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        
        if self.published:
            return f"Cannot add song. Album is published"
        
        if song in self.songs:
            return "Song is already added"

        else:
            self.songs.append(song) 
            return f"Song {song.name} has been added to the album {self.name}" 

    def remove_song(self, song_name: str):
        if song_name not in self.songs:
            return "Song is not in the album"

        elif self.published == True:
            return "Cannot remove songs. Album is published"
        
        else:
            self.songs.remove(song_name)
            return f"Removed song {song_name} from album {self.name}"
    
    def publish(self):
        if self.published == True:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published"

    def details(self):

        sng = ""
        for n in self.songs:
            sng += f"== {n.get_info()}\n"

        return f"Album {self.name}\n{sng}"


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []
    
    def add_album(self, album: Album):
        if album.name in self.albums:
            return f"Band {self.name} already has {album.name} in their libary."
        self.albums.append(album) 
        return f"Band {self.name} has added thir newest album {album.name}"
    
    def remove_album(self, album_name: str):
        albums_list = [a for a in self.albums if a.name == album_name]
        
        if albums_list:           ## davidq dali vuobshte imame neshto v kolekciqta
            album = albums_list[0] ## imeto na albuma e ot [0]
            if album.published:
                return f'Album has been published. It cannot be removed.'
            if album not in self.albums:
                return f"Album {album_name} is not found."
        else:
            self.albums.remove(album)
            return f"Album {album} has been removed."

    def details(self):

        lop = ""

        for al in self.albums:
            lop += f"{al.details()}\n"
        return f"Band {self.name}\n{lop}"



song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)                       ## v song imame somo 1 pesen
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

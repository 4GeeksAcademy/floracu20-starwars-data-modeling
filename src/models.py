import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    homeworld = Column(Integer, ForeignKey('planet.id'), nullable=False)
    homeworld_relationship = relationship("Planet", back_populates="residents")
    films = relationship("Film", secondary="film_character", back_populates="characters")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(90), nullable=False)
    terrain = Column(String(90), nullable=False)
    diameter = Column(Integer, nullable=False)
    url = Column(String(80), nullable=False)
    residents = relationship("People", back_populates="homeworld")
    films = relationship("Film", secondary="film_planet", back_populates="planets")

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    model = Column(String(90), nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    url = Column(String(80), nullable=False)
    members = relationship("People", back_populates="starship")
    films = relationship("Film", secondary="film_starship", back_populates="starships")

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    episode_id = Column(Integer, nullable=False)
    planets = Column(String(550), nullable=False)
    characters = Column(String(550), nullable=False)
    starships = Column(String(550), nullable=False)
    url = Column(String(80), nullable=False)
    planets = relationship("planet", secondary="film_planet", back_populates="films")
    characters = relationship("People", secondary="film_character", back_populates="films")
    starships = relationship("Starship", secondary="film_starship", back_populates="films")  

# Tablas intermedias para las relaciones muchos a muchos

# Relación muchos a muchos entre Film y Planet
class FilmPlanet(Base):
    __tablename__ = 'film_planet'
    film_id = Column(Integer, ForeignKey('film.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), primary_key=True)

# Relación muchos a muchos entre Film y Starship
class FilmStarship(Base):
    __tablename__ = 'film_starship'
    film_id = Column(Integer, ForeignKey('film.id'), primary_key=True)
    starship_id = Column(Integer, ForeignKey('starship.id'), primary_key=True)

# Relación muchos a muchos entre Film y People (personajes)
class FilmCharacter(Base):
    __tablename__ = 'film_character'
    film_id = Column(Integer, ForeignKey('film.id'), primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)  

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

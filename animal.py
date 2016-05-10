from flask import Flask
import random
app = Flask(__name__)
class Animal(object):
	def __init__(self,name,health):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
	def run(self):
		self.health -=5
	def displayHealth(self):
		print self.name
		print self.health
class Dog(Animal):
	def __init__(self,name,health):
		self.name = name
		self.health = 150
	def pet(self):
		self.health +=5
class Dragon(Animal):
	def __init__(self,name,health):
		self.name = name
		self.health = 170
	def fly(self):
		self.health -= 10
	def displayHealth(self):
		print "this is a dragon"
		print self.name
		print self.health

animal = Animal("animal",100)
animal.walk()
animal.walk()
animal.walk()
animal.run()
animal.run()
animal.displayHealth();
dog = Dog("Dog",150)
dog.walk()
dog.walk()
dog.walk()
dog.run()
dog.run()
dog.pet()
dog.displayHealth();
dragon = Dragon("dragon",170)
dragon.walk()
dragon.walk()
dragon.walk()
dragon.run()
dragon.run()
dragon.fly()
dragon.displayHealth();

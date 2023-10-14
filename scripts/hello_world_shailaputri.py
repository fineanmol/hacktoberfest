'''This is my first contribution towards Hacktoberfest 2023.
I have forked this repo from fineanmol.
Here I present a unique way to say "Hello, World!" in a language of your choice. 
I have made the code extremely modular and reusable, owning upto the DRY principle. 
It incorporates several design patterns like factory and strategy.
The API creates script based on the language of choice provided by the user. 
Hope you have a fun time learning how to say Hello World in different langugages.'''


from abc import ABC, abstractmethod
from enum import Enum

class ValidLang(Enum):
	Python = 1
	C = 2
	CPP = 3
	Java = 4
	CSharp = 5
	JavaScript = 6
	PHP = 7
	Swift = 8
	Ruby = 9
	Kotlin = 10

	@classmethod
	def choices(cls):
		return [(key.value, key.name) for key in cls]

	#models
class Person:
	def __init__(self, name='Anon', location='IND'):
		self.name = name
		self.location = location
		self.lang = None
	def __str__(self):
		return f"Hi {self.name} from {self.location}."
	def setLang(self):
		return self.lang
	def getLang(self, lang):
		self.lang = lang


#Strategies for different language
class LangCodeStrategy(ABC):
	@abstractmethod
	def printHelloWorld(self):
		pass

class PythonLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('print("Hello, world!")')

class CLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('#include <stdio.h> \n int main() \n {printf("Hello, World!"); \n return 0; \n}')

class CPPLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('#include <iostrean> \n int main() \n {printf("Hello, World!"); \n return 0; \n}')

class JavaLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('public class Program \n {public static void main(String[] args) \n {System.out.print("Hello, World!")} \n }\n}')

class CSharpLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('using System; \n namespace Hello \n {class Program {\n static void Main (string[] args) \n { Console.WriteLine("Hello, World!"); \n }}} \n}')

class JSLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('console.log("Hello, World!");')

class PHPLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('<?php \n echo "Hello, World!"; \n?>')

class SwiftLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('print("Hello, world!")')

class RubyLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('puts "Hello, world!"')

class KotlinLangCode(LangCodeStrategy):
	def printHelloWorld(self):
		print('fun main(args: Array<String>) \n {print("Hello, World!");}\n')

class LangCodeFactory:

	def __init__(self):
		self.pythonLangCode = PythonLangCode()
		self.cLangCode = CLangCode()
		self.cppLangCode = CPPLangCode()
		self.javaLangCode = JavaLangCode()
		self.cSharpLangCode = CSharpLangCode()
		self.jsLangCode = JSLangCode()
		self.phpLangCode = PHPLangCode()
		self.swiftLangCode = SwiftLangCode()
		self.rubyLangCode = RubyLangCode()
		self.kotlinLangCode = KotlinLangCode()

	def setLangCode(self, lang):

		
		# if lang== 'Python' : return self.pythonLangCode
		# else : return f"Not a valid language"
		
		if lang== ValidLang.Python : return self.pythonLangCode
		elif lang == ValidLang.C : return self.cLangCode
		elif lang == ValidLang.CPP : return self.cppLangCode
		elif lang == ValidLang.Java : return self.javaLangCode
		elif lang==ValidLang.CSharp : return self.cSharpLangCode
		elif lang ==ValidLang.JavaScript : return self.jsLangCode
		elif lang ==ValidLang.PHP: return self.phpLangCode
		elif lang == ValidLang.Swift : return self.swiftLangCode
		elif lang == ValidLang.Ruby :  return self.rubyLangCode
		elif lang == ValidLang.Kotlin : return self.kotlinLangCode
		else: return f"Not a valid lang"


class HelloWorld:
	def createscript(self, person):
		langCodeFactory = LangCodeFactory()
		langCodeStrategy = langCodeFactory.setLangCode(person.setLang())
		langCodeStrategy.printHelloWorld()

def main():
	print('Say Hello, World! in the language of your choice!')
	print(f'We offer these languages: {ValidLang.choices()}')
	print('__________________________')

	print("Please introduce yourself: Name (space) Place (space) Language")
	name, place, choice = input().split(' ')
	return name, place, int(choice)

def testing():
	print('Say Hello World in the language of your choice!')
	print(f'We offer these languages: {ValidLang.choices()}')
	print('__________________________')
	print("Please introduce yourself: Name (space) Place (space) Language")
	name, place, choice = 'Mark','USA',10
	return name, place, int(choice)

	



if __name__ == '__main__':
	# name, place, choice = main()
	name, place, choice = testing()
	person = Person(name, place)
	print(str(person))
	person.getLang(ValidLang(choice))
	print("\n\nYour script is loading...")
	print('\n================= \n\n')
	hello_world = HelloWorld()
	hello_world.createscript(person)
	print('\n\n=================\n\n')

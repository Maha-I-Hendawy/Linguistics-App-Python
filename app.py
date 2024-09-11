class Text:
	def __init__(self, text):
		self.text = text 

	def __str__(self):
		return f"{self.text}"

	def words(self):
		word = [w.replace('.', '') for w in self.text.split(' ')]
		print(word)


	def sentences(self):
		sentence = [s.replace('.', '') for s in self.text.split('.')]
		print(sentence)






txt = Text("this is a sentence. this is another sentence, and that's another sentence")

print(txt) 

txt.words()

txt.sentences()
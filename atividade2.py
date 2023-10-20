import requests
import re
import numpy
from bs4 import BeautifulSoup

errors = []

punctuation_pattern = r'\s+[.,;!?]'
lower_case_word_pattern = r'\. \s*([a-z]+)'
plural_discordance_pattern = r'\b(os|uns)\s+[aeiouáàâãéèêíìóòôõúùAEIOUÁÀÂÃÉÈÊÍÌÓÒÔÕÚÙ]\b|\b(as|umas)\s+[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\b'
discordance_pattern = r'\b(a|uma)\s+[a-zA-Z]+[b-z]$'
space_pattern = r'[a-zA-Z]+  [a-zA-Z]+'
question_space_pattern = r'\?[a-zA-Z]+|\s+\?'

chapter_6 = requests.get("https://brasileiraspln.com/livro-pln/1a-edicao/parte4/cap6/cap6.html")
chapter_20 = requests.get("https://brasileiraspln.com/livro-pln/1a-edicao/parte8/cap20/cap20.html")

chapter_6_paragraphs = BeautifulSoup(chapter_6.content, 'html.parser').find("main", {"class": "content"}).find_all("p")
chapter_20_paragraphs = BeautifulSoup(chapter_20.content, 'html.parser').find("main", {"class": "content"}).find_all("p")

chapters = numpy.append(chapter_6_paragraphs, chapter_20_paragraphs)

for p in chapters:
  text = p.get_text()

  plural_matches = re.findall(plural_discordance_pattern, text)
  punctuation_matches = re.findall(punctuation_pattern, text)
  lower_case_matches = re.findall(lower_case_word_pattern, text)
  discordance_matches = re.findall(discordance_pattern, text)
  space_matches = re.findall(space_pattern, text)
  question_space_matches = re.findall(question_space_pattern, text)

  if (punctuation_matches):
    errors.append(punctuation_matches)
  if (plural_matches):
    errors.append(plural_matches) 
  if (lower_case_matches):
    errors.append(lower_case_matches)
  if (discordance_matches):
    errors.append(discordance_matches)          
  if (space_matches):
    errors.append(space_matches)     
  if (question_space_matches):
    print(question_space_matches)
    errors.append(question_space_matches)        

print(len(errors))

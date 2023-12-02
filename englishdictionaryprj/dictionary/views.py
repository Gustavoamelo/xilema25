from django.shortcuts import render, redirect
from PyDictionary import PyDictionary
from googletrans import Translator

def home(request):
    return render(request, 'home.html')

def word(request):
    search = request.GET.get('search')

    if not search:
        # Se a palavra de busca estiver vazia, redirecione para a página inicial
        return redirect('home')

    # Traduzir a palavra para inglês
    translator = Translator()
    translated_word = translator.translate(search, src='pt', dest='en').text

    dictionary = PyDictionary()
    meaning = dictionary.meaning(translated_word)
    antonyms = dictionary.antonym(translated_word)
    synonyms = dictionary.synonym(translated_word)

    context = {
        'meaning': meaning['Noun'][0] if meaning and 'Noun' in meaning else 'Não encontrado',
        'antonyms': antonyms if antonyms else ['Não encontrado'],
        'synonyms': synonyms if synonyms else ['Não encontrado'],
    }
    return render(request, 'word.html', context)

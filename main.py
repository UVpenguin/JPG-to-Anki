import genanki
import os
import random; 

#name flashcards
_name_ = input("name of flashcards:\n")
directory = os.getcwd() #gets directory of this python file
list_of_images_in_dir = []
total_images = 0
newid = random.randrange(1 << 30, 1 << 31) #creates a random and new deck id

my_model = genanki.Model( ## creates model anki card

  121212,
  'Basic',
  fields=[
    {'name': 'Front'},
    {'name': 'Back'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Front}}',
      'afmt': '<hr id="answer">{{Back}}',
    },
  ])

my_deck = genanki.Deck( #creates anki deck
  newid,
  _name_)

for filename in os.listdir(directory): #loops through each python file in 'directory'
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            total_images += 1   
            list_of_images_in_dir.append(filename) 

print("total images in dir: "+str(total_images))

for c in range(total_images):
    if c % 2 == 0: #skips odd number files, because flashcard question are on even numbers and answers are on odd
        try: my_note = genanki.Note( #adds note to deck
            model=my_model,
            fields=[f'<img src={list_of_images_in_dir[c]}>', f'<img src={list_of_images_in_dir[c+1]}>'])
        except:
            print('odd number of images')
            input('press Enter to Close Window...')
            exit()
        my_deck.add_note(my_note)
        print("note "+str(c)+" added")


print("Total Cards Added: " + str(total_images/2))


my_package = genanki.Package(my_deck)
my_package.media_files = list_of_images_in_dir

my_package.write_to_file('output.apkg')
print("done")
input("Press Enter to Close Window...")

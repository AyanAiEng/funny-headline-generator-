import random

# List of politicians
politicians = [
    "Imran Khan",
    "Shehbaz Sharif",
    'Bilawal Bhutto Zardari',
    'Asif Ali Zardari',
    'Nawaz Sharif',
    'Maryam Nawaz',
    'Fawad Chaudhry',
    'Rana Sanaullah',
    'Maulana Fazlur Rehman',
    'Pervez Musharraf',
    'Sheikh Rasheed',
    'Donald Trump',
]

# List of sports personalities
sports_man = [
    'Virat Kohli',
    'MS Dhoni',
    'Babar Azam',
    'Ronaldo',
    'Messi',
    'Usain Bolt',
    'Shoaib Malik',
    'Mohammad Rizwan',
    'Shoaib Akhtar',
    'Shahid Afridi',
    'Wasim Akram',
    'Sachin Tendulkar',
    'Rohit Sharma',
]

# List of actors
actors = [
    'Humayun Saeed',
    "Mahira Khan",
    "Fawad Khan",
    "Feroze Khan",
    "Imran Abbas",
    "Ahad Raza Mir",
    "Shah Rukh Khan",
    "Salman Khan",
    "Aamir Khan",
    "Akshay Kumar",
    "Alia Bhatt",
    "Priyanka Chopra",
    "Deepika Padukone"
]

# List of funny actions
actions = [
    'gets stuck in a vending machine',
    'starts dancing in slow motion',
    'declares war on mosquitoes',
    'accidentally eats shampoo',
    'challenges a pigeon to a staring contest',
    'slaps a statue thinking it’s a real person',
    'talks to his reflection for 2 hours',
    'gets lost in their own house',
    'tries to charge a banana',
    'mistakes shampoo for mic and sings',
    'joins a kindergarten class by mistake',
    'gives a speech to an empty room',
    'argues with Siri in public',
    'orders pizza to the Parliament',
    'gets arrested for over-smiling',
    'claims to see ghosts in the mirror',
    'trips while waving at fans',
    'starts doing push-ups during a speech',
    'mistakes a chair for a person',
    "tries to ride a cat thinking it's a lion",
    'does stand-up comedy unintentionally',
    'blames gravity for failure',
    'mistakes ketchup for sanitizer',
    'calls 911 after losing his pen',
    'delivers speech while sleepwalking',
    'joins a protest against himself',
    'gets chased by a chicken',
    'declares himself invisible',
    'tries to swim in a fountain',
    'starts crying during a haircut',
    'laughs at his own shadow',
    'eats paper thinking it’s cake',
    'argues with a traffic cone',
    'gets hypnotized by a mirror',
    'tries to unlock a door with a spoon',
    'gets caught playing hide and seek alone',
    'mistakes a fire alarm for a doorbell',
    'does yoga in an elevator',
    'starts barking during a serious meeting',
    'paints mustache on his own face',
    'applies makeup with peanut butter',
    'starts a rap battle in a courtroom',
    'sings lullabies at a press conference',
    'tried to microwave ice cream',
    'tried to plant a tree in a swimming pool',
    'throws his phone thinking it’s a boomerang',
    'puts sunglasses on at night and walks into a wall',
    'starts dancing after reading a sad story',
    'faints after seeing his own meme',
    'mistook a washing machine for a time machine'
]

# Locations for each category
politicians_places = [
    'in Supreme Court',
    'in Oxford Library',
    'in the Cabinet Meeting Room',
    'in Parliament',
    'in the Conference Hall',
    'in a hospital',
    'in a graveyard',
    'in the Board Meeting Room',
    'at a children’s play area',
    'at a wedding dance floor',
    'during a wedding',
    'with the Prime Minister',
]

circket_places = [
    'in a cricket stadium',
    'at a post-match press conference',
    'at a sports university',
    'in a library',
    'in a hospital',
    'in a washroom',
    'at the gym',
    'in front of Burj Khalifa',
    'at a training academy',
    'at sponsorship events',
    'in front of Quaid-e-Azam’s grave',
    'at a vaccination center',
    'at youth development programs',
    'in the sports ministry office',
    'in Supreme Court',
    'in a graveyard',
]

actors_places = [
    'at a script reading session',
    'in an audition room',
    'on a film set',
    'in a graveyard',
    'in a library',
    'in Supreme Court',
    'at a police station',
    'in an embassy',
    'at the passport office',
    'at a youth talent hunt',
    'in front of Quaid-e-Azam’s grave',
    'in a university',
    'in front of Burj Khalifa',
]

# Headline generation function
def fake_headlines_generator(subject_list, place_list):
    subject = random.choice(subject_list)
    action = random.choice(actions)
    place = random.choice(place_list)
    return f"Breaking News: {subject} {action} {place}!"

# Welcome message
print('Welcome to the Fake News Generator!')

# Main loop
while True:
    try:
        user_cate = int(input('\nSelect an option:\n1: Sports\n2: Politics\n3: Actors\n4: Exit\nYour choice (1-4): '))
    except ValueError:
        print('Enter a valid number.')
        continue

    if user_cate == 1:
        subject = sports_man
        place = circket_places
    elif user_cate == 2:
        subject = politicians
        place = politicians_places
    elif user_cate == 3:
        subject = actors
        place = actors_places
    elif user_cate == 4:
        print('Thank you for using the Fake News Headline Generator. Have a fun day!')
        break
    else:
        print('Invalid input. Try again.')
        continue

    # Sub-loop for generating multiple headlines
    while True:
        headline = fake_headlines_generator(subject, place)
        print('\n' + headline)

        save_headline = input('Do you want to save this headline? (yes/no): ').strip().lower()
        if save_headline == 'yes':
            with open('save_jokes.txt', 'a', encoding='utf-8') as file:
                file.write(headline + '\n')
            print('Headline saved to save_jokes.txt.')
        else:
            print('Headline not saved.')

        again = input('Do you want more fake headlines? (yes/no): ').strip().lower()
        if again != 'yes':
            break

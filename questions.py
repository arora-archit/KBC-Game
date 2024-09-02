#writing questions to a text file
with open("Questions.txt","w")as obj:
    questions = [
  'In ODI Cricket, who created the record of scoring the fastest century in just 31 balls ?\n',
  'If you call someone ‘Makkhichoos’ then what are you calling him ?\n',
  'How many players of a Kho-Kho team can play on the field during the match ?\n',
  'Which of these Indian cities is closest to the Pakistani city of Lahore ?\n',
  'The language spoken by the people by Pakistan is ?\n',
  'The term “Googly” is associated with ?\n',
  'India first took part in the olympic games in the year ?\n',
  'Where are Kangaroos found ?\n',
  'Oval stadium in England is associated with ?\n',
  'In 2011 India won the World Cup. Who was adjudicated as the man of the series in the tournament ?\n',
  'Eden Gardens in Kolkata is ----- stadium.?\n',
  'Ronaldo is associated with ?\n',
  'Icc’s 2007, the World Cup Cricket was held in ?\n',
  'Wankhede Stadium is at ?\n',
  'World’s most ancient game is ?\n',
  'Stethoscope was invented by ?\n',
  'A dye is prepared from \n',
  'Which disease is caused by the fungi? \n',
  'Which is the Land of the Rising Sun? \n',
  'The desert that lies on the boundary between India and Pakistan is \n',
  'In which kingdom is the story of the ‘Bahubali’ series of films mainly set?\n',
  'What is the common name for surgery conducted on coronary arteries that supply blood to the heart ?\n',
  'In July 2017, Narendra Modi Become the first Indian Prime Minister to visit which country ?\n',
  'Which of these musical instrument is held in one hand and played with the other ?\n',
  'On the last day of his life Bhagat Singh was reading a book about the Ideology of which revolutionary ?\n',
  'Which Air force officer had the unique honour of leading the fly-post over the Red fort in Delhi on 15 August 1947 ?\n',
  'Which image appears on the flip side of the new 2000 Rs Note, launched in 2016?\n',
  'Which Indian hill station gets its name from the Tibetan words that mean "land of the thunderbolt"?\n',
  'Which of these diseases is transmitted by mosquitoes?\n',
  'Who among these has served as the Ambassador of India to the United Nations?\n',
  'Who was the first Indian to win the World Junior Badminton Championships?\n',
  'Which of the following is a recipient of the Nobel Peace Prize?\n',
  'The cave temples at the historical site of Elephanta are dedicated to which God?\n'
]
    obj.writelines(questions)

#writing options in another csv file
import csv
with open("Options.csv",'w',newline='')as cF:
    cW = csv.writer(cF)
    cW.writerow(['Option 1','Option 2','Option 3','Option 4'])
    options = [['Corey Anderson','AB De Villiers','Shahid Afridi','Rohit Sharma'],
               ['Evil','Humble','Dishonest','Miserly'],
               ['10','9','7','8'],
               ['Srinagar','Jaisalmer','Amritsar','Udhampur'],
               ['Hindi','Palauan','Sindhi','English'],
               ['Cricket','Football','Badminton', 'Hockey'],
               ['1920','1928','1972','1976'],
               ['Bangladesh','Kenya','Pakistan','Australia'],
               ['polo','Cricket','Hockey','Football'],
               ['Virat Kohli', 'Yuvraj Singh', 'M.S. Dhoni', 'Zaheer Khan'],
               ['Tennis', 'Cricket', 'Hockey', 'Polo'],
               ['Cricket', 'Football', 'Hockey', 'Tennis'],
               ['Australia','West Indies','South Africa','India'],
               ['Kolkata','Mumbai','Delhi','Jaipur'],
               ['Wrestling','Swimming','Boxing','Running'],
               ['Bessemer','Rane Laennec','Henry Becquerel','None of these',],
               ['Sida','Tridax','Tephrosia','Indigofera'],
               ['Polio','Malaria','Dermatitis','Cholera'],
               ['China','Taiwan','Japan','Australia'],
               ['Thar','Sahara','Gobi','None of these'],
               ['Magadh','Mahishmati','Kalinga','Badami'],
               ['Cataract','Gastric','Bypass','Debriment'],
               ['Israel','Jordan', 'Saudi Arabia','Qatar'],
               ['Tabla','Santoor', 'Mridangam','Dafli'],
               ['Antonio Gramsci','Che Guevera','Leon Trotsky','Vladimir Lenin'],
               ['Arjan Singh','Pratap Chandra Lal','Subroto Mukarjee','Aspy Engineer'],
               ['Parliament of India','Tractor','Red Fort','Mangalyaan'],
               ['Gangtok','Aizawl','Darjeeling','Kohima'],
               ['Rabies','Tetanus','Japanese Encephalitis','Plague'],
               ['Mohd Hamid Ansari','I K Gujral','Mohd Hidayatullah','Zakir Hussain'],
               ['P V Sindhu','Aparna Balan','Saina Nehwal','Jwala Gutta'],
               ['Mahatma Gandhi','Swami Vivekananda','Rabindranath Tagore','Mother Teresa'],
               ['Hanuman', 'Vishnu','Shiva','Kamadeva']]
    cW.writerows(options)
    

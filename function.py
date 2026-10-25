import random
def generate_headline():
 subjects=[ # Scientists & Innovators
    "Albert Einstein", "Isaac Newton", "Marie Curie", "Nikola Tesla", 
    "Charles Darwin", "Ada Lovelace", "Galileo Galilei", "Alan Turing", 
    "Louis Pasteur", "Stephen Hawking", "Tim Berners-Lee", "Thomas Edison",
    
    # Artists, Writers & Musicians
    "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo", 
    "William Shakespeare", "Jane Austen", "Mark Twain", "Virginia Woolf", 
    "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Frida Kahlo", "Claude Monet","ShahRukh Khan",
    
    # Historical & Political Leaders
    "Mahatma Gandhi", "Abraham Lincoln", "Nelson Mandela", "Winston Churchill", 
    "Martin Luther King Jr.", "George Washington", "Julius Caesar", "Cleopatra", 
    "Alexander the Great", "Queen Elizabeth I", "Napoleon Bonaparte", "Simon Bolivar",
    
    # Thinkers & Philosophers
    "Socrates", "Plato", "Aristotle", "Confucius", "Rene Descartes", 
    "Immanuel Kant", "Friedrich Nietzsche", "Karl Marx", "Voltaire",
    
    # Modern Pioneers & Icons
    "Steve Jobs", "Bill Gates", "Neil Armstrong", "Amelia Earhart", 
    "Rosa Parks", "Malala Yousafzai", "Mother Teresa", "Jane Goodall"
 ]


 actions = [
    # Physical Movements
    "runs a marathon", "swims across the channel", "climbs Mount Everest", 
    "dances gracefully", "jumps over the hurdle", "walks in the park", 
    "flies a plane", "rides a bicycle", "explores a hidden cave",
    
    # Intellectual & Creative Actions
    "writes a bestselling novel", "solves a complex riddle", "paints a masterpiece", 
    "invents a time machine", "composes a beautiful symphony", "codes a new app", 
    "discovers a new planet", "reads a fascinating book", "designs a futuristic building",
    
    # Daily & Social Activities
    "cooks a delicious gourmet meal", "bakes a chocolate cake", "gives a speech", 
    "helps a stranger", "sings a catchy song", "tells a funny joke", 
    "plants a beautiful garden", "brews a cup of coffee", "learns a new language",
    
    # Adventurous & Dramatic Actions
    "defeats a mythical dragon", "travels back in time", "uncovers a secret conspiracy", 
    "performs a daring magic trick", "escapes from a maze", "rescues a stranded kitten", 
    "wins a championship trophy", "sails across the stormy ocean"
 ]

 places_elements = [
    # Taj Mahal Features
    "inside the Main Mausoleum Dome", 
    "near the Four Corner Minarets", 
    "near the Yamuna Riverfront Terrace", 
    "near the Central Reflecting Pool", 
    "inside the Taj Mahal Mosque", 
    "inside the Jawab Assembly Hall", 
    "near the Great Gate (Darwaza-i-rauza)", 
    "inside the Charbagh Gardens", 
    "near the Taj Museum",
    
    # Agra Fort Features
    "inside the Sheesh Mahal (Mirror Palace)", 
    "inside the Diwan-i-Am", 
    "inside the Diwan-i-Khas", 
    "near the Khas Mahal", 
    "near the Jahangiri Mahal", 
    "inside the Musamman Burj (Octagonal Tower)", 
    "inside the Moti Masjid", 
    "inside the Nagina Masjid", 
    "inside the Anguri Bagh (Grape Garden)", 
    "near the Amar Singh Gate", 
    "near the Delhi Gate moat"
  ]
 return f"{random.choice(subjects)}{random.choice(actions)}{random.choice(places_elements)}"






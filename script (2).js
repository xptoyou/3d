document.getElementById('generate').addEventListener('click', function() {
  const adjectives = ['Quick', 'Lazy', 'Clever', 'Happy', 'Bright', 'Brave', 'Mighty', 'Cool'];
  const animals = ['Tiger', 'Eagle', 'Shark', 'Dragon', 'Wolf', 'Lion', 'Panda', 'Falcon'];

  const randomAdjective = adjectives[Math.floor(Math.random() * adjectives.length)];
  const randomAnimal = animals[Math.floor(Math.random() * animals.length)];

  const username = randomAdjective + randomAnimal + Math.floor(Math.random() * 1000);

  document.getElementById('username').textContent = username;
});

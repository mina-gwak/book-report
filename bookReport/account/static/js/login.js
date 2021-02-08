const form = document.querySelector('.login');
const checkLabel = form.querySelector('.check-label');
const submitBtn = form.querySelector('button');
const inputID = form.querySelector('.user-id');

function getID() {
  const id = localStorage.getItem('userID');
  if (id !== null) {
    inputID.value = id;
  }
}

function saveID(id) {
  localStorage.setItem('userID', id);
}

function handleClick(e) {
  const label = e.target.parentNode.querySelector('.check-label');
  if (label.classList.contains('active')) {
    const id = e.target.parentNode.querySelector('.user-id').value;
    saveID(id);
  } else {
    localStorage.removeItem('userID');
  }
}

function clickCheckBtn(e) {
  checkLabel.classList.toggle('active');
}

function init() {
  checkLabel.addEventListener('click', clickCheckBtn);
  submitBtn.addEventListener('click', handleClick);
  getID();
}

init();
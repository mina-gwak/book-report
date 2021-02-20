function showDiv(div) {
  div.classList.add('show');
}

function init() {
  const div = document.querySelector('.result-div');
  const li = div.querySelector('li');
  console.log(li !== null);
  if (li !== null) {
    showDiv(div);
  }
}

init();

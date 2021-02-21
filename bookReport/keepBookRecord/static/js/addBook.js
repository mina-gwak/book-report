const startDate = document.querySelector('#start-date');
const endDate = document.querySelector('#end-date');
const bookContainer = document.querySelector('.book-container');
const readingTrue = bookContainer.querySelector('#reading-true');
const readingFalse = bookContainer.querySelector('#reading-false');
const quotationBtn = document.querySelector('.quotation-btn');

function saveQuotation(e) {
  e.preventDefault();
  const content = e.target.parentNode.querySelector('textarea');
  const page = e.target.parentNode.querySelector('input[type="text"]');
  const date = e.target.parentNode.querySelector('input[type="date"]');
  content.disabled = true;
  page.disabled = true;
  e.target.parentNode.removeChild(e.target);
  quotationBtn.classList.remove('hide');
}

function addQuotation() {
  quotationBtn.classList.add('hide');
  const quotationList = document.querySelector('.quotations-list');
  const countLi = quotationList.childElementCount;
  const li = document.createElement('li');
  const content = document.createElement('textarea');
  const page = document.createElement('input');
  const span = document.createElement('span');
  const date = document.createElement('input');
  const btn = document.createElement('button');
  li.id = countLi + 1;
  content.name = 'q-content-' + (countLi + 1);
  content.id = 'q-content-' + (countLi + 1);
  page.type = 'text';
  page.id = 'q-page-' + (countLi + 1);
  span.textContent = 'P';
  date.type = 'date';
  date.id = 'q-date-' + (countLi + 1);
  setDate(date);
  date.disabled = true;
  btn.type = 'click';
  btn.textContent = 'Save';
  btn.addEventListener('click', saveQuotation);
  li.appendChild(content);
  li.appendChild(page);
  li.appendChild(span);
  li.appendChild(date);
  li.appendChild(btn);
  quotationList.appendChild(li);
}

function checkRadio(option) {
  if (option.id === 'reading-true') {
    endDate.disabled = true;
    endDate.value = '';
  } else if (option.id === 'reading-false') {
    endDate.removeAttribute('disabled');
    setDate(endDate);
  }
}

function setDefaultRadio() {
  readingTrue.checked = true;
}

function setDate(date) {
  date.value = new Date().toISOString().substring(0, 10);
}

function init() {
  setDefaultRadio();
  setDate(startDate);
  bookContainer.addEventListener('click', function(e) {
    let option = e.target;
    if (option.tagName !== 'INPUT') return;
    checkRadio(option)
  });
  quotationBtn.addEventListener('click', addQuotation);
}

init();
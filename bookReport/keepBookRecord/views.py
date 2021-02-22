from django.shortcuts import render, redirect
import json
import urllib.request

# Create your views here.
def main(request):
  return render(request, 'main.html')

def search(request):
  if request.method == 'POST':
    client_id = 'm6nHRQVrwpdwZNxZ5U8S'
    client_secret = 'gUDV44fcz4'

    book_name = request.POST.get('bookName')
    encText = urllib.parse.quote("{}".format(book_name))
    url = "https://openapi.naver.com/v1/search/book.json?query=" + encText

    book_api_request = urllib.request.Request(url)
    book_api_request.add_header("X-Naver-Client-Id", client_id)
    book_api_request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(book_api_request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        items = result.get('items')

        context = {
          'items': items
        }
        return render(request, 'search.html', context=context)
  return render(request, 'search.html')

def addBook(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    pubdate = request.POST.get('pubdate')
    author = request.POST.get('author')
    publisher = request.POST.get('publisher')
    image = request.POST.get('image')
    info = {
      'title': title,
      'pubdate': pubdate,
      'author' : author,
      'publisher' : publisher,
      'image' : image
    }
  return render(request, 'addBook.html', {'info': info})

def saveRecord(request):
  return redirect('main')
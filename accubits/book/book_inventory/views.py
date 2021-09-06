from django.http import JsonResponse
from .models import Book, BookBorrow
from .form import BookForm
import json
from .authenticator import get_user_details, validate_user
# Create your views here.


@validate_user
def book_handler(request):
    # add a book api
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            frm = BookForm(data)
            if frm.is_valid():
                book = Book(name=data['name'], author=data['author'], count=data['count'])
                book.save()

                return JsonResponse({"msg": "added successfully", "resp": {"id": book.pk}, "status": 200, "error": ""})
        except  Exception as err:
            response = {"error": str(err), "status": 500, "msg": "", "resp": {}}
            return JsonResponse(response)

    # get all books api
    if request.method == 'GET':
        try:
            books = Book.objects.all()
            res = []
            for book in books:
                res.append({"name": book.name,
                            "count": book.count,
                            "author": book.author,
                            "id": book.id})

            return JsonResponse({"msg": "", "resp": res, "status": 200, "error": ""})
        except Exception as err:
            response = {"error": str(err), "status": 500, "msg": "", "resp": {}}
            return JsonResponse(response)

@validate_user
def get_book_detail(request, id=None):
    if request.method == "GET":
        try:
            if id is not None:
                book_detail = Book.objects.filter(pk=id)
                book = book_detail[0]
                book = {"name": book.name, "author": book.author, "count": book.count, "id": book.id}
                return JsonResponse({"msg": "success", "resp": book, "status": 200, "error": ""})
        except Exception as err:
            response = {"error": str(err), "status": 500, "msg": "", "resp": {}}
            return JsonResponse(response)


@validate_user
def borrow_book(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            book_id = data['book_id']
            date = data['date']
            user = get_user_details(request.META['HTTP_AUTHORIZATION'])

            borrow = BookBorrow(book_id=book_id, date=date, user_id=user.id)
            borrow.save()
            return JsonResponse({"msg": "Success", "resp": {"book_id": book_id, "user_id": user.id},
                                 "status": 200, "error": ""})
        except  Exception as err:
            response = {"error": str(err), "status": 500, "msg": "", "resp": {}}
            return JsonResponse(response)

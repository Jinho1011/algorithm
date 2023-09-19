import sys
N=int(sys.stdin.readline())

book_list={}
for _ in range(N):
    book_name=sys.stdin.readline().strip()
    if book_name not in book_list:
        book_list[book_name]=1
    else:
        book_list[book_name]+=1

max_sell_book=[]
for book in book_list:
    if len(max_sell_book)==0:
        max_sell_book.append(book)
    elif book_list[max_sell_book[0]]==book_list[book]:
        max_sell_book.append(book)
    elif book_list[max_sell_book[0]]<book_list[book]:
        max_sell_book.clear()
        max_sell_book.append(book)
    else:
        continue

max_sell_book.sort()

print(max_sell_book[0])


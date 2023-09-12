# MEMO
```python
import sys
input = sys.stdin.readline
```

<br>

## 문자열
`count("str")` : 개수

<br>

## Math

`round(num)` : 반올림<br>
`Math.ceil(num)` : 올림<br>
`Math.floor(num)` : 내림<br><br>

### 순열과 조합
```python
import itertools

listName = [val1, val2, ...]
itertools.permutations(listName, num) # 순열
itertools.combinations(listName, num) # 조합
```
 <br>

> 큰 리스트 안에 조합을 리스트로 저장
> 
> `list(map(list, itertools.combinations(cardNum, 3)))` <br>
> -> [[val1, val2, ...], [val1, val3, ...], ..., [combN], ... ]
